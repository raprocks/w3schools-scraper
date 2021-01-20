from helpers import get_soup, write_dict_to_json


soup = get_soup("https://www.w3schools.com/tags/default.asp")

# Get Data Table
table = soup.find('div', id='htmltags')
# Get all "tr" table rows from table
rows = []
for each in table.findAll('tr'):
    rows.append(each)

data_dict = {}
# Get data from rows
for row in rows:
    column = row.findAll('td')
    if len(column) == 0:  # if row with no td parsed
        continue
    try:
        html5tag = "html5badge" in column[0].attrs.get('class', "")
        tagname = column[0].text
        tag_descriptions = (column[1].text.strip()
                            .replace("\\u00a0", '')
                            .replace("\n", '')
                            .replace("\r", ''))
        tagref_link = "https://www.w3schools.com/tags/" + column[0].a['href']
        identifier = column[0].a['href'].split("_")[1].split(".asp")[0]
        print(identifier, "found")
        data_dict[identifier] = {
            "name": tagname,
            "short_description": tag_descriptions,
            "reflink": tagref_link,
            "html5": html5tag
        }
    except IndexError as error:
        print("IndexError, index not in column", error)
    except TypeError as error:
        print("TypeError, attribute not in tag", error)

write_dict_to_json(data_dict, "HtmlShortRef")
