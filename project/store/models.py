from django.db import models

# Category is the parent model, so I wrote it first.
class Category(models.Model):
    """
    Categories to sort products in the store.
    """
    title = models.CharField(max_length=255)

class Product(models.Model):
    """
    Products which will be sold in the store.
    """
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # "DecimalField" works better than "IntegerField" in this case, because decimal numbers are more legal than integers in setting prices.
    # In this case, the price can only have 10 digits and 2 decimal places.
    details = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    # The attribute "category" stands for the objects of "Category" model table.
    # It means that each product comes from a category and a category can contain several products.
    # "on_delete" keyword specifies what will happen if the parent object (created category in "Category" model) is deleted.
    # "models.CASCADE" specifies that all of the products will be deleted from the database if their parent object (category) is deleted.
    # "related_name" makes each Category model object able to have access to its relative Product objects using "category.products.all()".
    registration_date = models.DateTimeField(auto_now_add=True)
    # "auto_now_add" saves the datetime when the new product is created in the admin panel and fills this property automatically.
