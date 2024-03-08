from django.db import models

class Product(models.Model):
    label=models.CharField(max_length=100,unique=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    description=models.TextField()
    manifacturingDate=models.DateField(auto_now_add=True)
    expirationDate=models.DateField()
    photo=models.ImageField(upload_to='images/products',null=True,blank=True)
    #relationship between Product and provider (1-n)
    provider=models.ForeignKey('Provider',on_delete=models.SET_NULL,null=True,blank=True)

class Provider(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15)
    website=models.URLField(null=True,blank=True)

class Client(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    birth_date=models.DateField()
    email=models.EmailField(primary_key=True)
    phone_number=models.CharField(max_length=15)
    photo=models.ImageField(upload_to='images/clients',null=True,blank=True)
    #define the relationship between Client and Address (1-1)
    address=models.OneToOneField('Address',on_delete=models.SET_NULL, null=True,blank=True)
    command=models.ManyToManyField('Product',through='Command',through_fields=('client','product'))

class Address(models.Model):
    houne_number=models.CharField(max_length=10)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=10)

class Command(models.Model):
    product=models.ForeignKey('Product',on_delete=models.CASCADE)
    client=models.ForeignKey('Client',on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    date=models.DateTimeField(auto_now_add=True)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
