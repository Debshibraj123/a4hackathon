from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Book
from .forms import BookForm


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'form': form})



def student_update(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'form': form, 'student': student})



def student_delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})






def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_create.html', {'form': form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_update.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_delete.html', {'book': book})


def student_page(request):
    students = Student.objects.all()
    books = Book.objects.all()
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        book_ids = request.POST.getlist('books')
        student = Student.objects.get(id=student_id)
        student.book_set.set(book_ids)
        return redirect('student_page')
    return render(request, 'student_page.html', {'students': students, 'books': books})


def book_page(request):
    students = Student.objects.all()
    books = Book.objects.all()
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        student_ids = request.POST.getlist('students')
        book = Book.objects.get(id=book_id)
        book.student_id = None if not student_ids else student_ids[0]
        book.save()
        return redirect('book_page')
    return render(request, 'book_page.html', {'students': students, 'books': books})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('student_list')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('student_list')
            except:
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


def start_view(request):
    return render(request, 'index.html')