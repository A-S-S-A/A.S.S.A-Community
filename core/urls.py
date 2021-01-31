from django.urls import path
from users import views as user_views

app_name = "core"

urlpatterns = [
    path("", user_views.UserView.as_view(), name="home"),
]
