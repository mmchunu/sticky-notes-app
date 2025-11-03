# ====== Import modules ======
from django.urls import path
from . import views  # Import views from this app

# ====== Define URL patterns ======
urlpatterns = [
    path('', views.home, name='home'),                 # Home page: list all notes
    path('create/', views.create_note, name='create'), # Create a new note
    path('edit/<int:pk>/', views.edit_note, name='edit'),  # Edit a note by ID
    path('delete/<int:pk>/', views.delete_note, name='delete'),  # Delete a note by ID
]
