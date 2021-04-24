from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Name(models.Model):
	name = models.CharField(max_length = 50)
	profession = models.CharField(max_length = 50)
	profession1 = models.CharField(max_length = 50)
	profession2 = models.CharField(max_length = 50)

	def __str__(self):
		return self.name

class About(models.Model):
	aboutme = models.TextField(max_length = 150)
	profession = models.CharField(max_length = 50)
	about_profession = RichTextField(max_length = 150)
	birthday = models.CharField('Birthday', max_length=100, default='Aprel 19, 1996')
	website = models.CharField(max_length = 50)
	phone = models.CharField(max_length = 50)
	city = models.CharField(max_length = 50)
	age = models.CharField(max_length = 50)
	degrre = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 254)

	def __str__(self):
		return self.profession

class Resume(models.Model):
	description = RichTextField()

	def __str__(self):
		return self.description

class Summary(models.Model):
	name = models.CharField(max_length = 50)
	description = RichTextField()
	city = models.CharField(max_length = 50, default='Yangiariq')
	phone = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 54, default='sss@mail.ru')
	year = models.CharField(max_length = 254, default='2014-2019')

	def __str__(self):
		return self.name

class Education(models.Model):
	edu_name_degree = models.CharField(max_length = 50)
	about_edu = RichTextField(max_length = 254)
	year = models.CharField(max_length = 254, default='2014-2019')
	university_name = models.CharField(max_length = 254, default='TATU')

	def __str__(self):
		return self.edu_name_degree

class Skills(models.Model):
	title = models.CharField('Name', max_length=100)
	percentage = models.CharField('Percentage', max_length=50)
	about_skil = models.CharField(max_length=254, default='mahoratlarim haqida qisqacha')

	def __str__(self):
		return f"{self.title} has been added to skills"

	class Meta:
		verbose_name = 'Skill'
		verbose_name_plural = 'Skills'

class Experience(models.Model):
	name = models.CharField(max_length=254,default='Dizayner')
	year = models.CharField(max_length = 254, default='2014-2019')
	title = models.CharField(max_length = 254, default='IdealSoft MCHJ, Urganch')
	description = description = RichTextField()

	def __str__(self):
		return self.name
		

