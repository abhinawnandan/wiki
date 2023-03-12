from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.entryPath, name="entryPath"),
    path("search/",views.search,name="search"),
    path("newPage/",views.new_Page,name="new_Page"),
    path("edit/",views.editPage,name="editPage"),
    path("edit_save/",views.edit_save,name="edit_save"),
    path("rand/", views.rand, name="rand"),
]
