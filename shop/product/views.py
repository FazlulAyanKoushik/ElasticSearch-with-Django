from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
from product.models import Product
from product.serializers import ProductSerializer, ProductDocumentSerializer
from product.documents import ProductDocument

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDocumentViewSet(APIView):
    def get(self, request, *args, **kwargs):
        search_query = request.query_params.get('search', None)  # Get the search query from the request query parameters
        if search_query:  # If the search query is not None
            s = ProductDocument.search().query("match", name=search_query)  # Search for products with names that match the search query
            if s.count() == 0:
                print("No results found for the search query")
                s = ProductDocument.search().query(
                    "multi_match",
                    query=search_query,
                    fields=['name', 'price']
                )
        else:
            s = ProductDocument.search()  # Get all products if no search query is provided
        # Here s.execute() is used to execute the search query and get the search results from Elasticsearch
        response = s.execute()
        # Here the search results are serialized using the ProductDocumentSerializer
        # response.hits is a list of the search results
        serializer = ProductDocumentSerializer(response.hits, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
