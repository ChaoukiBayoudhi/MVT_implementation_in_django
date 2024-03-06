from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField(null=True,blank=True)



# Product model : Class that inherits from models.Model
class Product(models.Model):
    #define a string Field (equivalent to varchar(100) in SQL)
    label = models.CharField(max_length=100)
    #define a decimal field (equivalent to Number(10,2) in SQL Oracle)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #define a text field (to input a multi-line text)
    description = models.TextField()
    #define a date field
    #the auto_now_add=True will automatically set the date to the current date when the object is created
    #equivant in SQL oracle :  manifacturing_date DATE DEFAULT SYSDATE
    manifacturing_date = models.DateField(auto_now_add=True)
    #define an image field
    #upload_to is the directory where the image will be stored
    #null=True means that the field can be empty
    #blank=True means that the field is not required
    #this Field need the library Pillow, to be installed with the command : pip install pillow
    photo = models.ImageField(upload_to='images/products/', null=True, blank=True)

class Address(models.Model):
    home_number = models.PositiveSmallIntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    #the email field is the primary key of the Client table
    email = models.EmailField(primary_key=True)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField()

