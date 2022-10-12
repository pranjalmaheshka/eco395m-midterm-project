## Main file
import os
import pandas as pd
from common import get_soup
from scrape_pages import scrape_all

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
    Returns a list of lists, which includes ["school", "prof's name", "title"]
    """
    data = scrape_all()

    output = []
    for prof in data:
        title = prof[2].lower()
        if "research assistant professor" in title:
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


def get_data():
    '''Getting a final data as lists of lists and converting it to a Pandas df.'''

    raw_data = scrape_all()

    # send raw data to h-index file and add info

    raw_df = pd.DataFrame(raw_data, columns = ['University', 'Professor', 'Title'])

    # final df needs to have relevant title + Google Scholar info

    #print(raw_df)
    return None
#get_data()

def get_h_index(prof_info):

    return None

def tabulate_data(prof_info):
    return None


'''
def run_main()
    return None

if __name__ == "__main__":
    run)main()
    # code for testing
'''
