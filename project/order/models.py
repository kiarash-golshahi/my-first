from django.conf import settings # To import AUTH_USER_MODEL
from django.db import models

class Order(models.Model):
    orderer_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 'settings.AUTH_USER_MODEL' points to the default Django user model, which is 'django.contrib.auth.User' in this project. We also can customize this model later.
    ordered_product = models.ForeignKey('store.Product', on_delete=models.PROTECT)
    address = models.TextField()
    phone = models.CharField(max_length=11)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-registration_date']
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش‌ها'
    
    def __str__(self):
        return f'سفارش {self.orderer_user} برای {self.ordered_product}'
