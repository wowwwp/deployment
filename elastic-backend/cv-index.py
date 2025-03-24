from elasticsearch import Elasticsearch, helpers
import pandas as pd

client = Elasticsearch("http://54.79.54.184:9200/")

# Create an index if it doesnt exist
if not client.indices.exists(index="cv-transcriptions"):
    client.indices.create(index="cv-transcriptions")

# Read the csv file
df = pd.read_csv('./cv-valid-dev.csv')
df.fillna("", inplace=True)

# Convert the dataframe to a dictionary
data = [
    {"_index": "cv-transcriptions",
     "_type": "doc",
        "_id": record["filename"], "_source": record}
    for record in df.to_dict(orient="records")
]

# Insert the data into the index
helpers.bulk(client, data, index="cv-transcriptions")
