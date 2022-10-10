'''Getting a list of professors in Duke's Economics Department'''
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

#from common import get_soup()

duke_url1 = 'https://econ.duke.edu/people/other-faculty/regular-rank-faculty'
    

def get_soup(url):
    '''Takes a url and returns a BeautifulSoup instance representing the HTML of the page.'''
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    return soup 

def duke_soups():
    duke_url2 = 'https://econ.duke.edu/people/appointed-faculty/secondary-faculty'
    duke_url3 = 'https://econ.duke.edu/people/other-faculty/instructional-faculty'
    duke_url4 = 'https://econ.duke.edu/people/other-faculty/emeritus-faculty'

    soup1 = get_soup(duke_url1)
    soup2 = get_soup(duke_url2)
    soup3 = get_soup(duke_url3)
    soup4 = get_soup(duke_url4)

    return soup1, soup2, soup3, soup4

#if __name__ == "__main__":
'''
    BASE_DIR = "artifacts"
    CSV_PATH = os.path.join(BASE_DIR, "duke_profs.csv")
    
    os.makedirs(BASE_DIR, exist_ok=True)

    write_duke(books, CSV_PATH)
'''
duke_profs1 = duke_soups()[0] # Regular rank faculty
duke_profs2 = duke_soups()[1] # Secondary faculty
duke_profs3 = duke_soups()[2] # Instructional faculty
duke_profs4 = duke_soups()[3] # Emeritus faculty

'''
duke_profurls = []
for tag in duke_profs1.find_all("div", class_ = "views-field views-field-field-profile-url-1"):
    for link in tag.find_all("a", href = True):
        duke_profurls.append(link['href'])
#print(f"List of prof urls {duke_profurls}")

duke_profnames = []
for tag in duke_profs1.find_all("div", class_ = "views-field views-field-field-profile-url-1"):
    for name in tag.find_all('div', class_='h4'):
        duke_profnames.append(name.a.text)
#print(f"List of prof names {duke_profnames}")

duke_proftitles = []
for tag in duke_profs1.find_all("div", class_ = "views-field views-field-field-appointment-titles"):
    duke_proftitles.append(tag.text)
#print(f"List of prof titles {duke_proftitles}")
'''

## Secondary Faculty
def get_duke_data():
    duke_profs1 = duke_soups()[0] # Regular rank faculty
    duke_profurls = []
    for tag in duke_profs1.find_all("div", class_ = "views-field views-field-field-profile-url-1"):
        for link in tag.find_all("a", href = True):
            duke_profurls.append(link['href'])
    #print(f"List of prof urls {duke_profurls}")

    duke_profnames = []
    for tag in duke_profs1.find_all("div", class_ = "views-field views-field-field-profile-url-1"):
        for name in tag.find_all('div', class_='h4'):
            duke_profnames.append(name.a.text)
    #print(f"List of prof names {duke_profnames}")

    duke_proftitles = []
    for tag in duke_profs1.find_all("div", class_ = "views-field views-field-field-appointment-titles"):
        duke_proftitles.append(tag.text)
    #print(f"List of prof titles {duke_proftitles}")

    return
    
def get_duke_final():

    return duke_final
