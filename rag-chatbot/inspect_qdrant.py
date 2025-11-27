from qdrant_client import QdrantClient
print(dir(QdrantClient))
client = QdrantClient(":memory:")
print("search" in dir(client))
print("query_points" in dir(client))
