from import_export import resources
from .models import Category, Products


class CategoryResource(resources.ModelResources):
    class Meta:
        model = Category


class ProductsResource(resources.ModelResources):
    class Meta:
        model = Products
