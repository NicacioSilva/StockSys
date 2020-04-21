from django.db import models


# This class produces a product class that can be inherited as
# any type of product.
class Product(models.Model):
    # Those will represents the type, price, status and issues of the products.
    name = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Ready to Purchase'),
        ('SOLD', 'Item Sold'),
        ('RESTOCKING', 'Under Restocking')
    )

    status = models.CharField(max_length=10, choices=choices, default='SOLD')
    issues = models.CharField(max_length=100, default='No Issues')

    def __str__(self):
        # This method will provide string output of your class.
        return 'Name: {0} Price: {1}'.format(self.name, self.price)

    # It tells to Django ignore Product class on the generations of the database,
    # because it's just a generic class.
    class Meta:
        abstract = True


class Laptop(Product):
    pass


class Desktop(Product):
    pass


class Mobile(Product):
    pass
