import requests
import json
import datetime
import tqdm
import time
import os

URL = 'https://api.jikan.moe/v4'
WAIT_TIME = 1.1

def pageScrape(end, page, path):
    response = requests.get(f'{URL}{end}?page={page}')
    response.raise_for_status()
    data = response.json()
    with open(path, 'w') as file:
        json.dump(data['data'], file, indent=4)


def scrapeJikan(database):

    # create file if not exists
    path = f'data/raw/{database}'
    if not os.path.exists(path):
        os.makedirs(path)

    # Finds last page + calculates length
    last_page = requests.get(f'{URL}/{database}').json()['pagination']['last_visible_page']
    length = len(str(last_page))

    start = datetime.datetime.now()

    # Scrapes for each page
    for page in tqdm.trange(1, last_page + 1):
        start = time.perf_counter()
        pageScrape(f'/{database}', page, f'{path}/page{str(page).zfill(length)}.json')
        end = time.perf_counter()
        time.sleep(max(0, start + WAIT_TIME - end))

    finish = datetime.datetime.now()

    print(f'Time taken: {finish - start}\n ')

scrapeJikan('anime')
scrapeJikan('manga')