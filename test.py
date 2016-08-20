from pymongo import MongoClient

client = MongoClient() # will connect on the default host and port.

db = client.test_database
# collection = db.dataset # A collection is a group of documents stored in MongoDB, and can be thought
# of as roughly the equivalent of a table in a relational database. Getting a collection in PyMongo works
# the same as getting a database:

post = {"author": "hello","text": "My first blog post!"}
posts = db.posts
posts.insert_one(post)
# print(posts.find_one()) # This method returns a single document matching a query (or None if there are no matches).

for post in posts.find(): # find() returns a Cursor instance,
                            # which allows us to iterate over all matching documents.
                            # For example, we can iterate over every document in the posts collection:
    print(post)


