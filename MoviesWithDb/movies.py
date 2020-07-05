import justpy as jp
import json
import sqlite3
import profile


class MovieDatabase:

 def list_movies(self):

    # genera la lista dei film del genere scelto
    def view_genre(self, msg):
         conn = sqlite3.connect('movies.db')
         c = conn.cursor()
         genre = (self.text,)
         for row in c.execute('SELECT * FROM films WHERE genre=?', genre):
             li.text = f'Genere selezionato: {self.text}'
             body_table = jp.Tbody(style='overflow:auto;', a=movie_table)
             row_table = jp.Tr(style='')
             div_table1 = jp.Td(style='width: 447px;', a=row_table)
             div_title_film = jp.Div(style='cursor: pointer;', text=row[0], a=div_table1, click=open_film)
             div_table2 = jp.Td(style='width: 183px;', a=row_table)
             div_director_film = jp.Div(style='cursor: pointer;', text=row[8], a=div_table2, click=open_film)
             div_table3 = jp.Td(style='width: 100px;', a=row_table)
             div_date_film = jp.Div(style='cursor: pointer;', text=row[3], a=div_table3, click=open_film)
             div_title_film.additional_properties = row
             div_director_film.additional_properties = row
             div_date_film.additional_properties = row
             row_table.additional_properties = {'Titolo': row[0], 'Regista': row[8], 'Data di uscita': row[3]}
             body_table.add(row_table)

         conn.commit()

         conn.close()
         button_sort_director.additional_properties = [self.text, 'Regista']
         button_sort_title.additional_properties = [self.text, 'Titolo']
         li2.set_classes('block')
         div1.remove_component(div2)
         movie_table.add(body_table)
         div1.add(div_sort_buttons)
         div1.add(movie_table)

    #genera la lista ordinata in base al titolo
    def sort_by_title(self, msg):
        movie_table.delete_components()
        body_table_title_sorted = jp.Tbody(style='overflow:auto;')
        conn = sqlite3.connect('movies.db')
        c = conn.cursor()
        for row in c.execute('SELECT * FROM films ORDER BY title'):
            if row[7] == self.additional_properties[0]:
                li.text = f'Genere selezionato: {self.additional_properties[0]}'
                row_table = jp.Tr(style='')
                div_table1 = jp.Td(style='width: 447px;', a=row_table)
                div_title_film = jp.Div(style='cursor: pointer;', text=row[0], a=div_table1, click=open_film)
                div_table2 = jp.Td(style='width: 183px;', a=row_table)
                div_director_film = jp.Div(style='cursor: pointer;', text=row[8], a=div_table2, click=open_film)
                div_table3 = jp.Td(style='width: 100px;', a=row_table)
                div_date_film = jp.Div(style='cursor: pointer;', text=row[3], a=div_table3,
                                       click=open_film)
                div_title_film.additional_properties = row
                div_director_film.additional_properties = row
                div_date_film.additional_properties = row
                body_table_title_sorted.add(row_table)
        movie_table.add(body_table_title_sorted)

    #genera la lista ordinata in base al regista
    def sort_by_director(self, msg):
        movie_table.delete_components()
        body_table_sorted = jp.Tbody(style='overflow:auto;')
        conn = sqlite3.connect('movies.db')
        c = conn.cursor()
        for row in c.execute('SELECT * FROM films ORDER BY director'):
            if row[7] == self.additional_properties[0]:
                li.text = f'Genere selezionato: {self.additional_properties[0]}'
                row_table = jp.Tr(style='')
                div_table1 = jp.Td(style='width: 447px;', a=row_table)
                div_title_film = jp.Div(style='cursor: pointer;', text=row[0], a=div_table1, click=open_film)
                div_table2 = jp.Td(style='width: 183px;', a=row_table)
                div_director_film = jp.Div(style='cursor: pointer;', text=row[8], a=div_table2, click=open_film)
                div_table3 = jp.Td(style='width: 100px;', a=row_table)
                div_date_film = jp.Div(style='cursor: pointer;', text=row[3], a=div_table3,
                                       click=open_film)
                div_title_film.additional_properties = row
                div_director_film.additional_properties = row
                div_date_film.additional_properties = row
                body_table_sorted.add(row_table)
        movie_table.add(body_table_sorted)

    #dalla visualizzazione del singolo film, torna alla lista
    def return_to_list(self, msg):
        div_sort_buttons.set_class('block')
        p_title.set_classes('hidden')
        p_director.set_classes('hidden')
        p_date.set_classes('hidden')
        p_gross.set_classes('hidden')
        p_budget.set_classes('hidden')
        p_rating.set_classes('hidden')
        p_distributor.set_classes('hidden')
        p_imdb_rating.set_classes('hidden')
        p_time.set_classes('hidden')
        tasto_indietro_lista_film.set_classes('hidden')
        tasto_indietro.set_classes('block')
        movie_table.set_classes("block")
        li.set_classes('block')
        button_sort_director.on('click', sort_by_director)

    #apre la pagina di visualizzazione di un singolo film
    def open_film(self, msg):
        div_sort_buttons.set_class('hidden')
        tasto_indietro_lista_film.set_classes('block')
        tasto_indietro.set_classes('hidden')
        movie_table.set_classes("hidden")
        li.set_classes("hidden")
        p_title.set_classes('block')
        p_director.set_classes('block')
        p_date.set_classes('block')
        p_gross.set_classes('block')
        p_budget.set_classes('block')
        p_rating.set_classes('block')
        p_distributor.set_classes('block')
        p_imdb_rating.set_classes('block')
        p_time.set_classes('block')
        p_title.text = 'Titolo: ' + self.additional_properties[0]
        p_director.text = 'Regista: ' + self.additional_properties[8]
        p_date.text = 'Data di uscita: ' + self.additional_properties[3]
        p_gross.text = 'Incasso totale: ' + str(self.additional_properties[1])
        p_budget.text = 'Budget: ' + str(self.additional_properties[2])
        p_rating.text = 'Rating: ' + self.additional_properties[4]
        p_distributor.text = 'Distributore: ' + self.additional_properties[6]
        p_imdb_rating.text = 'Punteggio su IMDB: ' + str(self.additional_properties[9])
        if (self.additional_properties[5] != None):
            p_time.text = 'Durata: ' + str(self.additional_properties[5]) + ' minuti'

    # cProfile.run('view_genre')
    profile.runctx('view_genre', None, locals())

    #torna alla selezione del genere
    def remove_genre(self, msg):
          li.text='Benvenuto su MovieDatabase, scegli un genere:'
          div1.add(div2)
          li2.set_classes('hidden')
          movie_table.delete_components()
          div1.remove_component(div_sort_buttons)
          div1.remove_component(movie_table)
          button_sort_director.on('click', sort_by_director)
          body_table.set_classes('block')

    # istanze di classi di JustPy
    wp = jp.WebPage()
    ul = jp.Ul(
        style='margin-bottom: 0px;overflow: hidden;background-color: #C3C3C3;border-top-right-radius:.225rem;border-top-left-radius:.225rem',
        a=wp, classes='shadow-md m-2 p-2')
    li = jp.Li(style='margin-left: 1%;text-decoration: none;float: left;color: black;font-size:20px',
               text='Benvenuto su MovieDatabase, scegli un genere:', a=ul)

    div1 = jp.Div(
        style='overflow:auto;height: 520px;padding:4%;padding-top:0%;margin-top: 0px;background-color: #DCDCDC;border-bottom-right-radius:.225rem;border-bottom-left-radius:.225rem',
        a=wp, classes='shadow-md m-2')

    div2 = jp.Div(style='margin-top:46px; position:absolute', a=div1)
    div_sort_buttons = jp.Div(style='padding-top: 19px;width: 1080px;height: 73px;position:absolute;background-color: #DCDCDC;')
    button_sort_title = jp.Button(a=div_sort_buttons, style='width: 27rem; border-radius: 2px;', classes='mr-2 mb-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4', text='Ordina per titolo', click=sort_by_title)
    button_sort_director = jp.Button(a=div_sort_buttons, style='width: 11rem; border-radius: 2px;', classes='w-32 mr-2 mb-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4', text='Ordina per regista', click=sort_by_director)

    movie_table = jp.Table(style='margin-top: 95px; color:black;width:59%')
    p_title = jp.P(a=div1, style='margin-top: 82px;color: black;font-size:20px', classes='hidden')
    p_director = jp.P(a=div1, style='color: black;font-size:20px', classes='hidden')
    p_date = jp.P(a=div1, style='color: black;font-size:20px', classes='hidden')
    p_gross = jp.P(a=div1, style='color: black;font-size:20px', classes='hidden')
    p_budget = jp.P(a=div1, style='color: black;font-size:20px', classes='hidden')
    p_rating = jp.P(a=div1, style='color: black;font-size:20px', classes='hidden')
    p_distributor = jp.P(a=div1, style='color: black;font-size:20px', classes='hidden')
    p_imdb_rating = jp.P(a=div1, style='color: black;font-size:20px', classes='hidden')
    p_time = jp.P(a=div1, style='color: black;font-size:20px', classes='hidden')
    body_table = jp.Tbody(style='overflow:auto;', a=movie_table)
    body_table_sorted = jp.Tbody(style='overflow:auto;')
    body_table_title_sorted = jp.Tbody(style='overflow:auto;')
    li2 = jp.Li(style='margin-left: 1%;text-decoration: none;float: left;color: black;font-size:20px', a=ul)
    li2.set_classes('hidden')
    tasto_indietro = jp.Button(a=li2,text='Clicca qui per tornare indietro', style='width: 263px;color:red;', click=remove_genre)
    tasto_indietro_lista_film = jp.Button(a=li2, text='Clicca qui per tornare alla lista',style='width: 265px;color:red;',classes='hidden', click=return_to_list)

    genres = ['Avventura','Azione','Commedia','Musical','Horror','Romantico','Thriller','Drammatico','Documentario','Altro']

    for i in genres:
        jp.Button(text=i, a=div2,click=view_genre,style=f'border-radius: .125rem;font-weight: 700;height: 12rem;margin: .5rem;margin-right: .5rem;margin-bottom: .5rem;padding-bottom: .5rem;padding-top: .5rem;padding-right: 1rem;padding-left: 1rem;color: #fff;width: 14rem;background-image: url("/static/images/{i}.jpg");')

    return wp

if __name__ == '__main__':
    jp.justpy(MovieDatabase.list_movies)
