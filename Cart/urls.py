from django.urls import path
from django.urls import include
from .views import add_product
from .views import delete_product
from .views import set_quantity
from .views import decrease_quantity
from .views import get_cart
from .views import GetFullCartPage

app_name = 'Cart'
urlpatterns = [
	path('add/', add_product, name = "add_product_to_cart"),
	path('decrease/', decrease_quantity, name="decrease_quantity"),
	path('delete/', delete_product, name = "delete_product_from_cart"),
	path('setquantity/', set_quantity, name="change_product_quantity_in_cart"),
	path('getcart/', get_cart, name="show_cart"),
	path('checkcartandorder/', GetFullCartPage, name="get_fullCartPage"),
	path('createorder/', include('Order.urls', namespace = "Order")),
]
