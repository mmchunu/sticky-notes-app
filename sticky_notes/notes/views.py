# ====== Import necessary modules ======
from django.shortcuts import render, redirect, get_object_or_404
from .models import StickyNote          # Import the StickyNote model
from .forms import StickyNoteForm        # Import the form to handle note input

# ====== VIEW: Home Page (Read all notes) ======
def home(request):
    """
    Display all sticky notes on the home page.
    """
    notes = StickyNote.objects.all()  # Fetch all notes from the database
    return render(request, 'notes/home.html', {'notes': notes})  # Pass notes to template

# ====== VIEW: Create a New Note ======
def create_note(request):
    """
    Handle creation of a new sticky note.
    GET: Display empty form.
    POST: Save form data to the database.
    """
    if request.method == 'POST':  # Check if the form is submitted
        form = StickyNoteForm(request.POST)  # Bind POST data to the form
        if form.is_valid():  # Validate the form data
            form.save()      # Save the new note to the database
            return redirect('home')  # Redirect to home page after saving
    else:
        form = StickyNoteForm()  # Create an empty form for GET request
    return render(request, 'notes/create_note.html', {'form': form})

# ====== VIEW: Edit an Existing Note ======
def edit_note(request, pk):
    """
    Edit an existing sticky note.
    GET: Display form pre-filled with note data.
    POST: Update note with submitted data.
    """
    note = get_object_or_404(StickyNote, pk=pk)  # Fetch note by ID or return 404
    if request.method == 'POST':
        form = StickyNoteForm(request.POST, instance=note)  # Bind POST data to existing note
        if form.is_valid():
            form.save()  # Save updated note
            return redirect('home')  # Redirect to home page
    else:
        form = StickyNoteForm(instance=note)  # Pre-fill form with existing note data
    return render(request, 'notes/edit_note.html', {'form': form})

# ====== VIEW: Delete a Note ======
def delete_note(request, pk):
    """
    Delete a sticky note.
    GET: Display confirmation page.
    POST: Delete the note and redirect to home.
    """
    note = get_object_or_404(StickyNote, pk=pk)  # Fetch note or 404 if not found
    if request.method == 'POST':
        note.delete()  # Delete the note from the database
        return redirect('home')  # Redirect after deletion
    return render(request, 'notes/delete_note.html', {'note': note})  # Confirmation page
