from django import forms

from goods.models import Good


class GoodForm(forms.ModelForm):
    fields = "__all__"

    class Meta:
        model = Good
        fields = "__all__"
