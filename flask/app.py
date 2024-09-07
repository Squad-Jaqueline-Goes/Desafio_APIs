from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)


@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])


@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("profile.html", profile=dict)


@app.route("/lista")
def get_list_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    for character in dict["results"]:
        character = {
            "name": character["name"],
            "status": character["status"],
        }
        characters.append(character)

    return {"characters": characters}


# rota para location
@app.route("/locations")
def get_locations():  # função para listar as localizações
    # var que recebera o valor da api
    url = "https://rickandmortyapi.com/api/location"

    # var que vai acessar a classe "urllib.request" para acessar a url
    response = urllib.request.urlopen(url)

    # var que fará a leitura dos resultados
    locations = response.read()

    # var para formatar os resultados no formato json
    dict = json.loads(locations)

    # dicionario de localizações
    locations = []

    for location in dict["results"]:
        location = {
            "id": location["id"],
            "name": location["name"],
            "type": location["type"],
            "dimension": location["dimension"],
        }
        locations.append(location)
        
        #retorno da renderização da pag html com a lista de localizações
        return render_template("locations.html", locations=locations)
        
@app.route("/episodes")
def get_list_episodes():
    url = "https://rickandmortyapi.com/api/episode/"
    response = urllib.request.urlopen(url)
    episodes = response.read()
    dict = json.loads(episodes)

    episodes = []

    for episode in dict["results"]:
        episode = {
            "id": episode["id"],
            "name": episode["name"],
            "air_date": episode["air_date"],
            "episode": episode["episode"],
        }
        episodes.append(episode)

    return render_template("episodes.html", episodes=episodes)
