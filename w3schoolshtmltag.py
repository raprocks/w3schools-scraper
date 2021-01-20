import json
from helpers import get_soup, write_dict_to_json
from bs4 import BeautifulSoup


def scrape_tag(tagurl: str):
    soup = get_soup(tagurl)
    main_div = soup.find('div', 'id')
    # identifier = tagurl.split('/')[-1].split('tag_')[1].split('.asp')[0]
    soup = get_soup(tagurl)
    main_div = soup.find('div', id="main")
    br_tag = BeautifulSoup().new_tag(name='br')
    hr_tag = BeautifulSoup().new_tag(name='hr')
    # replace target tree with tree after first <br/> tag
    main_div_list = list(main_div)
    br_tag_index = main_div_list.index(br_tag)
    main_div_list = main_div_list[br_tag_index:]
    main_div = BeautifulSoup("".join(map(str, main_div_list)))
    # get table of compatibility
    # compatability_table = main_div.find('table')
    parts = []
    for i in range(len(main_div.find_all('hr'))):
        hr_index = main_div_list.index(hr_tag)
        parts.append(main_div_list[:hr_index])
        main_div_list = main_div_list[hr_index+1:]
    parts.append(main_div_list)
    description = ""
    event_attributes_support = False
    standard_attributes_support = False
    support_dict = {}
    for part in parts:
        local_soup = BeautifulSoup("".join(map(str, part)))
        if local_soup.h2 is None:
            continue
        elif local_soup.h2.text == "Definition and Usage":
            description = ''
            p_tags = local_soup.find_all('p')
            for p in p_tags:
                description += (p.text
                                .strip()
                                .replace("\\u00a0", '')
                                .replace("\n", '')
                                .replace("\r", ''))
        elif local_soup.h2.text == "Browser Support":
            support_dict = {}
            local_table = local_soup.table
            ths = local_table.find_all('th')
            tds = local_table.find_all('td')
            datazip = zip(ths, tds)
            for browser, support in datazip:
                if browser.get('title') is None:
                    continue
                title = browser["title"]
                support_dict[title] = True if support.text.lower(
                ).strip() == "yes" else False
        elif local_soup.h2.text == "Standard Attributes":
            if local_soup.p == "The comment tag does not support any standard attributes.":
                standard_attributes_support = False
            else:
                standard_attributes_support = True
        elif local_soup.h2.text == "Event Attributes":
            if local_soup.p == "The comment tag does not support any event attributes.":
                event_attributes_support = False
            else:
                event_attributes_support = True
        else:
            title = local_soup.h2
            print(title)
            break
    return_dict = {
        'description': description,
        'event_attributes_support': event_attributes_support,
        'standard_attributes_support': standard_attributes_support,
        'browser_support': support_dict
    }
    return return_dict


if __name__ == "__main__":

    with open("HtmlShortRef.json") as fd:
        data_dict = json.loads(fd.read())

    for key in data_dict.keys():
        print(key)
        reflink = data_dict[key]["reflink"]
        scraped = scrape_tag(reflink)
        data_dict[key].update(scraped)
    # write_dict_to_json(data_dict, "HtmlBigRef")
