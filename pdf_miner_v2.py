import fitz
import json
import os
import re
import requests
import glob
import pandas as pd
import PyPDF2
import crossref_commons.retrieval
from difflib import SequenceMatcher

def get_data_from_bibsonomy_export():
    # Load the JSON file
    with open("publications_bibsonomy.json", "r") as json_file:
        data = json.load(json_file)
    pubs = []
    # Iterate through the JSON objects and extract the desired information
    for key, entry in data.items():
        doi = entry.get("DOI", entry.get("doi", "N/A"))
        title = entry.get("title", "N/A")
        journal = entry.get("container-title", "N/A")
        pubs.append({
            "title":title,
            "doi":doi,
            "journal": journal,
        })
    return pubs


def get_metadata(pdf_path):
    pdf = PyPDF2.PdfFileReader(open(pdf_path, "rb"))
    metadata = pdf.getDocumentInfo()
    pubs = get_data_from_bibsonomy_export()
    #print(metadata)
    try:
        doi = metadata.get("/doi")
        title = metadata.get("/Title")
        year = metadata.get("/CreationDate")
        journal_issn = crossref_commons.retrieval.get_publication_as_json(doi)["ISSN"][0]
        journal_name = crossref_commons.retrieval.get_publication_as_json(doi)["container-title"][0]
    except:
        title = metadata.get("/Title")

        doi = get_doi_by_title(title)
        year = metadata.get("/CreationDate")
        journal_issn = crossref_commons.retrieval.get_publication_as_json(doi)["ISSN"][0]
        journal_name = crossref_commons.retrieval.get_publication_as_json(doi)["container-title"][0]
    
    return title, year[2:6], journal_issn, journal_name 

def get_journal_by_title(title_to_find):
    # Get the data from BibSonomy
    publications = get_data_from_bibsonomy_export()

    # Search for the title and return the DOI if found
    for publication in publications:
        if publication['title'] == title_to_find:
            return publication['journal']

    # Return None if the title is not found
    return None

def get_doi_by_title(title_to_find, similarity_threshold=0.8):
    # Get the data from BibSonomy
    publications = get_data_from_bibsonomy_export()

    # Search for the title and return the DOI if found
    for publication in publications:
        title = publication['title']
        similarity = title_similarity(title, title_to_find)
        if similarity >= similarity_threshold:
            return publication['doi']

    # Return None if the title is not found
    return None

def title_similarity(title1, title2):
    # Calculate the similarity between two titles using SequenceMatcher
    return SequenceMatcher(None, title1, title2).ratio()

def extract_publication_year(pdf_path):
    doc = fitz.open(pdf_path)

    # Regular expression pattern to match "Accepted" or "Published" dates
    date_pattern = r'(Accepted|Published|Received):\s+(\d{1,2}\s+\w+\s+\d{4})'
    
    accepted_year = None
    published_year = None
    text = ""
    
    for page_num in range(min(2, doc.page_count)):
        page = doc[page_num]
        text += page.get_text()
        date_matches = re.findall(date_pattern, text)
        
        for match in date_matches:
            event, date_str = match
            if event.lower() == "accepted":
                accepted_year = extract_year_from_date_str(date_str)
            elif event.lower() == "published":
                published_year = extract_year_from_date_str(date_str)
            elif event.lower() == "received in revised form":
                received_year = extract_year_from_date_str(date_str)
                if accepted_year is None:
                    accepted_year = received_year

        # Check for the "YYYY The Authors" pattern
        year_authors_match = re.search(r'(\d{4}) The Author(\(s\))?', text)
        if year_authors_match:
            year = int(year_authors_match.group(1))
            if accepted_year is None:
                accepted_year = year
            if published_year is None:
                published_year = year
        
         # Check for the "(YYYY)" pattern
        parentheses_year_match = re.search(r'\((\d{4})\)', text)
        if parentheses_year_match:
            year = int(parentheses_year_match.group(1))
            if accepted_year is None:
                accepted_year = year
            if published_year is None:
                published_year = year

    if accepted_year is not None and published_year is not None:
        return max(accepted_year, published_year)
    elif accepted_year is not None:
        return accepted_year
    elif published_year is not None:
        return published_year
    else:
        return None  # Year not found in publication_years

def extract_year_from_date_str(date_str):
    # Extract the year from the matched date string
    date_parts = date_str.split()
    for part in date_parts:
        if part.isnumeric() and 1900 <= int(part) <= 2100:
            return int(part)
    return None


