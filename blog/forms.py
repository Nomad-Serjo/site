from django import forms

from blog.models import Blog


class BlogForm(forms.ModelForm):
    fields = "__all__"

    class Meta:
        model = Blog
        fields = "__all__"
