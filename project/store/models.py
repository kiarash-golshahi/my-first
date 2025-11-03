from django.db import models

class Product(models.Model):
    """
    This model contains the basic attributes of a product which is in the online shop; that means:
        1. Title
        2. Price
        3. Details about the product; its identity and its properties
        4. Category
        5. Registration date
    The seller, as admin, has access to this model and can add or delete new products to the database.
    """
    title = models.CharField(max_length=500)
    price = models.IntegerField()
    details = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    # The attribute "category" stands for the objects of "Category" model table.
    # It means that each product comes from a category and a category can contain several products.
    # "on_delete" keyword specifies what will happen if the parent object (created category in "Category" model) is deleted.
    # "models.CASCADE" specifies that all of the products will be deleted from the database if their parent object (category) is deleted.
    registration_date = models.DateTimeField()

    def __str__(self):
        return f'{self.title}'

class Category(models.Model):
    """
    This model make the seller, as admin, able to create categories to sort the products.
    """
    title = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.title}'
