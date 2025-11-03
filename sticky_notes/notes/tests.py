# ====== IMPORTS ======

from django.test import TestCase
from django.urls import reverse
from .models import StickyNote

# ====== TESTING THE NOTE MODEL ======

class NoteModelTest(TestCase):
    def setUp(self):
        """
        SETUP METHOD RUNS BEFORE EACH TEST
        Create a sample note to test the model
        """
        self.note = StickyNote.objects.create(
            title="Test Note",        # SAMPLE TITLE
            content="This is a test note"  # SAMPLE CONTENT
        )

    def test_note_creation(self):
        """
        TEST THAT THE NOTE IS CREATED CORRECTLY
        """
        # CHECK THE NOTE TITLE
        self.assertEqual(self.note.title, "Test Note")
        # CHECK THE NOTE CONTENT
        self.assertEqual(self.note.content, "This is a test note")
        # CHECK THAT THE OBJECT IS AN INSTANCE OF Note
        self.assertTrue(isinstance(self.note, StickyNote))


# ====== TESTING CRUD VIEWS ======

class NoteViewsTest(TestCase):
    def setUp(self):
        """
        SETUP METHOD RUNS BEFORE EACH TEST
        Create a sample note for testing CRUD operations
        """
        self.note = StickyNote.objects.create(
            title="Sample",
            content="Sample content"
        )

    def test_home_view_status_code(self):
        """
        TEST THAT THE HOME PAGE LOADS SUCCESSFULLY
        """
        response = self.client.get(reverse('home'))  # GET REQUEST TO HOME
        self.assertEqual(response.status_code, 200)  # EXPECT STATUS 200

    def test_create_view(self):
        """
        TEST CREATING A NEW NOTE
        """
        response = self.client.post(
            reverse('create'),  # CREATE VIEW URL
            {'title': 'New Note', 'content': 'New content'}  # FORM DATA
        )
        self.assertEqual(response.status_code, 302)  # REDIRECT AFTER SUCCESS
        self.assertEqual(StickyNote.objects.last().title, 'New Note')  # CHECK DB

    def test_edit_view(self):
        """
        TEST EDITING AN EXISTING NOTE
        """
        response = self.client.post(
            reverse('edit', args=[self.note.id]),  # EDIT VIEW URL WITH NOTE ID
            {'title': 'Edited', 'content': 'Edited content'}  # UPDATED DATA
        )
        self.assertEqual(response.status_code, 302)  # REDIRECT AFTER SUCCESS
        self.note.refresh_from_db()  # REFRESH NOTE FROM DATABASE
        self.assertEqual(self.note.title, 'Edited')  # CHECK TITLE UPDATE

    def test_delete_view(self):
        """
        TEST DELETING A NOTE
        """
        response = self.client.post(
            reverse('delete', args=[self.note.id])  # DELETE VIEW URL WITH NOTE ID
        )
        self.assertEqual(response.status_code, 302)  # REDIRECT AFTER SUCCESS
        self.assertFalse(StickyNote.objects.filter(id=self.note.id).exists())  # NOTE REMOVED FROM DB
