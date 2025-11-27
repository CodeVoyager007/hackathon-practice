from qdrant_client import QdrantClient
from qdrant_client.http import models

client = QdrantClient(":memory:")
client.create_collection(
    collection_name="test",
    vectors_config=models.VectorParams(size=4, distance=models.Distance.COSINE)
)

client.upsert(
    collection_name="test",
    points=[
        models.PointStruct(
            id=1,
            vector=[0.1, 0.1, 0.1, 0.1],
            payload={"text": "hello"}
        )
    ]
)

results = client.query_points(
    collection_name="test",
    query=[0.1, 0.1, 0.1, 0.1],
    limit=1
)

print(results)
print(results.points[0].payload)
