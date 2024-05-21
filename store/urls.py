from django.urls import path
from .views import ProductList, CategoryList, ProductDetail, login_registration, user_login, user_logout, register, \
    save_review, save_favorite_product, FavouriteProductsView, save_email, send_mail_to_customer, cart, to_cart, \
    checkout, successPayment, create_checkout_sessions, clear_cart

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('category/<slug:slug>/', CategoryList.as_view(), name="category_detail"),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    path('login_registration/', login_registration, name='login_registration'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('save_review/<int:product_id>/', save_review, name='save_review'),
    path('add-favorite/<slug:product_slug>/', save_favorite_product, name='add_favourite'),
    path('favourite/', FavouriteProductsView.as_view(), name='favourite'),
    path('save_email/', save_email, name='save_email'),
    path('send_email/', send_mail_to_customer, name='send_email'),
    path('cart/', cart, name='cart'),
    path('to_cart/<int:product_id>/<str:action>/', to_cart, name='to_cart'),
    path('checkout/', checkout, name='checkout'),
    path('payment/', create_checkout_sessions, name='payment'),
    path('payment_success/', successPayment, name='success'),
    path('clear_cart/', clear_cart, name='clear_cart'),
]
