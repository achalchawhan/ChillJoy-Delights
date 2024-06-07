# from django.db import models

# # Create your models here.
# class contactus(models.Model):
#     name=models.CharField(max_length=122)
#     email=models.CharField(max_length=122)
#     phone=models.CharField(max_length=12)
#     desc=models.TimeField()
#     date= models.DateField()
    
#     def __str__(self) -> str:
#         return self.name

# # from django.db import models


# # class Contactus(models.Model):
# #     name = models.CharField(max_length=100)
# #     email = models.EmailField()
# #     phone = models.CharField(max_length=15)
# #     desc = models.TextField()
# #     date = models.DateTimeField(auto_now_add=True)  # Add this line

# #     def __str__(self):
# #         return self.name

    
    
# # class order(models.Model):
# #     name=models.CharField(max_length=122)
# #     email=models.CharField(max_length=122)
# #     phone=models.CharField(max_length=122)
    
# #     OPTIONS = [
# #         ('Icecream', 'Option 1'),
# #         ('Cones', 'Option 2'),
# #         ('Familypack', 'Option 3'),
# #     ]
# #     option = models.CharField(
# #         max_length=20,
# #         option=OPTIONS,
# #         default='option1',
# #     )
# #     option=models.CharField(max_length=122)
# #     quantity=models.CharField()
# #     desc=models.TimeField()
# #     address=models.CharField(max_length=122)
# #     date= models.DateField()

# class Order(models.Model):
#     name = models.CharField(max_length=122)
#     email = models.CharField(max_length=122)
#     phone = models.CharField(max_length=122)
    
#     OPTIONS = [
#         ('Icecream', 'Option 1'),
#         ('Cones', 'Option 2'),
#         ('Familypack', 'Option 3'),
#     ]
#     option = models.CharField(
#         max_length=20,
#         choices=OPTIONS,  # Use 'choices' instead of 'option'
#         default='Icecream',  # Set a default value from your OPTIONS
#     )

#     quantity = models.CharField(max_length=122)  # Specify the data type (e.g., IntegerField) based on your requirements
#     desc = models.CharField(max_length=255)  # Use CharField for a description, adjust max_length as needed
#     address = models.CharField(max_length=122)
#     date = models.DateField()
    
    
    
    
    
# from django.db import models

# class Contactus(models.Model):
#     name = models.CharField(max_length=122)
#     email = models.CharField(max_length=122)
#     phone = models.CharField(max_length=12)  # Adjust max_length as needed
#     desc = models.TextField()
#     date = models.DateField()

#     def __str__(self):
#         return self.name



from django.db import models

class Contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)  # Adjust max_length as needed
    
    OPTIONS = [
        ('Icecream', 'Option 1'),
        ('Cones', 'Option 2'),
        ('Familypack', 'Option 3'),
    ]
    option = models.CharField(
        max_length=20,
        choices=OPTIONS,
        default='Icecream',
    )

    quantity = models.CharField(max_length=122)  # Specify the data type (e.g., IntegerField) based on your requirements
    desc = models.TextField()  # Use TextField for a description, adjust as needed
    address = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name
