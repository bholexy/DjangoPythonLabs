from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

'''
class LabComments(models.Model):
	comment = models.CharField(max_length=200)

	def __str__(self):
		return self.comment


class LabNotes(models.Model):
	note = models.CharField(max_length=200)


	def __str__(self):
		return self.note
'''

class Lab(models.Model):
	lab_title = models.CharField(max_length = 200)
	course_title = models.CharField(max_length = 200)
	lab_number = models.IntegerField()

    # created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # updated_at = models.DateTimeField(auto_now=True, editable=False)
    # title = models.CharField(max_length=255)
    # slug = models.SlugField(max_length=255,unique=True) 

	def __str__(self):
		return self.lab_title

	class Meta:
		ordering = ('course_title', 'lab_number')






class Grades(models.Model):
	grade = models.CharField(max_length = 20)

	def __str__(self):
		return self.grade

class GradesReport(models.Model):
	lab_id = models.ForeignKey(Lab, on_delete = models.CASCADE)
	grade_id = models.ForeignKey(Grades, on_delete = models.PROTECT)
	date = models.DateTimeField(default=timezone.now, null=False)
	user_id = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.user_id, self.lab_id, self.grade_id, self.date

class Document(models.Model):
	document = models.FileField(upload_to = 'uploads/')
	uploaded_at = models.DateTimeField(auto_now_add = True)

class MainModel(models.Model):
	title = models.CharField(max_length = 42)
	document = models.ForeignKey(Document, on_delete = models.CASCADE)


class LabTasks(models.Model):
	lab_id = models.ForeignKey(Lab, on_delete = models.CASCADE)
	task_number = models.IntegerField(null = True)
	comment = models.TextField()
	note = models.TextField(null = True, blank = True)
	task = models.TextField()
	hint = models.TextField(null = True, blank = True)


	def __str__(self):
		return self.task

	class Meta:
		ordering = ('lab_id', 'task_number')
