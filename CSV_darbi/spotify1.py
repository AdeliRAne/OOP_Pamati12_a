import pandas as pd
import csv

songs=[]

with open("spotify.csv", "r", encoding='utf8') as csv_file:
    reader=csv.DictReader(csv_file)
    for line in reader:
        songs.append(line)

df = pd.DataFrame(songs)

df.to_json("spotify.json", indent=4)

years = df['Year'].unique()
count_year = []

for year in years:
    song_count = df[df['Year']== year].shape[0]
    count_year.append(song_count)
print(year)
print(count_year)