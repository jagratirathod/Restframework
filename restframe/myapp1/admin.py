from django.contrib import admin
from myapp1.models import Category,Restaurants,Food,Order,Wishlist,Orderline,ProductReview

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','cat_name','image']
admin.site.register(Category,CategoryAdmin)

class RestaurantAdmin(admin.ModelAdmin):
    list_display=['id','restorant_name','address']
admin.site.register(Restaurants,RestaurantAdmin)

class Foodadmin(admin.ModelAdmin):
    list_display=['id','name','description','price','image','category','restaurants']
admin.site.register(Food,Foodadmin)

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','user','totalprice','order_date','status','order_id']
admin.site.register(Order,OrderAdmin)

class WishlistAdmin(admin.ModelAdmin):
    list_display=['id','user','food']
admin.site.register(Wishlist,WishlistAdmin)

class OrderlineAdmin(admin.ModelAdmin):
    list_display=['id','totalquantity','food','order']
admin.site.register(Orderline,OrderlineAdmin)

class ReviewsAdmin(admin.ModelAdmin):
     list_display=['id','user','foodId','comment','rating']
admin.site.register(ProductReview,ReviewsAdmin)