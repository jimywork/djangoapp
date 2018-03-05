from django.db import models

from django.utils import timezone

class Contato(models.Model):
    
    Amigos = 'AM'
    Familia = 'FA'
    Trabalho = 'TR'

    CONTATO_GROUPS = (
        (Amigos, 'Amigos'),
        (Familia, 'Família'),
        (Trabalho, 'Trabalho'),
    )

    contatos_groups = models.CharField(
        max_length=2,
        choices=CONTATO_GROUPS,
        default=Amigos,
    )

    name_contact = models.CharField(max_length=32, blank=True, help_text='Nome Completo', default='')
    phone_contact = models.CharField(max_length=32, blank=True, help_text='Telefone', default='')
    email_contact = models.EmailField(max_length=32, blank=True, help_text='Endereço de E-mail', default='')
    address_contact = models.CharField(max_length=150, blank=True, help_text='Endereço', default='')
    org_contact = models.CharField(max_length=150, blank=True, help_text='Organização', default='')
    text_contact = models.TextField(max_length=255, blank=True, help_text='Observação', default='')
    date_contact = models.DateTimeField(default=timezone.now)

    def was(self, filter) :
    	print("Was ... %s\n%s" % (filter, self.name_contact))

    def __str__(self) :
    	return self.name_contact