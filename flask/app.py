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
