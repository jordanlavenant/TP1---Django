import datetime
from django.db import models

class Status(models.Model):
  numero = models.AutoField(primary_key=True)
  libelle = models.CharField(max_length=100)

  def __str__(self):
    return "{0} [{1}]".format(self.libelle, self.numero)

class Product(models.Model):
  name = models.CharField(max_length=100)
  code = models.IntegerField()
  price = models.IntegerField(null=True)
  date = models.DateField(default=datetime.date.today)
  status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)

  def __str__(self):
    return "{0} [{1}]".format(self.name, self.code)

class ProductItem(models.Model):
  code = models.IntegerField()
  color = models.CharField(max_length=100)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)

  def __str__(self):
    return "{0} {1} [{2}]".format(self.product.name, self.color, self.product.code)