from django.db import models


class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    stock = models.IntegerField('Quantity in Stock')

    def __str__(self) -> str:
        return self.name


class Client(models.Model):
    name = models.CharField('Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    email = models.EmailField('E- mail', max_length=120)

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'
