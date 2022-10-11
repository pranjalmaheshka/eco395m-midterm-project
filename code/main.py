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


def get_data():
    '''Getting a final data as lists of lists and converting it to a Pandas df.'''
    
    raw_data = scrape_all()
    
    # send raw data to h-index file and add info

    raw_df = pd.DataFrame(raw_data, columns = ['University', 'Professor', "Title"])
    
    # final df needs to have relevant title + Google Scholar info

    #print(raw_df)    

get_data()

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

