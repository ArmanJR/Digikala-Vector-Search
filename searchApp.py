ELASTIC_ENDPOINT = ""
ELASTIC_USERNAME = "elastic"
ELASTIC_PASSWORD = ""
ELASTIC_INDEX = "dk_semantic_search"
SAMPLE_COUNT = 1000

import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

try:
    es = Elasticsearch(
        ELASTIC_ENDPOINT,
        basic_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD),
    )
except ConnectionError as e:
    print("Connection Error:", e)

if es.ping():
    print("Successfully connected to ElasticSearch")
else:
    print("(!) Can not connect to Elasticsearch")


def search(input_keyword):
    model = SentenceTransformer('intfloat/multilingual-e5-large')
    vector_of_input_keyword = model.encode(input_keyword)

    query = {
        "field": "titleVector",
        "query_vector": vector_of_input_keyword,
        "k": 10,
        "num_candidates": SAMPLE_COUNT
    }
    res = es.knn_search(index=ELASTIC_INDEX, knn=query, source=["title_fa", "Category1"])
    results = res["hits"]["hits"]

    return results


def main():
    st.title("Search DigiKala Semantic")

    # Input: User enters search query
    search_query = st.text_input("Enter your search query")

    # Button: User triggers the search
    if st.button("Search"):
        if search_query:
            # Perform the search and get results
            results = search(search_query)

            # Display search results
            st.subheader("Search Results")
            for result in results:
                with st.container():
                    if '_source' in result:
                        try:
                            st.header(f"{result['_source']['title_fa']}")
                        except Exception as e:
                            print(e)

                        try:
                            st.write(f"Category: {result['_source']['Category1']}")
                        except Exception as e:
                            print(e)
                        st.divider()


if __name__ == "__main__":
    main()
