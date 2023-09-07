import os
import pandas as pd
os.chdir(r"C:\Users\Dr Poonam Pandey\Desktop\codsoft\recommendation system\Data")
data= pd.read_csv(r"C:\Users\Dr Poonam Pandey\Desktop\codsoft\recommendation system\Data\movie_metadata.csv")
print(data.head())
print (data.shape)
df = data[['genres', 'movie_title', 'imdb_score', 'movie_imdb_link']].copy()
print(df.head())

genres_all_movies = [df.loc[i]['genres'].split('|') for i in df.index]

genres = sorted(list(set([item for sublist in genres_all_movies for item in sublist])))
print(genres)
full_data= []
movie_titles= []
print(df)

df.to_csv('test.csv')
for i in df.index:
    movie_titles.append((df.loc[i]['movie_title'].strip(), i, df.loc[i]['movie_imdb_link'].strip()))
    movie_data = [1 if genre in df.loc[i]['genres'].split('|') else 0 for genre in genres]
    movie_data.append(df.loc[i]['imdb_score'])
    full_data.append(movie_data)
print(movie_titles[1])
print(full_data[0])
print(movie_titles)
