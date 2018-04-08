from django import forms
from guestbook.models import Guestbook


class GuestbookForm(forms.ModelForm):

    class Meta:
        model = Guestbook
        fields = "__all__"
        # exclude = []
    user = forms.CharField(label="Пользователь", max_length=20)
    content = forms.CharField(widget=forms.Textarea, label="Содержание")
    honeypot = forms.CharField(required=False, label="Ловушка для спамеров")
