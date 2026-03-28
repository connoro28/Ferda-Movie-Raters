from flask import Flask, render_template, request, jsonify
from dataLoader import load_data
import sys
import time
import random
sys.path.append('hash_tables')
from seperateChaining import SeperateChaining
from linearProbing import LinearProbing


app = Flask(__name__)

# loads the data and builds the hash tables for both when it runs
print("loading data and building hash tables")
records, movies = load_data()
sc = SeperateChaining()
lp = LinearProbing()
sc_insert_time = sc.load(records)
lp_insert_time = lp.load(records)
print("Finished loading. Tables ready.")

# build a mapping from title to movie ID for searching by name
title_to_id = {info["title"].lower(): mid for mid, info in movies.items()}

# get the min and max movie IDs for display in the UI
min_id = min(movies.keys())
max_id = max(movies.keys())

@app.route("/")
def index():
    return render_template("index.html", min_id=min_id, max_id=max_id)

@app.route("/search", methods=["POST"])
def search():
    # gets the movie id from the request
    data = request.json
    movie_id = int(data.get("movie_id"))

    # checks if the movie id is in the dictionary
    if movie_id not in movies:
        return jsonify({"error": "Movie ID not found"}), 404

    movie = movies[movie_id]

    # time the lookup for separate chaining
    start = time.time()
    sc_result = sc.lookup(movie_id)
    sc_lookup_time = round(time.time() - start, 6)

    # time the lookup for linear probing
    start = time.time()
    lp_result = lp.lookup(movie_id)
    lp_lookup_time = round(time.time() - start, 6)

    return jsonify({
        "title": movie["title"],
        "genres": movie["genres"].replace("|", ", "),
        "avg_rating": sc_result[0],
        "total_ratings": sc_result[1],
        "sc_insert_time": sc_insert_time,
        "lp_insert_time": lp_insert_time,
        "sc_lookup_time": sc_lookup_time,
        "lp_lookup_time": lp_lookup_time,
        "sc_collisions": sc.collisions,
        "lp_collisions": lp.collisions,
    })

@app.route("/search_by_name", methods=["POST"])
def search_by_name():
    data = request.json
    name = data.get("name", "").lower().strip()

    # match id to title
    if name in title_to_id:
        return jsonify({"movie_id": title_to_id[name]})
    for title, mid in title_to_id.items():
        if name in title:
            return jsonify({"movie_id": mid})

    return jsonify({"error": "Movie not found"}), 404

@app.route("/random", methods=["GET"])
def random_movie():
    movie_id = random.choice(list(movies.keys()))
    return jsonify({"movie_id": movie_id})

if __name__ == "__main__":
    app.run(debug=True)