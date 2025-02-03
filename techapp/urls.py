from django.urls import path
from techapp import views


urlpatterns = [
    path('',views.index,name='index'),
    path('shop/',views.shop,name='shop'),
    path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
    path('user/',views.user,name='user'),
    path('cart/',views.cart,name='cart'),
    path('register/',views.register,name='register'),
    path('checkout/',views.checkout,name='checkout'),
    path('address/',views.address,name='address'),
    path('orders/',views.order_history,name='order_history'),
    path('user_login/', views.user_login, name='user_login'),  # Login view
    path('watch/',views.watch,name='watch'),
    path('headphone/',views.headphone,name='headphone'),
    path('speaker/',views.speaker,name='speaker'),
    path('joystick/',views.joystick,name='joystick'),
    path('contact_view/', views.contact_view, name='contact_view'),
    path('contactlist/', views.contactlist, name='contactlist'),
    # path('my_account/', views.my_account, name='my_account'),
    path('thing/<int:product_id>/',views.product_detail,name='product_detail'),
 

    path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/',views.remove_from_cart,name='remove_from_cart'),
    path('update_cart/<int:cart_item_id>/',views.update_cart,name='update_cart'),
    # path('order_summary/', views.order_summary, name='order_summary'),
    path('order_summary/<int:order_id>/',views.order_summary,name='order_summary'),
    # path('order_history/',views.order_history,name='order_history'),
    path('payment/<int:order_id>/', views.razorpay_payment, name='razorpay_payment'),   
    path("login/google/", views.google_login, name="google_login"),
    path('logout/', views.logout_view, name='logout'),


]