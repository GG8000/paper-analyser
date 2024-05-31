def cutting_dois_into_array(doi_file):
    doi_arr = doi_file.split()
    return doi_arr
    

def scrape_paper():
    import urllib.request
    from bs4 import BeautifulSoup
    url = "https://www.sciencedirect.com/science/article/pii/S000632072300277X?via%3Dihub"
    open_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(open_page, "html.parser")
    section = soup.find_all(attrs={"id" : "s0010"})
    print(section.text.strip())

def scrape_packages():
    import urllib.request
    from bs4 import BeautifulSoup
    url = "https://cran.r-project.org/web/packages/available_packages_by_name.html"
    open_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(open_page, "html.parser")
    r_packages = soup.find_all(attrs={"class": "CRAN"});

    all_packages = []
    for package in r_packages:
        name=package.text.strip()
        if(len(name) > 1):
            all_packages.append(name)

    # output = open("cran_package.csv","a")
    # for package in all_packages:
    #      output.write(str(package) + "\n")

    return all_packages

#scrape_packages()

def download_from_doi():
    from scidownl import scihub_download
    import json

    with open("publications_bibsonomy.json", "r") as json_file:
        data = json.load(json_file)

    for key, entry in data.items():
        doi = entry.get("DOI", entry.get("doi", "N/A"))
        title = entry.get("title", "N/A")
        journal = entry.get("container-title", "N/A")
        
        paper_type = "doi"
        out = f"./upload/{title[0:10]}.pdf"
        proxies = {
            'http': 'socks5://127.0.0.1:7890'
        }
        scihub_download(doi, paper_type=paper_type, out=out, proxies=proxies)

#download_from_doi()

## Zeitlicher Trend der Package Nutzung
## Einzelne Informationen des Papers zugänglich machen, für spätere Auswertungen 
## Zotero oder Mendeley haben da Möglichkeit von PDFs die Infos auszulesen

def create_uploads_folder():
    import os
    # Specify the path to the local repository directory
    repo_directory = os.getcwd()  

    # Specify the name of the uploads folder
    uploads_folder = "uploads"

    # Combine the repository directory and the uploads folder path
    uploads_path = os.path.join(repo_directory, uploads_folder)

    # Check if the uploads folder exists
    if not os.path.exists(uploads_path):
        # If not, create the uploads folder
        os.makedirs(uploads_path)
        print(f"The '{uploads_folder}' folder has been created.")
    else:
        print(f"The '{uploads_folder}' folder already exists.")
