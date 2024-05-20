from django.db import models

# Create your models here.
class Books(models.Model):
    Book_name = models.CharField(max_length=55)
    Book_Id = models.IntegerField()
    Book_Author = models.CharField(max_length=55)

    class Meta:
        db_table = 'bookslist'