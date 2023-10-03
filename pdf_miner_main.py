import fitz
import string
import glob
import os
from helper import scrape_packages
import re
import statistics




def search_pdfs_for_keywords():
    all_packages = scrape_packages()
    for pdf_files in glob.glob('*.pdf'):
         #access pdf files
        document = fitz.open(pdf_files)
        # count pdf file pages
        #document_page_numbers = document.pageCount

    
    keyword_search = []
    # read the first page to last page
    method_found = False
    discussion_found = False
    after_intro = False
    words_list = []
    for page in document:
        page_text = document[page.number].get_textpage().extractText()
        #print(page_text)
        #page_text = document[2].get_textpage().extractWORDS()
        
        

        # Search for mentions of R packages within the methods section
    
        mentioned_packages = []
    
        for package_name in all_packages:
            if re.search(rf'\b{package_name}\b', page_text, re.IGNORECASE):
                    mentioned_packages.append(package_name)

        # Print the mentioned R packages
        print("Mentioned R Packages:", mentioned_packages)

        ## PROBLEM HERE: PACKAGE NAMES ARE MOST OF THE TIME IN INVERTED COMMAS SO THE KEYWORDS DOESNT FIND IT

                
        #check if package, packages, R or any related keywords are in the word list, and just take the surroundings of it
        
            

             
        
    return keyword_search
                

            

    print(pdf_files, "->", keys)
    # store output file
    output = open("keyword dataset.csv","a")
    output.write(pdf_files + "\t" + str(keys) + "\n")


#print(search_pdfs_for_keywords())


# Predefined list of R packages
r_packages = scrape_packages()
longest_r_package_name = -1
average_package_length = sum( map(len, r_packages) ) / len(r_packages)
median_package_length = statistics.median(map(len,r_packages))
for package in r_packages:
     if len(package) > longest_r_package_name:
          longest_r_package_name = len(package)

#print(longest_r_package_name, average_package_length, median_package_length)


# Open the PDF file with PyMuPDF
for pdf_files in glob.glob('*.pdf'):
         #access pdf files
        pdf_document = fitz.open(pdf_files)
        # count pdf file pages
        #document_page_numbers = document.pageCount

# Initialize a variable to store the entire paper text
entire_paper_text = ""

# Iterate through each page
for page_number in range(pdf_document.page_count):
    page = pdf_document.load_page(page_number)
    page_text = page.get_textpage().extractText()
    # Append the text from the current page to the entire paper text
    entire_paper_text += page_text


# Find the positions of "package" or "packages" in the entire paper text
package_positions = [match.start() for match in re.finditer(r'\b\D?[Pp]ackages?\b', entire_paper_text, re.IGNORECASE)]
# Extract the surrounding text for further investigation
surrounding_text = []

for position in package_positions:
    # Define the number of characters to include before and after the word

    context_length = longest_r_package_name  # Adjust this value as needed
    #context_length = int(average_package_length) + 5
    # Extract the surrounding text
    start = max(0, position - context_length)
    end = min(len(entire_paper_text), position + context_length + len("packages"))
    context = entire_paper_text[start:end]
    
    surrounding_text.append(context)
    
#print(surrounding_text)
# Define the regex pattern to match words in single or double quotes

pattern = r'[“"‘]([^”"’]+)[“"’]*'

text = "".join(surrounding_text)
#print(text)
# Use re.findall to find all words in quotes in the text
found_words = re.findall(pattern, text)
print(text)
print(found_words)


r_packages_used = [word for word in found_words if word in r_packages]


print(r_packages_used)

new_text = text.split()


for word in new_text:
    if word in r_packages:
        r_packages_used.append(word)

print(r_packages_used)

## PROBLEM: WHAT IF PACKAGE IS FROM GITHUB AND NOT LISTED IN CRAN NOR BIOCONDUCTOR???
## MAYBE PRINT ALL WORDS WHICH ARE NEXT TO PACKAGE NAME INTO A SEPERATE LIST 

# Print the surrounding text for each occurrence of "package" or "packages"
# for i, context in enumerate(surrounding_text, 1):
#     print(f"Occurrence {i}:")
#     print(context)
#     print()

# Close the PDF document
pdf_document.close()






