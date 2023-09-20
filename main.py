from pdfminer.high_level import extract_text


def examine_text_for_keywords(pdf):
    text = extract_text(pdf)

    return text

pdf_list = []

for pdf in pdf_list:
    examine_text_for_keywords(pdf)

# Print all R Packages, which are used for research paper
# Maybe also automate that app get PDF from doi or bibtex File, download the paper and examine it for the R Package keywords
# Therefore use sci-hub 
# At first print R Packages just on screen



