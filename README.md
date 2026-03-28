# Movie Rating linear probing and seperate chaining lookup comparison
A web app that compares two hash table collision strategies seperate chaining and linear probing using the MovieLens movie rating dataset.

# Team
-Connor Opdyke
-Ronin Mithaug
-George Tabor

# Project Overview
Large systems must efficiently insert and search movie rating data. When many keys are inserted into a hash table, collisions can occur which affect the performance. This project compared two different hash table collision techniques to determine which performs better when storing and retrieving data.

# Features
- Loads all movies into a hash table
- Search for a move by ID, and name
- Random movie lookup
- view average rating and total ratings for specific movie
- compare the insertion time, lookup time, and collisions of both methods

# Dataset
MovieLens Small Dataset
- 100,836 rathing across 9,742 movies and 610 users
- https://grouplens.org/datasets/movielens/

# Tech
- Python
- Flask
- HTML CSS JavaScript

# Data Strucutres Used
- Seperate Chaining Hash Table (each bucket holds a list of entries, collisions handled by appending to the chain)
- Linear Probing Hash Table (collisions handled by walking forward to the next spot)

# How to run
1. Clone Repository
2. Instal dependecies
    -pip install flask
3. Download MovieLens small dataset https://grouplens.org/datasets/movielens/ then put files in data/ folder
4. Run the app
    - python app.py

