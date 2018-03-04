from django.shortcuts import Http404, render

# Create your views here.

# from django.http import HttpResponse
from django.template import loader

from .models import Contato



def index (request) :

	contacts = Contato.objects.all()

	context = {
		'contacts': contacts,
	}

	return render(request, 'polls/index.html', context)

def detail (request, contact_id ) :

	try:
		contact = Contato.objects.get(pk=contact_id)
	except Contato.DoesNotExist:
		raise Http404("Question does not exist")


	contacts = Contato.objects.filter(id=contact_id)

	return render(request, 'polls/details.html', {'contacts': contacts })