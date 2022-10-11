## Main file
import os
import bs4 as BeautifulSoup
import pandas as pd
import requests

from common import get_soup()

from harvard import harvard
from princeton import princeton
from uchicago import uchicago
from stanford import stanford
from pennstate import pennstate
from yale import yale
from northwestern import northwestern
from duke import duke
from umd import umd
from hopkins import hopkins
from bu import bu
from wisconsin import wisconsin
from uta import uta

colleges = [
    'harvard','princeton','uchicago',
    'stanford','pennstate','yale',
    'northwestern','duke','umd',
    'hopkins','bu','wisconsin','uta'
    ]

def tab_data()
    raw_data = []
    #for college in colleges:
    #    raw_data.append(college)

def get_h_index(prof_info)
    return prof_h_index

def tabulate_data(prof_info)
    return None


'''
def run_main()
    return None

if __name__ == "__main__":
    run)main()
    # code for testing
'''

