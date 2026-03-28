import time

class SeperateChaining:
    def __init__(self, size=10007):
        # initialize hash table and counter to track collisions
        self.size = size
        self.table = [[] for _ in range(size)]
        self.collisions = 0
    def _hash(self, key):
        return key % self.size
    def insert(self, movie_id, rating):
        #get index for movie id
        index = self._hash(movie_id)
        #get bucket at that index
        bucket = self.table[index]

        # if bucket has entires, then it has collision, adding it to the counter
        if len(bucket) > 0:
            self.collisions += 1
        #add rating to total, and increase count of ratings
        for entry in bucket:
            if entry[0] == movie_id:
                entry[1][0] += rating
                entry[1][1] += 1
                return
        #if movie not found then add new entry
        bucket.append([movie_id, [rating, 1]])
    
    def lookup(self, movie_id):
        # find bucket and searh for movie id, then return the average
        index = self._hash(movie_id)
        for entry in self.table[index]:
            if entry[0] == movie_id:
                total, count = entry[1]
                return round(total / count, 2), count
        return None
    def load(self, records):
        # measure time taken to load all of the records
        start = time.time()
        for movie_id, rating in records:
            self.insert(movie_id, rating)
        return round(time.time() - start, 4)
