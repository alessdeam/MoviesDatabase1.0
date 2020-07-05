import json
import sqlite3

conn = sqlite3.connect('movies.db')
c = conn.cursor()

# c.execute('''CREATE TABLE films(title text, gross real, budget real, date text , rating text, time real, distributor text, genre text, director text, imdb real)''')
#
# with open('movies.json', encoding="utf8") as f:
#     data = json.load(f)
#
# movies = []
#
# for i in data:
#     single_movie = (i['Titolo'], i['Worldwide_Gross'], i['Production_Budget'], i['Data di uscita'], i['MPAA_Rating'], i['Running_Time_min'], i['Distributor'], i['Major_Genre'], i['Regista'], i['IMDB_Rating'])
#     movies.append(single_movie)
#
c.execute('DELETE FROM films where director is null')

for row in c.execute('SELECT * FROM films ORDER BY title'):
    print(row[8])

conn.commit()

conn.close()
