def cutting_dois_into_array(doi_file):
    doi_arr = doi_file.split();
    return doi_arr;

def generate_keywords_for_selection(selection):
    keywords=[];
    if selection=="r":
        keywords=["R", "package", "packages"]
    elif selection == "methods":
        keywords=["methods"]
    else:
        keywords=["R", "Package"]

    return keywords