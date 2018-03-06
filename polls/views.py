from django.shortcuts import Http404, render

# Create your views here.

# from django.http import HttpResponse
from django.template import loader

from .models import Contato



def index (request) :

	contacts = Contato.objects.all()

	return render(request, 'polls/contacts.html', {'contacts': contacts, })

def detail (request, contact_id ) :

	try:
		contact = Contato.objects.get(pk=contact_id)
	except Contato.DoesNotExist:
		raise Http404("Question does not exist")

	contacts = Contato.objects.filter(id=contact_id)

	return render(request, 'polls/details.html', {'contacts': contacts })

def search (request) :

	query = request.GET.get('s', '')

	contact = Contato.objects.filter(name_contact__icontains=query.upper())

	if len(contact) <= 0:
		return render(request, 'polls/404.html', {'contacts': query })

	return render(request, 'polls/contacts.html', {'contacts': contact })