from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

# Rota para listar todos os personagens
@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("characters.html", characters=dict["results"])

# Rota para o perfil de um personagem
@app.route("/profile/<id>")
def get_profile(id):
    url = f"https://rickandmortyapi.com/api/character/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("profile.html", profile=dict)

# Rota para listar personagens (retornando JSON)
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

# Rota para listar episódios
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

# Rota para uma localização específica
@app.route("/location/<id>")
def get_location(id):
    url = f"https://rickandmortyapi.com/api/location/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("location.html", location=dict)

if __name__ == "__main__":
    app.run(debug=True)

