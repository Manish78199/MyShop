from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path("cart/",views.cart,name="Cart"),
path("signin/",views.signin,name="signin"),
path("signup/",views.signup,name="signup"),
path("logout/",views.Logout,name="Logout"),
path("cartdetails",views.cartdetails,name="cartdetails"),
path("credential/<str:method>",views.loginmethod,name="loginmethod"),
path("checkout/",views.checkout,name="checkout"),
path("status/",views.status,name="status"),
path("contact/",views.contact,name="contact"),
path("veiw/<int:pid>/",views.veiw,name="veiw"),
path("find/",views.find1,name="find1"),
path("find/<str:cat>/",views.find2,name="find2"),
path("find/<str:cat>/<str:pname>/",views.find3,name="find3"),
path("order/",views.OrderNow,name="OrderNow"),
path("Test",views.Test,name="Test"),
path("search/<str:findi>",views.search,name="search")
]