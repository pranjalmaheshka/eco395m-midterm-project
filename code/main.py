## Main file
import os
import pandas as pd
from common import get_soup
from scrape_pages import scrape_all
from search_keys import search_keys
import csv


colleges = [
    'harvard','princeton','uchicago',
    'stanford','pennstate','yale',
    'northwestern','duke','umd',
    'hopkins','bu','wisconsin','uta'
    ]

def clean_titles():
    """
    Runs through the scraped data and filters through faculty titles.
    Keep "Professor", "Associate Professor", and "Assistant Professor" titles only.
    Returns a list of lists, which includes [["school", "prof's name", "title"], ...]
    """
    data = scrape_all()

    output = []
    for prof in data:
        title = prof[2].lower()
        if "research assistant professor" in title:
            continue
        elif "research professor" in title:
            continue
        elif "clinical" in title:
            continue
        elif "lecturer" in title:
            continue
        elif "emeritus" in title:
            continue
        elif "adjunct" in title:
            continue
        elif "visiting" in title:
            continue
        elif "professor of instruction" in title:
            continue
        elif "associate professor" in title:
            output.append([prof[0],prof[1],"Associate Professor"])
        elif "assistant professor" in title:
            output.append([prof[0],prof[1],"Assistant Professor"])
        elif "professor" in title:
            output.append([prof[0],prof[1],"Professor"])
        else:
            continue

    return output



def get_h_index():
    '''Extract h index, h index since 2017, citations all, citations since 2017 for each faculty member'''
    faculty = clean_titles()
    keywords = search_keys()

    faculty_info = [] #[name, title, h index all, h index since 2017, citations all, citations since 2017]

    for i in faculty:
        individual_info = []
        school = i[0]
        name = i[1]
        title = i[2]
        individual_info.append(school)
        individual_info.append(name)
        individual_info.append(title)
        sep_name = name.replace(" ", "+")

        #Get url of the individual faculty member's google scholar page
        soup = get_soup2("https://scholar.google.com/citations?view_op=search_authors&mauthors=" + sep_name + "&hl=en&oi=ao")
        search_results = soup.find_all("div", class_="gsc_1usr") #individual entries

        found_indicator = 0
        for i in search_results:
            individual_result = i.find("div", class_="gs_ai_aff").text #current affiliation
            for x in keywords[school]:
                if x in individual_result:
                    found_indicator = 1
                    matched_faculty = i
                    break

        if found_indicator == 1:
            soup = get_soup2("https://scholar.google.com/"+ matched_faculty.find("div", class_="gs_ai gs_scl gs_ai_chpr").a["href"])
            data_tag = soup.find_all("td", class_="gsc_rsb_std")

            individual_info.append(data_tag[0].text) #citations all
            individual_info.append(data_tag[1].text) #citations since 2017

            individual_info.append(data_tag[2].text) #h index all
            individual_info.append(data_tag[3].text) #h index since 2017

            faculty_info.append(individual_info)

        elif found_indicator == 0:
            individual_info.append("")
            individual_info.append("")

            individual_info.append("")
            individual_info.append("")
            faculty_info.append(individual_info)

    return faculty_info

def write_data_to_csv(data, path):
    """Write the data to the csv.    """
    # [name, title, h index all, h index since 2017, citations all, citations since 2017]
    headers = ["university", "name","title", "citations", "citations2017", "h_index", "h_index2017"]
    with open(path, "w+", newline="") as out_file:
        write = csv.writer(out_file)
        write.writerow(headers)
        write.writerows(data)



if __name__ == "__main__":
    data = get_h_index()
    OUTPUT_DIR = "artifacts"
    OUTPUT_PATH = os.path.join(OUTPUT_DIR, "scores.csv")
    write_data_to_csv(data, OUTPUT_PATH)
