import os
import json
import pandas as pd
def concat_data_movies():
    name = './data/movies.csv'
    files = [file for file in os.listdir("./data") if file.endswith('.json')]
    df  = pd.DataFrame()
    for index, json_file in enumerate(files):
        part_df = pd.read_json(f'data/{json_file}')
        df = pd.concat([df,part_df])
    df.to_csv(name)
    return name
