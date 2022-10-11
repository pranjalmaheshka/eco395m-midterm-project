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

    output = princeton + boston_u + harvard + utaustin + uchicago

    return output