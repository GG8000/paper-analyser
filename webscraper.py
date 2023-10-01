import urllib.request
from bs4 import BeautifulSoup
url = "https://cran.r-project.org/web/packages/available_packages_by_name.html"
open_page = urllib.request.urlopen(url)
soup = BeautifulSoup(open_page, "html.parser")
print(soup)