def find_r_packages_in_pdf(pdf_path, filename, r_packages):
    found_packages = set()

    # Open the PDF file with PyMuPDF
    pdf_document = fitz.open(pdf_path)

    entire_paper_text = ""
    # Iterate through each page
    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        page_text = page.get_text()
        entire_paper_text += page_text

    # Define the regex pattern to find words in quotes
    pattern = r'[“"‘]([^”"’]+)[“"’]*'

    # Split the text into words
    words = entire_paper_text.split()

    # Initialize a list to store found R packages
    found_packages = []

    # Iterate through the words in the text
    for i, word in enumerate(words):
        # Check if the word is in the list of R packages
        if word.strip("'") in r_packages:
            # Initialize a flag to check for "and" in the range
            has_and = False
            has_and_and_bracket = False
            # Look for "and" within the range
            for j in range(max(0, i - 5), min(i + 11, len(words))):
                if words[j].lower() == "and":
                    if entire_paper_text[j] == ")":
                            has_and_and_bracket = True
                    else:
                        has_and = True
                    break
            # Expand the search range for two more words if "and" is found
            if has_and:
                for k in range(max(0, i - 5), min(i + 13, len(words))):
                    if words[k].lower() in ["package", "packages"]:
                        found_packages.append(word.strip("'"))
                        break
            elif has_and_and_bracket:
                for k in range(max(0, i - 5), min(i + 16, len(words))):
                    if words[k].lower() in ["package", "packages"]:
                        found_packages.append(word.strip("'"))
                        break
            else:
                # Look for the words "package," "Package," "Packages," or "packages" within 5 words before and after
                for j in range(max(0, i - 5), min(i + 6, len(words))):
                    if words[j].lower() in ["package", "packages"]:
                        found_packages.append(word.strip("'"))

    # Find words in quotes and compare with r_packages
    matches = re.finditer(pattern, entire_paper_text)
    for match in matches:
        word_in_quotes = match.group(1)
        # Check if the word in quotes is within the specified range of "package" or "packages"
        for j in range(max(0, match.start() - 5), min(match.end() + 5, len(entire_paper_text))):
            if entire_paper_text[j:j+len(word_in_quotes)].lower() == word_in_quotes.lower() and word_in_quotes in r_packages:
                has_and = False
                has_and_and_bracket = False
                # Look for "and" within the range
                for k in range(max(0, j - 5), min(j + 11, len(entire_paper_text))):
                    if entire_paper_text[k].lower() == "and":
                        if entire_paper_text[k] == ")":
                            has_and_and_bracket = True
                        else:
                            has_and = True
                        break
                # Expand the search range for two more words if "and" is found
                if has_and:
                    for m in range(max(0, j - 5), min(j + 13, len(entire_paper_text))):
                        if entire_paper_text[m:m+len(word_in_quotes)].lower() == word_in_quotes.lower() and word_in_quotes in r_packages:
                            found_packages.append(word_in_quotes)
                            break
                elif has_and_and_bracket:
                    for m in range(max(0, j - 5), min(j + 17, len(entire_paper_text))):
                        if entire_paper_text[m:m+len(word_in_quotes)].lower() == word_in_quotes.lower() and word_in_quotes in r_packages:
                            found_packages.append(word_in_quotes)
                            break
                else:
                    found_packages.append(word_in_quotes)

    # Remove duplicates from the found packages
    found_packages = list(set(found_packages))

    # Sort "and" out
    found_packages = [word for word in found_packages if word != "and"]

    # Print the found R packages
    #result_string = f"{filename} -> " + ", ".join(found_packages)
    #print(result_string)
    
    return found_packages


def visualization_used_packages(data, years, titles, issns, journals):
    # Extract unique package names
    unique_packages = set(package for _, packages in data for package in packages)
    
    # Create a dictionary to store the data
    data_dict = {}
    
    # Initialize data_dict with zeros for each package and a year column
    for package in unique_packages:
        data_dict[package] = [0] * len(data)
    data_dict['published_in'] = [0] * len(data)  # Initialize the year column
    
    # Iterate through the data to populate the data_dict
    for i, (paper_name, packages) in enumerate(data):
        for package in packages:
            data_dict[package][i] = 1
        year_value = years[i][1]
        data_dict['published_in'][i] = int(year_value) if year_value is not None else 0  # Set the year column value as an integer
    
    # Add titles as a new column
    data_dict['title'] = [title for _, title in titles]
    data_dict['journal'] = [journal for _, journal in journals]
    data_dict['issn'] = [issn for _, issn in issns]
    

    # Create the DataFrame
    df = pd.DataFrame(data_dict)
    
    # Set the paper names as the index
    df.index = [paper_name for paper_name, _ in data]
    
    # Reorder the columns
    df = df[['published_in'] + [col for col in df if col != 'published_in']]
    
    return df
    