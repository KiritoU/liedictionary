from django.urls import path
from . import views

app_name = "dictionary"
urlpatterns = [
    path('', views.WordListView.as_view(), name='index'),
    path('word/<int:pk>/', views.WordDetailView.as_view(), name='word-detail'),
    path('word/<int:pk>/update', views.WordUpdateView.as_view(), name='word-update'),
    path('word/<int:pk>/delete', views.WordDeleteView.as_view(), name='word-delete'),
    path('word/new', views.WordCreateView.as_view(), name='word-create'),
]