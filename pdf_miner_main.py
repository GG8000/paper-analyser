import fitz
import glob
import os
from helper import scrape_packages




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
        content_words = document[page.number].get_textpage().extractWORDS()
        #content_words = document[2].get_textpage().extractWORDS()
        for word in content_words:
            # Search for Word Method
            investigate_word = word[4]
            #print(investigate_word.lower())
            if investigate_word.lower() == "introduction":
                after_intro = True
                #print("Found Introduction")
            if investigate_word.lower() == "methods":
                method_found = True
                #print("Found Methods")
            if method_found and after_intro and not discussion_found:
                words_list.append(investigate_word)
            # Search for Word Result
            if investigate_word.lower() == "discussion":
                discussion_found = True
                method_found = False
        
        #print(words_list)
        #if len(words_list) == 0:
            #print("Next Page")
                
        #check if package, packages, R or any related keywords are in the word list, and just take the surroundings of it
        r_words = ["package", "packages", "R"]
        r_words_index_in_words_list = []
        for word in r_words:
            print(word)
            # go through every word and search it in the word_list.
            # save indicies in array for further observations
            if word in words_list:
                r_words_index_in_words_list.append(words_list.index(word))
            
        for keyword in all_packages:    
            # Go through words_list and check for keywords
                
            if "packages" or "packages" in words_list:
                    keyword_search.append(keyword)

             
        
    return keyword_search
                

            

    print(pdf_files, "->", keys)
    # store output file
    output = open("keyword dataset.csv","a")
    output.write(pdf_files + "\t" + str(keys) + "\n")


print(search_pdfs_for_keywords())







