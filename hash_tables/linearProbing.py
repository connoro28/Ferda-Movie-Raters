import time

class LinearProbing:
    def __init__(self, size=10007):
        #initialize hash table and collision counter
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.collisions = 0

    def _hash(self, key):
        #hash function to compute the index for a key
        return key % self.size

    def insert(self, movie_id, rating):
        index = self._hash(movie_id)

        # linear probing keeps searching for an empty slot or the same movieID to update
        while self.keys[index] is not None:
            if self.keys[index] == movie_id:
                self.values[index][0] += rating
                self.values[index][1] += 1
                return
            self.collisions += 1
            index = (index + 1) % self.size

        # if slot empty then insert new movieId and its rating
        self.keys[index] = movie_id
        self.values[index] = [rating, 1]

    def lookup(self, movie_id):
        # search for movieId with linear probing, then return average rating
        index = self._hash(movie_id)
        while self.keys[index] is not None:
            if self.keys[index] == movie_id:
                total, count = self.values[index]
                return round(total / count, 2), count
            index = (index + 1) % self.size

        return None

    def load(self, records):
        # insers all records and measures time
        start = time.time()
        for movie_id, rating in records:
            self.insert(movie_id, rating)
        return round(time.time() - start, 4)
