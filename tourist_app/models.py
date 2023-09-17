from django.db import models

# Create your models here.

class login(models.Model):
    name = models.CharField(max_length=30,null=True) 
    password = models.CharField(max_length=30,null=True)  

class reg(models.Model):
    name = models.CharField(max_length=30,null=True) 
    file = models.FileField(upload_to='image/',null=True)
    email = models.EmailField(max_length=30,null=True)
    phonenumber = models.IntegerField(null=True)
    username = models.CharField(max_length=30,null=True) 
    password = models.CharField(max_length=30,null=True)  
    confirmpassword = models.CharField(max_length=30,null=True)

class londonfield(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.DateField(null=True)
    gender = models.CharField(max_length=10,null=True)
    name1 = models.CharField(max_length=100,null=True)
    age1 = models.DateField(null=True)
    gender1 = models.CharField(max_length=10,null=True)
    date2 = models.DateField(null=True)

    def calculate_age(self, reference_date):
        return reference_date.year - self.age.year - ((reference_date.month, reference_date.day) < (self.age.month, self.age.day))
    def calculate_age1(self, reference_date):
        return reference_date.year - self.age1.year - ((reference_date.month, reference_date.day) < (self.age1.month, self.age1.day))
    
class chinafield(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.DateField(null=True)
    gender = models.CharField(max_length=10,null=True)
    name1 = models.CharField(max_length=100,null=True)
    age1 = models.DateField(null=True)
    gender1 = models.CharField(max_length=10,null=True)
    date2 = models.DateField(null=True)

    def calculate_age(self, reference_date):
        return reference_date.year - self.age.year - ((reference_date.month, reference_date.day) < (self.age.month, self.age.day))
    def calculate_age1(self, reference_date):
        return reference_date.year - self.age1.year - ((reference_date.month, reference_date.day) < (self.age1.month, self.age1.day))

class singaporefield(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.DateField(null=True)
    gender = models.CharField(max_length=10,null=True)
    name1 = models.CharField(max_length=100,null=True)
    age1 = models.DateField(null=True)
    gender1 = models.CharField(max_length=10,null=True)
    date2 = models.DateField(null=True)

    def calculate_age(self, reference_date):
        return reference_date.year - self.age.year - ((reference_date.month, reference_date.day) < (self.age.month, self.age.day))
    def calculate_age1(self, reference_date):
        return reference_date.year - self.age1.year - ((reference_date.month, reference_date.day) < (self.age1.month, self.age1.day))
    
class japanfield(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.DateField(null=True)
    gender = models.CharField(max_length=10,null=True)
    name1 = models.CharField(max_length=100,null=True)
    age1 = models.DateField(null=True)
    gender1 = models.CharField(max_length=10,null=True)
    date2 = models.DateField(null=True)

    def calculate_age(self, reference_date):
        return reference_date.year - self.age.year - ((reference_date.month, reference_date.day) < (self.age.month, self.age.day))
    def calculate_age1(self, reference_date):
        return reference_date.year - self.age1.year - ((reference_date.month, reference_date.day) < (self.age1.month, self.age1.day))

class thailandfield(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.DateField(null=True)
    gender = models.CharField(max_length=10,null=True)
    name1 = models.CharField(max_length=100,null=True)
    age1 = models.DateField(null=True)
    gender1 = models.CharField(max_length=10,null=True)
    date2 = models.DateField(null=True) 

    def calculate_age(self, reference_date):
        return reference_date.year - self.age.year - ((reference_date.month, reference_date.day) < (self.age.month, self.age.day))
    def calculate_age1(self, reference_date):
        return reference_date.year - self.age1.year - ((reference_date.month, reference_date.day) < (self.age1.month, self.age1.day))

class indonesiafield(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.DateField(null=True)
    gender = models.CharField(max_length=10,null=True)
    name1 = models.CharField(max_length=100,null=True)
    age1 = models.DateField(null=True)
    gender1 = models.CharField(max_length=10,null=True)
    date2 = models.DateField(null=True)

    def calculate_age(self, reference_date):
        return reference_date.year - self.age.year - ((reference_date.month, reference_date.day) < (self.age.month, self.age.day))
    def calculate_age1(self, reference_date):
        return reference_date.year - self.age1.year - ((reference_date.month, reference_date.day) < (self.age1.month, self.age1.day))

class malaysiafield(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.DateField(null=True)
    gender = models.CharField(max_length=10,null=True)
    name1 = models.CharField(max_length=100,null=True)
    age1 = models.DateField(null=True)
    gender1 = models.CharField(max_length=10,null=True)
    date2 = models.DateField(null=True)

    def calculate_age(self, reference_date):
        return reference_date.year - self.age.year - ((reference_date.month, reference_date.day) < (self.age.month, self.age.day))
    def calculate_age1(self, reference_date):
        return reference_date.year - self.age1.year - ((reference_date.month, reference_date.day) < (self.age1.month, self.age1.day))

class contactfield(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length=30,null=True)
    subject = models.CharField(max_length=50,null=True)
    message = models.CharField(max_length=150,null=True)

class bookingfield(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length=30,null=True)
    date = models.DateField(null=True)
    destination = models.CharField(max_length=30,null=True,choices=(
        ('Shimla','Shimla'),
        ('Kovalam','Kovalam'),
        ('Leh Ladakh','Leh Ladakh'),
        ('Andaman','Andaman'),
        ('Sikkim','Sikkim'),
    )
    )
    special = models.CharField(max_length=150,null=True)

    # payment
class payment(models.Model):
    paymentMethod = models.CharField(max_length=30,null=True)
    name = models.CharField(max_length=30,null=True)
    cardnumber = models.CharField(max_length=16,null=True)
    expiration = models.CharField(max_length=20,null=True)
    cvv = models.CharField(max_length=3,null=True)
    
class payment_one(models.Model):
    paymentMethod = models.CharField(max_length=30,null=True)
    name = models.CharField(max_length=30,null=True)
    cardnumber = models.CharField(max_length=16,null=True)
    expiration = models.CharField(max_length=20,null=True)
    cvv = models.CharField(max_length=3,null=True)
    
class payment_two(models.Model):
    paymentMethod = models.CharField(max_length=30,null=True)
    name = models.CharField(max_length=30,null=True)
    cardnumber = models.CharField(max_length=16,null=True)
    expiration = models.CharField(max_length=20,null=True)
    cvv = models.CharField(max_length=3,null=True)
    
class payment_three(models.Model):
    paymentMethod = models.CharField(max_length=30,null=True)
    name = models.CharField(max_length=30,null=True)
    cardnumber = models.CharField(max_length=16,null=True)
    expiration = models.CharField(max_length=20,null=True)
    cvv = models.CharField(max_length=3,null=True)
    
class payment_four(models.Model):
    paymentMethod = models.CharField(max_length=30,null=True)
    name = models.CharField(max_length=30,null=True)
    cardnumber = models.CharField(max_length=16,null=True)
    expiration = models.CharField(max_length=20,null=True)
    cvv = models.CharField(max_length=3,null=True)
    
class payment_five(models.Model):
    paymentMethod = models.CharField(max_length=30,null=True)
    name = models.CharField(max_length=30,null=True)
    cardnumber = models.CharField(max_length=16,null=True)
    expiration = models.CharField(max_length=20,null=True)
    cvv = models.CharField(max_length=3,null=True)
    
class payment_six(models.Model):
    paymentMethod = models.CharField(max_length=30,null=True)
    name = models.CharField(max_length=30,null=True)
    cardnumber = models.CharField(max_length=16,null=True)
    expiration = models.CharField(max_length=20,null=True)
    cvv = models.CharField(max_length=3,null=True)
    
class payment_seven(models.Model):
    paymentMethod = models.CharField(max_length=30,null=True)
    name = models.CharField(max_length=30,null=True)
    cardnumber = models.CharField(max_length=16,null=True)
    expiration = models.CharField(max_length=20,null=True)
    cvv = models.CharField(max_length=3,null=True)
    
