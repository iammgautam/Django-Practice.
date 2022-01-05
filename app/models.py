from django.db import models
from django.db.models.enums import Choices

# Create your models here.
class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=100)
    stuemail = models.EmailField(max_length=100)
    stupass = models.CharField(max_length=100)

    def __str__(self):
        return self.stuname

    # def get_absolute_url(self):
    #     return reverse("student_detail", kwargs={"pk": self.pk})