# encoding: utf-8

from django.db import models

# Create your models here.

class Dream(models.Model):

	STATUS = (
        ('novo', 'Novo'),
        ('inviavel', 'Inviavel'),
        ('pre_aprovado', 'Pré-Aprovado'),
    )

	name = models.CharField('Nome do Paciente', max_length=255, default=None)
	age = models.CharField('Idade do Paciente', max_length=255, default=None)
	address = models.CharField('Endereço do Paciente', max_length=255, default=None, null=True)
	contact_name = models.CharField('Nome', max_length=255, default=None)
	email = models.CharField('E-mail', max_length=255, default=None)
	phone = models.CharField('Telefone', max_length=255, default=None)
	inmate = models.BooleanField('Internado', default=False)
	hospital_name = models.CharField('Nome do Hospital', max_length=255, default=None, null=True)
	hospital_contact = models.CharField('Contato do Hospital', max_length=255, default=None, null=True)
	health_conditions = models.TextField('Condições Médicas e Expectativa', default=None)  
	medical_approved = models.BooleanField('Aprovação Médica', default=False)
	parental_approved = models.BooleanField('Aprovação do Responsável', default=False)
	description = models.TextField('Descrição do Sonho', default=None)
	dream_report = models.TextField('Relato do Sonho', default=None)
	hospital_address = models.CharField('Endereço (onde paciente está)', max_length=255, default=None, null=True)
	observation = models.TextField('Observação', default=None)
	liason = models.CharField('Relacionamento com Paciente', max_length=255, default=None)
	status = models.CharField('Status', max_length=20, choices=STATUS)
	planning_description = models.TextField('Descrição do Planejamento', default=None)

	class Meta:
		# verbose_name = 'Gestão de Sonhos'
		verbose_name_plural = 'Sonhos'


