from flask import Flask, send_file
import os
import random


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

app = Flask(
    __name__,
    static_folder=os.path.join(PROJECT_DIR, "Estética"),
    static_url_path="/estetica"
)


jogos=["Your turn to die","Danganronpa","Teatro dos Finais Infelizes", "Enigma do Medo","Final Fantasy","Illusion Carnival" , "No Case Should Remain Unsolved","Saihate Station"]
musics={"Tribunal do Desespero": "https://www.youtube.com/watch?v=BkSNXEmuGlk", "Numb": "https://www.youtube.com/watch?v=8qJcbeO3Ajs", "I wanna be your slave": "https://www.youtube.com/watch?v=M6ZZKNPrSPw", "Bohemian Rhapsody": "https://www.youtube.com/watch?v=5zLnaNY58j8", "RuLe":"https://www.youtube.com/watch?v=0Z_YqhYHhpg"}
tribunal_do_desespero= f'<a href="{musics["Tribunal do Desespero"]}" target="_blank">Tribunal do Desespero </a>'
numb= f'<a href="{musics["Numb"]}" target="_blank">Numb </a>'
i_wanna_be_your_slave= f'<a href="{musics["I wanna be your slave"]}" target="_blank">I wanna be your slave </a>'
bohemian_rhapsody= f'<a href="{musics["Bohemian Rhapsody"]}" target="_blank">Bohemian Rhapsody </a>'
ruLe= f'<a href="{musics["RuLe"]}" target="_blank">RuLe </a>'
    
@app.route('/')
def inicio():
    caminho = os.path.join(os.path.dirname(__file__), 'index.html')
    return send_file(caminho) 
    


@app.route('/game')
def game():
    jogo = random.choice(jogos)
    return f'''
    <link rel="stylesheet" href="/estetica/style.css">
    <h4><a href="http://127.0.0.1:5000/">Voltar</a></h4>
    <h1>Jogos: {jogo}</h1>
    '''


@app.route("/listmusicas")
def music():
    musics_list = [tribunal_do_desespero, numb, i_wanna_be_your_slave, bohemian_rhapsody, ruLe ]
    musica = random.choice(musics_list)

    

    return f'''
    <link rel="stylesheet" href="/estetica/style.css">
    <h4><a href="http://127.0.0.1:5000/">Voltar</a></h4>
    <h1>Musicas: {musica}</h1>
    '''

@app.route("/randomfact")
def random_fact():
    return f'''
    <link rel="stylesheet" href="/estetica/style.css">
    <h4><a href="https://www.buzzfeed.com/dannicaramirez/weird-facts-fs" >Clique aqui para ver fatos aleatórios</a></h4>
    '''

app.run(debug=True)