import csv

def load_data(ratings_path="data/ratings.csv", movies_path="data/movies.csv"):
    # build movieID to title and genres mapping
    movies = {}
    with open(movies_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[int(row["movieId"])] = {
                "title": row["title"],
                "genres": row["genres"]
            }

    # build tuples list of movieID and rating
    records = []
    with open(ratings_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append((int(row["movieId"]), float(row["rating"])))

    return records, movies