
# query = "imaginary characters from outer space at war"

# results = collection.aggregate([
#   {"$vectorSearch": {
#     "queryVector": generate_embedding(query),
#     "path": "plot_embedding_hf",
#     "numCandidates": 100,
#     "limit": 4,
#     "index": "PlotSemanticSearch",
#       }}
# ]);

# for document in results:
#     print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')