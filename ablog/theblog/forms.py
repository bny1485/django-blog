from django import forms
from .models import Post, Category


# categories = [('test1', 'test1'), ("test2", "test2")]
choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=choice_list, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'author', 'body', 'snippet')
        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', }),
            'author': forms.Select(attrs={'class': 'form-control', }),
            'body': forms.Textarea(attrs={'class': 'form-control', }),
            'snippet': forms.Textarea(attrs={'class': 'form-control', }),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body')
        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'author': forms.Select(attrs={'class': 'form-control', }),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control', }),
            'body': forms.Textarea(attrs={'class': 'form-control', }),
        }
