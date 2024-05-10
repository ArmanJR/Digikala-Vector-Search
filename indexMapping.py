indexMapping = {
    "properties": {
        "id": {
            "type": "long"  # Assuming 'id' is a numeric identifier
        },
        "title_fa": {
            "type": "text",  # Persian text might require specific analyzers for better search functionality
            # "fields": {
            #     "keyword": {
            #         "type": "keyword",  # Adding a keyword field for aggregation or exact matches
            #         "ignore_above": 256
            #     }
            # }
        },
        "Rate": {
            "type": "float"  # Assuming 'Rate' is a numeric value with potential decimal places
        },
        "Rate_cnt": {
            "type": "long"  # Number of rates given
        },
        "Category1": {
            "type": "keyword"  # Suitable for filters or aggregations
        },
        "Category2": {
            "type": "keyword"
        },
        "Brand": {
            "type": "keyword"  # Brands typically require exact matching
        },
        "Price": {
            "type": "float"  # Assuming price could have decimals
        },
        "Seller": {
            "type": "keyword"  # Seller names are typically used for exact matches
        },
        "Is_Fake": {
            "type": "boolean"  # True or False values
        },
        "min_price_last_month": {
            "type": "float"  # Assuming it could have decimals
        },
        "sub_category": {
            "type": "keyword"  # Subcategories are generally used for exact matching or aggregations
        },
        "titleVector": {
            "type": "dense_vector",
            "dims": 1024,  # https://huggingface.co/intfloat/multilingual-e5-large
            "index": True,
            "similarity": "cosine"  # Choosing cosine similarity for vector field
        }
    }
}
