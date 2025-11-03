# ====== Import necessary modules ======
from django import forms
from .models import StickyNote  # Import the StickyNote model

# ====== Define the form for StickyNote ======
class StickyNoteForm(forms.ModelForm):
    """
    Form to create or edit a StickyNote.
    Uses Django's ModelForm to automatically generate fields
    based on the StickyNote model.
    """

    class Meta:
        model = StickyNote  # Link this form to the StickyNote model
        fields = ['title', 'content']  # Include only the title and content fields

        # Optional: Add custom widgets for styling
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter note title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter note content', 'rows': 4}),
        }

        # Optional: Add labels for the fields
        labels = {
            'title': 'Note Title',
            'content': 'Note Content',
        }
