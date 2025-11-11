from django.db import models

# Category is the parent model, so I wrote it first.
class Category(models.Model):
    """
    Categories to sort products in the store.
    """
    title = models.CharField(max_length=255, verbose_name='نام دسته')

    class Meta:
        ordering = ['title']
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    def __str__(self):
        return self.title

class Product(models.Model):
    """
    Products which will be sold in the store.
    """
    title = models.CharField(max_length=255, verbose_name='نام کالا')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت')
    # "DecimalField" works better than "IntegerField" in this case, because decimal numbers are more legal than integers in setting prices.
    # In this case, the price can only have 10 digits and 2 decimal places.
    details = models.TextField(verbose_name='جزئیات')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products', verbose_name='دسته‌بندی')
    # The attribute "category" stands for the objects of "Category" model table.
    # It means that each product comes from a category and a category can contain several products.
    # "on_delete" keyword specifies what will happen if the parent object (created category in "Category" model) is deleted.
    # "models.CASCADE" specifies that all of the products will be deleted from the database if their parent object (category) is deleted.
    # "related_name" makes each Category model object able to have access to its relative Product objects using "category.products.all()".
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    # "auto_now_add" saves the datetime when the new product is created in the admin panel and fills this property automatically.

    class Meta:
        ordering = ['title', 'registration_date']
        verbose_name = 'کالا'
        verbose_name_plural = 'کالاها'

    def __str__(self):
        return self.title
