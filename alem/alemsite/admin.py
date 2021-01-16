from django.contrib import admin
from .models import Brand, Color, Gender, Products, Size, Category, Status, Subcategory, Update, UserAlem, Messages, Orders, Favorites
from .forms import messageForm


# 1
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Brand, BrandAdmin)

# 2
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'ai', 'name')



admin.site.register(Category, CategoryAdmin)

# 3
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Color, ColorAdmin)

#4
# class FavoritesAdmin(admin.ModelAdmin):

#5
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Gender, GenderAdmin)

#8
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'ai','color','completed', 'date', 'user', 'quantity', 'size')

admin.site.register(Orders, OrderAdmin)


#9
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','category', 'subcategory', 'brand' )


admin.site.register(Products, ProductsAdmin)

#10
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory')


admin.site.register(Size, SizeAdmin)


#11
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Status, StatusAdmin)


#12
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')



admin.site.register(Subcategory, SubcategoryAdmin)


#13
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('update',)


admin.site.register(Update, UpdateAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email', 'phone','is_staff')


admin.site.register(UserAlem, UserAdmin)


class MessageAdmin(admin.ModelAdmin):
    form = messageForm
    list_display = ( 'user','text', 'date')
    ordering = ['date']


admin.site.register(Messages, MessageAdmin)

class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('ai','name','color','size','user','date')











admin.site.register(Favorites, FavoritesAdmin)
