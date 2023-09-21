from pdfminer.high_level import extract_text


def find_pdfs():
    import os
    # assign directory
    directory = 'pdfs'
    pdfs=[]
    # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            if "DS_Store" not in f:
                pdfs.append(f)
    return pdfs

def examine_pdfs():
    pdfs = find_pdfs();
    methods = []
    for file in pdfs:
        # Search for keywords
        methods.append(search_pdfs_for_keywords(file))
    return methods

def search_pdfs_for_keywords(pdf):
    text = extract_text(pdf)
    text = list(text.split())
    used_packages = []
    try:
        methods_i = text.index("Methods")
        res_i = text.index("Results")
        interesting_list = text[methods_i:res_i]

        indices = [i for i, x in enumerate(interesting_list) if x == "package"]
        for i in indices:
            used_packages.append(interesting_list[i + 1]);
    except:
        print("No Results or Methods in pdf")
    return used_packages
    

    

print(examine_pdfs())

# Print all R Packages, which are used for research paper
# Maybe also automate that app get PDF from doi or bibtex File, download the paper and examine it for the R Package keywords
# Therefore use sci-hub 
# At first print R Packages just on screen



