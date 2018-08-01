import os


from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#################################################
#	IMPORTS FROM WITHIN DJANGOLABS APPLICATION  #

from Labs.models import LabTasks, Lab
from Labs.forms import DocumentUploadForm
from Labs.utils.djangolabsutils import handle_lab2_uploaded_file, handle_lab3_uploaded_file, handle_lab4_uploaded_file, handle_lab5_uploaded_file

#################################################

from django import template


register = template.Library()




class ListLabsView(generic.ListView):
	template_name = 'labs/labs.html'
	context_object_name = 'all_django_labs'
	paginate_by = 5

	def get_queryset(self):
		return Lab.objects.all()
	


class DetailLabView(generic.DetailView):
	model = Lab
	template_name = 'labs/detail.html'
	form_class = DocumentUploadForm
	labtasks_paginate_by = 5


	def post(self, request, *args, **kwargs):
		form = DocumentUploadForm(request.POST, request.FILES)
		if form.is_valid() and each_django_lab.lab_number == 1:
			#<process form cleaned data>
			output = handle_lab1_uploaded_file(request.FILES['document'], request.POST.get("username"))
			return HttpResponse('Out of 100% Your Lab score is: ' + str(output))
		elif form.is_valid() and each_django_lab.lab_number == 2:
			#<process form cleaned data>
			output = handle_lab2_uploaded_file(request.FILES['document'], request.POST.get("username"))
			return HttpResponse('Out of 100% Your Lab score is: ' + str(output))
		elif form.is_valid() and each_django_lab.lab_number == 3:
			#<process form cleaned data>
			output = handle_lab3_uploaded_file(request.FILES['document'], request.POST.get("username"))
			return HttpResponse('Out of 100% Your Lab score is: ' + str(output))
		elif form.is_valid() and each_django_lab.lab_number == 4:
			#<process form cleaned data>
			output = handle_lab4_uploaded_file(request.FILES['document'], request.POST.get("username"))
			return HttpResponse('Out of 100% Your Lab score is: ' + str(output))
		else:
			pass





	def get_context_data(self, **kwargs):
		list_labs_view_instance = ListLabsView()

        # Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
		# context['book_list'] = Book.objects.all()
		#Add document upload form to template
		context['form'] = DocumentUploadForm()
		#query labs
		context['labs_pk'] = list_labs_view_instance.get_queryset()
		#get total number of labs
		context['number_of_all_labs'] = list_labs_view_instance.get_queryset().count()

		#set pagination
		# paginator = Paginator(labs_list, 1)
		# page =  self.request.GET.get('page')
		# context['page'] = page
		# context['labs_list'] = Paginator(labs_list, 1)
		# paginate page here
		labs_list = list_labs_view_instance.get_queryset()
		paginator = Paginator(labs_list, 1)
		page = self.request.GET.get('page', 1)


		context['lab_tasks'] =  paginator.page(page)





		return context



   
