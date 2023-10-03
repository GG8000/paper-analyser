import fitz
import os
import re
from helper import scrape_packages
import glob

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
    result_string = f"{filename} -> " + ", ".join(found_packages)

    print(result_string)

with open('bioc_cran_packages.txt', 'r') as file:
    # Read the lines and remove leading/trailing whitespace
    package_names = [line.strip() for line in file.readlines()]

# Convert the list to a comma-separated string
package_string = ", ".join(package_names)

r_packages = package_names

folder_path = "./pdfs/"
pdf_files = glob.glob(os.path.join(folder_path, '*.pdf'))

print("Starting keyword search")
for file in pdf_files:
    filename = os.path.basename(file)
    find_r_packages_in_pdf(file, filename,r_packages)