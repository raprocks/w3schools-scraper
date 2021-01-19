import json
import requests
from bs4 import BeautifulSoup


def write_dict_to_json(data: dict, name: str):
    with open(f"{name}.json", "w+") as fd:
        fd.write(json.dumps(data, indent=2, sort_keys=True))


def get_soup(url: str):
    res = requests.get(url)  # get request
    soup = BeautifulSoup(res.content, features="lxml")  # Parse HTML
    return soup
