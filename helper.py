def cutting_dois_into_array(doi_file):
    doi_arr = doi_file.split();
    return doi_arr;
    

def scrape_paper():
    import urllib.request
    from bs4 import BeautifulSoup
    url = "https://www.sciencedirect.com/science/article/pii/S000632072300277X?via%3Dihub"
    open_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(open_page, "html.parser")
    section = soup.find_all(attrs={"id" : "s0010"});
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

    return all_packages
