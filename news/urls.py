from django.urls import path
from .views import HomePageView, AddNewView, MyNewsView, NewDetailView, NewUpdateView, NewDeleteView, SearchView, CategoryView, TagsView
app_name = "news"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('add-new/', AddNewView.as_view(), name="add_new"),
    path('my-new/', MyNewsView.as_view(), name="my_new"),
    path('new-detail/<int:pk>/', NewDetailView.as_view(), name="new_detail"),
    path('new-update/<int:pk>/', NewUpdateView.as_view(), name="new_update"),
    path('new-delete/<int:pk>/', NewDeleteView.as_view(), name="new_delete"),
    path('search/', SearchView.as_view(), name='search'  ),
    path('category/<int:pk>', CategoryView.as_view(), name='category'  ),
    path('tags/<int:pk>', TagsView.as_view(), name='tags'  ),
    
]
