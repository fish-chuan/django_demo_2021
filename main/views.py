from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book

def index(request):
    book = Book.objects.all()
    return render(request, 'index.html', {'book':book})

@login_required
def upload(request):
    if request.method == 'POST':
        isbn = request.POST['isbn']
        book_name = request.POST['book_name']
        author = request.POST['author']
        image = request.FILES['image']
        publish_date = request.POST['publish_date']

        user = User.objects.get(username=request.user.username)

        if Book.objects.filter(isbn=isbn).exists():
            messages.info(request, 'ISBN碼重複！')
            return redirect('upload')

        record = Book.objects.create(isbn=isbn, book_name=book_name, author=author,
        image=image, publish_date=publish_date, publisher=user)
        record.save()
        
        return redirect('/')
    else:
        return render(request, 'upload.html')


@login_required
def modify(request, number):
    if request.method == 'POST':
        target = Book.objects.get(isbn=number)

        target.isbn = request.POST['isbn']
        target.book_name = request.POST['book_name']
        target.author = request.POST['author']
        try:
            image = request.FILES['image']
        except:
            image = None
        if image:
            target.image = image
        target.publish_date = request.POST['publish_date']
        
        target.user = User.objects.get(username=request.user.username)
        
        if request.user.username == target.publisher.username:
            target.save()
        return redirect('/details/' + number)
    else:
        target = Book.objects.get(isbn=number)
        return render(request, 'modify/modify_details.html', {'target':target})


@login_required
def list_history(request):
    user = User.objects.get(username=request.user.username)
    upload_history = Book.objects.filter(publisher=user)
    return render(request, 'modify/list.html', {'upload_history':upload_history})


@login_required
def delete(request, number):
    user = User.objects.get(username=request.user.username)
    target = Book.objects.get(isbn=number)
    if user.username == target.publisher.username:
        target.delete()
        return redirect('upload_history')
    else:
        return redirect('/')



def book_details(request, number):
    try:
        book = Book.objects.get(isbn=number)
    except:
        book = None
    return render(request, 'details.html', {'book':book})
