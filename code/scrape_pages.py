from common import get_soup

def scrape_princeton():
    """Takes the princeton faculty url and returns faculty name and their roles in  a list of lists."""

    school = "Princeton University"
    soup = get_soup("https://economics.princeton.edu/people/")
    posts_tag = soup.find_all("div", class_="posts")[0]
    people_tag = posts_tag.find_all("div", class_="person")

    output = []
    for n in range(len(people_tag)):
        name = people_tag[n].find_all("h3")[0].contents[0]
        job = people_tag[n].find_all("p", class_="job")[0].contents[0]
        output.append([school,name,job])

    return output


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


def scrape_harvard():
    """Takes the harvard faculty urls and returns faculty name and their roles in  a list of lists."""
    urls = ["https://economics.harvard.edu/faculty","https://economics.harvard.edu/faculty?sv_list_box_delta=1592918309&pager_id=0&destination=node/1314266&page=1"]
    total = []
    for link in urls:
        page = get_soup(link)
        div_tag = page.find_all("div", id = "box-1592918309-page")[0]
        profile_soup = div_tag.find_all("div", class_="person-teaser-wrapper")
        total.append(profile_soup)

    school = "Harvard University"
    output = []
    for url in total:
        for n in range(len(url)):
            name = url[n].find_all("a")[0].contents[0]
            job = url[n].find_all("div", class_="field-item even")[0].contents[0]
            output.append([school,name,job])

    return output


def scrape_utaustin():
    """Takes the UT Austin faculty url and returns faculty name and their roles in  a list of lists."""
    url = "https://catalog.utexas.edu/undergraduate/liberal-arts/faculty/"
    soup = get_soup(url)
    div_tag = soup.find_all("div", class_="facultylist")[0]
    profiles = div_tag.find_all("p", class_="faculty_entry")

    school = "University of Texas at Austin"
    output = []
    for n in range(len(profiles)):
        dept = profiles[n].find_all("span", class_="faculty_dept")[0].contents[0]
        if "Economics" in dept:
            name = profiles[n].find_all("span", class_="faculty_name")[0].contents[0]
            job = profiles[n].find_all("span", class_="faculty_title")[0].contents[0]
            output.append([school,name, job])

    return output


def scrape_uchicago():
    """Takes the University of Chicago faculty url and returns faculty name and their roles in  a list of lists."""
    url = "https://economics.uchicago.edu/directories/full/faculty"
    soup = get_soup(url)
    div_block = soup.find_all("div", class_="view-content")[1]
    profiles = div_block.find_all("div", class_="views-row")

    school = "University of Chicago"
    output=[]
    for n in range(41):
        name = profiles[n].find_all("a")[0].contents[0]
        job = profiles[n].find_all("p", class_="title")[0].contents[0].lstrip().rstrip()
        output.append([school,name,job])

    return output

def scrape_duke():
    """Takes the Duke University faculty url and returns faculty name and their roles in  a list of lists."""
    
    duke_url1 = 'https://econ.duke.edu/people/other-faculty/regular-rank-faculty'
    duke_profs = get_soup(duke_url1) # Regular rank faculty
    
    duke_profurls = []
    duke_profnames = []
    duke_proftitles = []
    
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

def scrape_northwestern():
    """Takes the Northwestern University faculty url and returns faculty name and their roles in  a list of lists."""
    
    nw_url = 'https://economics.northwestern.edu/people/faculty/index.html'
    nw_profs = get_soup(nw_url) # Faculty (minus Emeritus + Instructional)
    
    nw_profnames = []
    nw_proftitles = []

    for tag in nw_profs.find_all("div", class_ = "people-content"):
        for name in tag.find_all('h3'):
            nw_profnames.append(name.a.text)

    for tag in nw_profs.find_all("div", class_ = "people-content"):
        for title in tag.find_all('p', class_="title"):      
            nw_proftitles.append(title.text)

    northwestern = []
    for i in range(len(nw_profnames)):
        temp=[]
        temp.append("Northwestern University")
        temp.append(nw_profnames[i])
        temp.append(nw_proftitles[i])
        northwestern.append(temp)
    return northwestern 

