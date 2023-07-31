import pandas as pd

def convert_aired(aired_str):
    if isinstance(aired_str, str):
        aired_dict = eval(aired_str)  # Safely evaluate the string as a dictionary
        return f"{aired_dict['from']['string']} to {aired_dict['to']['string']}"
    return ""

def convert_published(published_str):
    if isinstance(published_str, str):
        published_dict = eval(published_str)  # Safely evaluate the string as a dictionary
        return f"{published_dict['from']['string']} to {published_dict['to']['string']}"
    return ""

def anime():
    with open('data/raw/anime.json', 'r', encoding='utf-8') as file:
        data = pd.read_json(file)

    # Define the columns you want to include in the CSV
    columns = [
        "mal_id", "title", "type", "source", "episodes", "status", "airing",
        "aired", "duration", "rating", "score", "scored_by", "rank", "popularity",
        "members", "favorites", "season", "year", "producers", "licensors",
        "studios", "genres", "explicit_genres", "themes", "demographics"
    ]

    # Flatten the nested JSON structure and create a list of dictionaries
    flat_data = []
    for entry_list in data.values:
        for entry in entry_list:
            if entry is not None:
                flat_data.append(entry)

    # Create a DataFrame from the flat_data
    df = pd.DataFrame(flat_data)

    # Convert lists of dictionaries to a comma-separated string of names for producers, licensors, studios, genres, explicit_genres, themes, and demographics
    df["producers"] = df["producers"].apply(lambda x: ", ".join([producer["name"] for producer in x]))
    df["licensors"] = df["licensors"].apply(lambda x: ", ".join([licensor["name"] for licensor in x]))
    df["studios"] = df["studios"].apply(lambda x: ", ".join([studio["name"] for studio in x]))
    df["genres"] = df["genres"].apply(lambda x: ", ".join([genre["name"] for genre in x]))
    df["explicit_genres"] = df["explicit_genres"].apply(lambda x: ", ".join(x))
    df["themes"] = df["themes"].apply(lambda x: ", ".join([theme["name"] for theme in x]))
    df["demographics"] = df["demographics"].apply(lambda x: ", ".join([item["name"] for item in x]))

    # Convert the "aired" column
    df["aired"] = df["aired"].apply(convert_aired)

    # Save the DataFrame to a CSV file
    df.to_csv("data/anime_data.csv", index=False, columns=columns)

def manga():
    with open('data/raw/manga.json', 'r', encoding='utf-8') as file:
        data = pd.read_json(file)

    # Define the columns you want to include in the CSV
    columns = [
        "mal_id", "title", "type", "chapters", "volumes", "status", "publishing",
        "published", "score", "scored_by", "rank", "popularity",
        "members", "favorites", "authors", "serializations", "genres",
        "explicit_genres", "themes", "demographics"
    ]

    # Flatten the nested JSON structure and create a list of dictionaries
    flat_data = []
    for entry_list in data.values:
        for entry in entry_list:
            if entry is not None:
                flat_data.append(entry)

    # Create a DataFrame from the flat_data
    df = pd.DataFrame(flat_data)

    # Convert lists of dictionaries to a comma-separated string of names for authors, serializations, genres, explicit_genres, themes, and demographics
    df["authors"] = df["authors"].apply(lambda x: ", ".join([author["name"] for author in x]))
    df["serializations"] = df["serializations"].apply(lambda x: ", ".join([serialization["name"] for serialization in x]))
    df["genres"] = df["genres"].apply(lambda x: ", ".join([genre["name"] for genre in x]))
    df["explicit_genres"] = df["explicit_genres"].apply(lambda x: ", ".join(x))
    df["themes"] = df["themes"].apply(lambda x: ", ".join([theme["name"] for theme in x]))
    df["demographics"] = df["demographics"].apply(lambda x: ", ".join([item["name"] for item in x]))

    # Convert the "published" column
    df["published"] = df["published"].apply(convert_published)

    # Save the DataFrame to a CSV file
    df.to_csv("data/manga_data.csv", index=False, columns=columns)

# anime()
manga()