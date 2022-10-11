from common import get_soup
from bs4 import BeautifulSoup
import pandas as pd

print("testing console")
def scrape_boston():
    """Takes the Boston University faculty url and returns faculty name and their roles in  a list of lists."""

    school = "Boston University"
    soup = get_soup("https://www.bu.edu/econ/people/faculty/")
    profile = soup.find_all("ul", class_="profile-listing profile-format-basic")[0]
    li_tag = profile.find_all("li")

    output = []
    for n in range(len(li_tag)):
        name = li_tag[n].find_all("h6")[0].contents[0]
        job = li_tag[n].find_all("p")[0].contents[0]
        output.append([school,name,job])

    return output

testing = scrape_boston()
str_prof = 'Professor'
full = 'Professor of Economics'
try:
    full.index(str_prof)
except ValueError:
    print("Error")

test1 = testing[0]
print(test1)