def scrape_stanford():
     """Takes the Stanford University faculty url and returns faculty name and their roles in  a list of lists."""

    url = "https://economics.stanford.edu/people/faculty"
    soup = get_soup(url)
        
    names = soup.find_all("span", {"class": "field-content hb-subtitle"})

    facnames = []

    for i in names: 
        allfac = i.a.text 
        facnames.append(allfac)

    titles = soup.find_all("div", {"class": "views-field views-field-field-hs-person-title"}) 

    factitles = []

    for i in titles: 
        alltitles = i.div.text 
        factitles.append(alltitles)

    stanford = []
    school = "Stanford University"
    list_stanford = len(factitles)

    for i in range(list_stanford): 
        temp = []
        temp.append(school)
        temp.append(facnames[i])
        temp.append(factitles[i])
        stanford.append(temp)

    return stanford

def scrape_nyu():
     """Takes the New York University faculty url and returns faculty name and their roles in  a list of lists."""
    url = "https://as.nyu.edu/departments/econ/faculty.html"
    soup = get_soup(url)

    names = soup.find_all("h2", {"class": "book-box__title theme__head--medium"})

    facnames = []

    for i in names: 
        allfac = i.string 
        facnames.append(allfac)

    titles = soup.find_all("div", {"class": "book-box__author"})

    factitles = []

    for i in titles: 
        alltitles = i.string.lstrip().rstrip()
        factitles.append(alltitles)

    nyu = []

    school = "New York University"
    list_nyu = len(factitles)

    for i in range(list_nyu): 
        temp = []
        temp.append(school)
        temp.append(facnames[i])
        temp.append(factitles[i])
        nyu.append(temp)

    nyu


def Columbia():
    """Takes the columbia faculty url and returns faculty name and their roles in  a list of lists."""
    soup= get_soup("https://econ.columbia.edu/faculty/")
    div_tag= soup.find_all("div", class_="tshowcase-isotope-wrap")[0]
    profiles= div_tag.find_all("div", class_= "tshowcase-box-info ts-align-left")
    school= "Columbia"
    output=[]
    for n in range(len(profiles)):
        names = profiles[n].find_all("div", class_= "tshowcase-box-title")[0].contents[0]
        title = profiles[n].find_all("div", class_="tshowcase-single-position") [0].contents[0]
        output.append([school,names,title])
    
    return output

def Brown():
    school="Brown"
    soup= get_soup("https://economics.brown.edu/people/faculty")
    ul_tag = soup.find_all("ul", class_ = "people_items component_items")[0]
    profiles= ul_tag.find_all("li")

    output=[]
    for n in range(len(profiles)):

        title = profiles[n].find_all("div", class_="people_item_title")[0].contents[0]
        title = title.replace("\n","").strip()
        name = profiles[n].find_all("h3",class_ ="people_item_name")[0].find_all("a")[0].contents[0]
        name = name.replace("\n","").strip()
        output.append([school,name,title])

    return output



def scrape_all():
    """
    Scrapes all universities examined, returning a list of lists containing faculty's name and their role.

    example output:
    output = [['University A', 'Jane Doe', 'Professor'], ['University A', 'John Smith', 'Associate Professor'], ...]
    """
    princeton = scrape_princeton()
    boston_u = scrape_boston()
    harvard = scrape_harvard()
    utaustin = scrape_utaustin()
    uchicago = scrape_uchicago()
    duke = scrape_duke()
    northwestern = scrape_northwestern()
    stanford = scrape_stanford()
    nyu = scrape_nyu()
    columbia = Columbia()
    brown = Brown()

    output = princeton + boston_u + harvard + utaustin + uchicago + duke + northwestern + stanford + nyu + columbia + brown

    return output
