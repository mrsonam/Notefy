from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    note_password = forms.CharField(required=False, widget=forms.PasswordInput())
    class Meta:
        model = Note
        fields = ('note_title','note_content', 'note_images', 'note_audios', 'note_videos','note_password' )

class note_access(forms.Form):
    note_password = forms.CharField(widget=forms.PasswordInput())