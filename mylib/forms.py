from django.forms import ModelForm
from django import forms

from .models import Book, Author, PublishingPress

"""class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['author_name']

class PublishingPressForm(forms.Form):
    publishing_press = forms.CharField(max_length=30)"""

class BookForm(forms.Form):
    book_title = forms.CharField(max_length=200)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
    book_edition = forms.IntegerField()
    book_theme = forms.CharField(max_length=30)
    publishing_year = forms.IntegerField()
    publishing_presses = forms.ModelChoiceField(queryset=PublishingPress.objects.all(), widget=forms.TextInput())

"""class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'"""

"""        def __init__(self, *args, **kwargs):
            super(BookForm, self).__init__(*args, **kwargs)
            if self.instance.pk:
                self.initial['authors'] = self.instance.authors.value_list('pk', flat=True)

        def save(self, *args, **kwargs):
            instance = super(BookForm, self).save(*args, **kwargs)
            if instance.pk:
                for author in instance.authors.all():
                    if author not in self.cleaned_data['authors']:
                        instance.authors.remove(author)
                for author in self.cleaned_data['authors']:
                    if author not in instance.authors.all():
                        instance.authors.add(author)
            return instance"""
