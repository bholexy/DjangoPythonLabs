from django.forms import ModelForm
from Labs.models import Document

class DocumentUploadForm(ModelForm):
	
	class Meta:
		model = Document
		fields = ['document',]