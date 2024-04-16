from django.urls import path
from .views import ticket_view, show_view, update_view, delete_view

urlpatterns = [
    path("", ticket_view, name="ticket_urls"),
    path("show/", show_view, name="show_urls"),
    path("update/<int:pk>", update_view, name="update_urls"),
    path("delete/<int:pk>", delete_view, name="delete_urls")
]
