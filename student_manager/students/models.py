from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    code = models.CharField(max_length=20)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title



# class Booking(models.Model):
#     student = models.ForeignKey('Student', on_delete=models.CASCADE, null=True, blank=True)
#     book = models.ForeignKey('Book', on_delete=models.CASCADE)
#     date_borrowed = models.DateField()
#     return_date = models.DateField()

#     def __str__(self):
#         return f"{self.student} - {self.book}"
