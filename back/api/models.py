# encoding: utf-8

from django.db import models

# Create your models here.

class Dream(models.Model):

	STATUS = (
        ('novo', 'Novo'),
        ('inviavel', 'Inviavel'),
        ('pre_aprovado', 'Pré-Aprovado'),
    )

	name = models.CharField('Nome', max_length=255, default=None)
	age = models.CharField('Idade', max_length=255, default=None)
	email = models.CharField('E-mail', max_length=255, default=None)
	phone = models.CharField('Telefone', max_length=255, default=None)
	inmate = models.BooleanField('Internado', default=False)
	hospital_name = models.CharField('Nome do Hospital', max_length=255, default=None)
	hospital_contact = models.CharField('Contato do Hospital', max_length=255, default=None)  
	medical_approved = models.BooleanField('Aprovação Médica', default=False)
	parental_approved = models.CharField('Aprovação do Responsável', max_length=255, default=None)
	description = models.TextField('Descrição', default=None)
	hospital_address = models.CharField('Endereço do Hospital', max_length=255, default=None)
	observation = models.CharField('Observação', max_length=255, default=None)
	liason = models.TextField('Relacionamento com Paciente', default=None)
	status = models.CharField('Status', max_length=1, choices=STATUS)
	planning_description = models.TextField('Descrição do Planejamento', default=None)


