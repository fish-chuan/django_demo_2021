from django import forms
from .models import Book

class Form_book(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'publish_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'update_time': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control', 'readonly':'true'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'})
        }

        labels = {
            'isbn': 'ISBN',
            'book_name': '書名',
            'author': '作者',
            'publish_date': '出版日期',
            'update_time': '更新日期',
            'publisher': '發表人',
            'image': '封面'
        }
        
