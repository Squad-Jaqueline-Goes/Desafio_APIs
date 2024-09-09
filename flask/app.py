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

@app.route("/desenvolvedoras/")
def profile_dev():
    return render_template("desenvolvedoras.html")


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
def get_locations():
    # URL da API
    url = "https://rickandmortyapi.com/api/location"

    # Requisição para a URL
    response = urllib.request.urlopen(url)
    locations = response.read()

    # Converte os resultados para o formato JSON
    data = json.loads(locations)

    # Lista de localizações
    locations = []

    for location in data["results"]:
        location_info = {
            "id": location["id"],
            "name": location["name"],
            "type": location["type"],
            "dimension": location["dimension"],
        }
        locations.append(location_info)

    # Renderiza o template com a lista de localizações
    return render_template("locations.html", locations=locations)

# Rota para uma localização específica
@app.route("/location/<id>")
def get_location(id):
    url = f"https://rickandmortyapi.com/api/location/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("location.html", location=dict)

@app.route("/location/<id>")
def get_location(id):
    url = f"https://rickandmortyapi.com/api/location/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    location_data = json.loads(data)

    # Adiciona a lista de residentes à localização
    residents = location_data.get("residents", [])

    return render_template("location.html", location=location_data, residents=residents)



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

@app.route("/episode/<id>")
def get_episode(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)
    episode_data = response.read()
    episode_dict = json.loads(episode_data)

    character_urls = episode_dict.get("characters", [])
    characters_info = []
    for char_url in character_urls:
        char_id = char_url.split('/')[-1]
        char_url_full = "https://rickandmortyapi.com/api/character/" + char_id
        char_response = urllib.request.urlopen(char_url_full)
        char_data = char_response.read()
        char_dict = json.loads(char_data)
        characters_info.append({
            "id": char_id,
            "name": char_dict.get("name"),
            "image": char_dict.get("image"),
            "profile_url": f'/profile/{char_id}'
        })

    return render_template("episode.html", episode=episode_dict, characters=characters_info)


if __name__ == '__main__':
    app.run(debug=True)