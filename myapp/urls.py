from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('product/',views.product,name='product'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('seller_index/',views.seller_index,name='seller_index'),
    path('change_password/',views.change_password,name='change_password'),
    path('seller_add_product/',views.seller_add_product,name='seller_add_product'),
    path('seller_view_product/',views.seller_view_product,name='seller_view_product'),
    path('seller_edit_product/<int:pk>/',views.seller_edit_product,name='seller_edit_product'),
    path('seller_delete_product/<int:pk>/',views.seller_delete_product,name='seller_delete_product'),
    path('add_to_wishlist/<int:pk>/',views.add_to_wishlist,name='add_to_wishlist'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('product_details/<int:pk>/',views.product_details,name='product_details'),
    path('remove_from_wishlist/<int:pk>/',views.remove_from_wishlist,name='remove_from_wishlist'),
    path('cart/',views.cart,name='cart'),
    path('remove_from_cart/<int:pk>/',views.remove_from_cart,name='remove_from_cart'), 
    path('add_to_cart/<int:pk>/',views.add_to_cart,name='add_to_cart'), 
    path('change_qty/<int:pk>/',views.change_qty,name='change_qty'),
    path('pay/',views.initiate_payment,name='pay'),
    path('callback/',views.callback,name='callback'),
    path('myorder/',views.myorder,name='myorder'),
    path('discount/<int:pk>/',views.discount,name='discount'),


]
