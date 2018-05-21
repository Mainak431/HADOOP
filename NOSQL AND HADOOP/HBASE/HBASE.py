from starbase import Connection

c = Connection("127.0.0.1","8000")

ratings = c.table('ratings')

if (ratings.exists()):
    print("Dropping existing ratings table\n")
    ratings.drop()


ratings.create('rating')

print("Parsing the ml-100k ratings data... \n")

ratingFile = open("D://Mainak//Movie Ratings//ml-100k//ml-100k//u.data",'r')

batch = ratings.batch()

for line in ratingFile :
    (userID,movieID,rating,timestamp) = line.split()
    batch.update(userID,{'rating':{movieID:rating}})

ratingFile.close()

print("Committing ratings data to HBASE USING REST SERVICE")

batch.commit(finalize=True)
print("Get Back Ratings for some users")
print("Ratings for User ID 1:")
print(ratings.fetch("1"))
print("Ratings for user ID:33")
print(ratings.fetch("33"))