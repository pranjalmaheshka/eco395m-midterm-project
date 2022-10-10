from common import get_soup


def scrape_princeton():
    """Takes the princeton faculty url and returns faculty name and their roles."""

    soup = get_soup("https://economics.princeton.edu/people/")
    posts_tag = soup.find_all("div", class_="posts")[0]
    people_tag = posts_tag.find_all("div", class_="person")

    output = []
    for n in range(len(people_tag)):
        name = people_tag[n].find_all("h3")[0].contents[0]
        job = people_tag[n].find_all("p", class_="job")[0].contents[0]
        output.append([name,job])

    return output


def scrape_boston():
    """Takes the Boston University faculty url and returns faculty name and their roles."""
    soup = get_soup("https://www.bu.edu/econ/people/faculty/")
    profile = soup.find_all("ul", class_="profile-listing profile-format-basic")[0]
    li_tag = profile.find_all("li")

    output = []
    for n in range(len(li_tag)):
        name = li_tag[n].find_all("h6")[0].contents[0]
        job = li_tag[n].find_all("p")[0].contents[0]
        output.append([name,job])

    return output

def scrape_harvard():
    """Takes the harvard faculty url and returns faculty name and their roles."""
    page1 = get_soup("https://economics.harvard.edu/faculty")
    div_tag = page1.find_all("div", id = "box-1592918309-page")[0]
    profile = div_tag.find_all("div", class_="person-teaser-wrapper")

    output = []
    for n in range(len(profile)):
        name = profile[n].find_all("a")[0].contents[0]
        job = profile[n].find_all("div", class_="field-item even")[0].contents[0]
        output.append([name,job])

    page2 = get_soup("https://economics.harvard.edu/faculty?sv_list_box_delta=1592918309&pager_id=0&destination=node/1314266&page=1")
    div_tag2 = page2.find_all("div", id = "box-1592918309-page")[0]
    profile2 = div_tag2.find_all("div", class_="person-teaser-wrapper")

    for n in range(len(profile2)):
        name = profile2[n].find_all("a")[0].contents[0]
        job = profile2[n].find_all("div", class_="field-item even")[0].contents[0]
        output.append([name,job])

    return output



def scrape_all():
    """
    Scrapes all universities examined, returning a list of lists containing faculty's name and their role.

    example output:
    output = [['Jane Doe', 'Professor'], ['John Smith', 'Associate Professor'], ...]
    """
    princeton = scrape_princeton()
    boston_u = scrape_boston()

    output = princeton + boston_u + harvard

    return output
