from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings



# 1
class Brand(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

# 2
class Category(models.Model):

    ai = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='Category/%Y/%m/%d')



    def __str__(self):
        return f'{self.ai} '

    def get_sub(self):
        return Subcategory.objects.filter(category=self)

# 3
class Color(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

# 4
class Favorites(models.Model):
    ai = models.ForeignKey('Category', on_delete=models.CASCADE,)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.ForeignKey('Products', on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)



    def get_absolute_url(self):
        return reverse('favorites', kwargs={"ai":self.ai, "name":self.name})

# 5
class Gender(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 6
#class Lastids(models.Model):

    #def __str__(self):
        #return self.name

#7
class Messages(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('UserAlem', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text

# 8
class Orders(models.Model):
    ai = models.ForeignKey('Category', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.ForeignKey('Products', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    size = models.ForeignKey('Size', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('orders', kwargs={"ai":self.ai, "name":self.name})

# 9
class Products(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='Products/%Y/%m/%d', blank=True)
    photo1 = models.ImageField(upload_to='Photo1/%Y/%m/%d', blank=True)
    photo2 = models.ImageField(upload_to='Photo2/%Y/%m/%d', blank=True)
    photo3 = models.ImageField(upload_to='Photo3/%Y/%m/%d', blank=True)
    price = models.FloatField()
    brand = models.ForeignKey('Brand', related_name='products', on_delete=models.CASCADE, null=True, )
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE, null=True)
    color = models.ForeignKey('Color', on_delete=models.CASCADE, null=True)
    gender = models.ForeignKey('Gender', on_delete=models.CASCADE, null=True)
    size = models.ForeignKey('Size', on_delete=models.CASCADE, null=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE, null=True)
    update = models.ForeignKey('Update', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('infoProducts', kwargs={"pk":self.pk})

# 10
class Size(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#11
class Status(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

# 12
class Subcategory(models.Model):
    category = models.ForeignKey('Category',on_delete=models.CASCADE, related_name='category')
    name = models.CharField(max_length=150,)

    def __str__(self):
        return self.name




# 13
class Update(models.Model):
    update = models.BooleanField(default=True)



# 14
class UserAlem(AbstractUser):
   phone = models.IntegerField(null=True)




    #def __str__(self):
       # return self.name






