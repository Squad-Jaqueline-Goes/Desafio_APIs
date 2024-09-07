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
    url = f"https://rickandmortyapi.com/api/character/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    character = json.loads(data)

    # Obtendo informações de origem e localização
    origin_url = character.get("origin", {}).get("url")
    location_url = character.get("location", {}).get("url")

    origin = {}
    location = {}

    if origin_url:
        origin_response = urllib.request.urlopen(origin_url)
        origin_data = origin_response.read()
        origin = json.loads(origin_data)

    if location_url:
        location_response = urllib.request.urlopen(location_url)
        location_data = location_response.read()
        location = json.loads(location_data)

    # Obtendo episódios em que o personagem aparece
    episodes_info = []
    for episode_url in character.get("episode", []):
        episode_response = urllib.request.urlopen(episode_url)
        episode_data = episode_response.read()
        episode = json.loads(episode_data)
        episodes_info.append({
            "id": episode["id"],
            "name": episode["name"],
            "episode": episode["episode"],
            "air_date": episode["air_date"]
        })

    return render_template("profile.html", 
                           profile=character, 
                           origin=origin, 
                           location=location, 
                           episodes=episodes_info)



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
