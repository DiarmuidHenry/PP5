from django.contrib import admin
from .models import Product, Category, Rating, UserProfile

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'average_rating')  
    search_fields = ('name', 'category__name') 
    list_filter = ('category', 'price')  
    # Read only, cannot be changed by superuser
    readonly_fields = ('average_rating',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent') 
    search_fields = ('name',) 

class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating') 
    search_fields = ('user__email', 'product__name') 
    list_filter = ('rating',)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone_number')
    search_fields = ('user__email', 'address', 'phone_number')

# Register the models with their custom admin views
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
