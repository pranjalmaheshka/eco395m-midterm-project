'''Getting a list of professors and titles in Duke's Economics Department'''
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

#from common import get_soup()

def get_soup(url):
    '''Takes a url and returns a BeautifulSoup instance representing the HTML of the page.'''
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    return soup 

def duke_soups():
    duke_url1 = 'https://econ.duke.edu/people/other-faculty/regular-rank-faculty'
    duke_url2 = 'https://econ.duke.edu/people/appointed-faculty/secondary-faculty'
    duke_url3 = 'https://econ.duke.edu/people/other-faculty/instructional-faculty'
    duke_url4 = 'https://econ.duke.edu/people/other-faculty/emeritus-faculty'

    soup1 = get_soup(duke_url1) # Regular rank faculty
    soup2 = get_soup(duke_url2) # Secondary faculty
    soup3 = get_soup(duke_url3) # Instructional faculty
    soup4 = get_soup(duke_url4) # Emeritus faculty

    return soup1, soup2, soup3, soup4

def duke():
    duke_profurls = []
    duke_profnames = []
    duke_proftitles = []
    

    duke_profs = get_soup(duke_url1)
    for tag in duke_profs.find_all("div", class_ = "views-field views-field-field-profile-url-1"):
        for link in tag.find_all("a", href = True):
            duke_profurls.append(link['href'])

    for tag in duke_profs.find_all("div", class_ = "views-field views-field-field-profile-url-1"):
        for name in tag.find_all('div', class_='h4'):
            duke_profnames.append(name.a.text)
    
    for tag in duke_profs.find_all("div", class_ = "views-field views-field-field-appointment-titles"):
        duke_proftitles.append(tag.text)
    
    duke = []
    for i in range(len(duke_profnames)):
        temp=[]
        temp.append("Duke University")
        temp.append(duke_profnames[i])
        temp.append(duke_proftitles[i])
        duke.append(temp)

    return duke

