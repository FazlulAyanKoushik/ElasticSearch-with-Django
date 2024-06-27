from django_elasticsearch_dsl import Document, Index, fields

from .models import Product

product_index = Index("product")  # Name of the Elasticsearch index
product_index.settings(  # Settings for the Elasticsearch index
    number_of_shards=1,  # The number of shards for the index
    number_of_replicas=0,  # The number of replicas for the index
)


@product_index.doc_type
class ProductDocument(Document):
    name = fields.TextField(attr="name", fields={"suggest": fields.Completion()})  # The name of the product

    class Django:
        model = Product
        fields = ["id", "price"]  # The fields of the Django model that you want to be indexed in Elasticsearch, in this case, the id and price fields, which are the primary key and price of the product


# Why do we need to index the id and price fields in Elasticsearch?
# To be able to search for products by their id and price in Elasticsearch using the search API


# What is the purpose of the suggest field in the name field?
# The suggest field is used to provide suggestions for product names based on user input, such as autocomplete suggestions in a search bar