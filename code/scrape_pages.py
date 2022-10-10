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
    soup = get_soup("https://www.bu.edu/econ/people/faculty/")
    profile = soup.find_all("ul", class_="profile-listing profile-format-basic")[0]
    li_tag = profile.find_all("li")

    output = []
    for n in range(len(li_tag)):
        name = li_tag[n].find_all("h6")[0].contents[0]
        job = li_tag[n].find_all("p")[0].contents[0]
        output.append([name,job])

    return output


def scrape_all():
    princeton = scrape_princeton()
    boston_u = scrape_boston()

    output = princeton + boston_u
    print(output)
    return None


if __name__ == "__main__":


    scrape_all()
