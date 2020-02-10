from django.test import TestCase
from .models import Note
from django.contrib.auth.models import User


# Create your tests here.
class TestModels(TestCase):

    def setUp(self):
        user1 = User.objects.create_user(
            first_name="Sonam",
            last_name="Sherpa",
            username="mrsonam",
            email="sonam@gmail.com",
            password="sonam123"
        )

        note1 = Note.objects.create(
            note_title="First Note",
            note_content="Hello, this is my first note",
            user_id=user1
        )
        note2 = Note.objects.create(
            note_title="Second Note",
            note_content="Hello, this is my second note",
            user_id=user1
        )
        note3 = Note.objects.create(
            note_title="My Note",
            note_content="Hello, this is my third note",
            user_id=user1
        )
        note4 = Note.objects.create(
            note_title="My Note",
            note_content="Hello, this is my note",
            user_id=user1
        )

    def test_count_note(self):
        user = User.objects.get(first_name="Sonam")
        note = Note.objects.filter(user_id=user)
        value = note.count()
        self.assertEquals(value, 4)
