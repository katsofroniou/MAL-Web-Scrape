import pandas as pd
import requests
import json
import datetime
import tqdm
import time
import os

URL = 'https://api.jikan.moe/v4'
WAIT_TIME = 1.1

def idFromCsv(csv_path):
    df = pd.read_csv(csv_path)
    anime_ids = df['mal_id'].tolist()
    return anime_ids

def pageScrape(end, path):
    response = requests.get(f'{URL}{end}')
    response.raise_for_status()
    data = response.json()
    with open(path, 'w') as file:
        json.dump(data['data'], file, indent=4)

def scrapeJikanDetails(database, anime_ids):
    # create file if not exists
    path = f'data/raw/{database}/stats'
    if not os.path.exists(path):
        os.makedirs(path)

    length = len(str(len(anime_ids)))
    start = datetime.datetime.now()

    # Scrapes for each anime ID
    for idx, anime_id in tqdm.tqdm(enumerate(anime_ids, start=1), total=len(anime_ids),
                                   desc='Fetching Anime Statistics'):
        start = time.perf_counter()
        pageScrape(f'/anime/{anime_id}/statistics', f'{path}/anime{str(idx).zfill(length)}.json')
        end = time.perf_counter()
        time.sleep(max(0, start + WAIT_TIME - end))

    finish = datetime.datetime.now()
    print(f'Time taken: {finish - start}\n ')

CSV_PATH = 'data/anime.csv'
ANIME_IDS = idFromCsv(CSV_PATH)

scrapeJikanDetails('anime', ANIME_IDS)