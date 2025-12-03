from qdrant_client import QdrantClient
client = QdrantClient(":memory:")
help(client.query_points)
