from django.db import models

# Product model : Class that inherits from models.Model
class Provider(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15)
    website=models.URLField(null=True,blank=True)
    class Meta:
        db_table='providers'

class Product(models.Model):
    #define a string Field (equivalent to varchar(100) in SQL)
    label=models.CharField(max_length=100,unique=True)
    #define a decimal field (equivalent to Number(10,2) in SQL Oracle)
    price=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    #define a text field (to input a multi-line text)
    description=models.TextField()
    #define a date field
    #the auto_now_add=True will automatically set the date to the current date when the object is created
    #equivant in SQL oracle :  manifacturing_date DATE DEFAULT SYSDATE
    manifacturingDate=models.DateField(auto_now_add=True)
    expirationDate=models.DateField()
    #define an image field
    #upload_to is the directory where the image will be stored
    #null=True means that the field can be empty
    #blank=True means that the field is not required
    #this Field need the library Pillow, to be installed with the command : pip install pillow
    photo=models.ImageField(upload_to='images/products',null=True,blank=True)
    #relationship between Product and provider (1-n)
    provider=models.ForeignKey(Provider,on_delete=models.SET_NULL,null=True,blank=True)
    class Meta:
        db_table='products'
    
class Address(models.Model):
    houne_number=models.CharField(max_length=10)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=10)
    class Meta:
        db_table='addresses'
    
class Client(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    birth_date=models.DateField()
    email=models.EmailField(primary_key=True)
    phone_number=models.CharField(max_length=15)
    photo=models.ImageField(upload_to='images/clients',null=True,blank=True)
    #define the relationship between Client and Address (1-1)
    address=models.OneToOneField(Address,on_delete=models.CASCADE)
    #define the relationship between Product and Client (n-n) through the model Command
    client_products=models.ManyToManyField(Product,through='Command',through_fields=('client','product'))
    class Meta:
        db_table='clients'

class Command(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    quantity=models.PositiveSmallIntegerField(default=1)
    
    class Meta:
        db_table='commands'
        ordering=['-date'] #descending order of date
        #ordering=['date']
        unique_together=['product','client']


    
