# encoding: utf-8

from django.db import models

# Create your models here.

class Dream(models.Model):

	STATUS = (
        ('novo', 'Novo'),
        ('inviavel', 'Inviavel'),
        ('pre_aprovado', 'Pré-Aprovado'),
    )

	CATEGORY = (
		('sonho_ir', 'Sonho Ir'),
        ('sonho_ir', 'Sonho Ir'),
        ('sonho_fazer', 'Sonho Fazer'),
        ('sonho_conhecer_rever', 'Sonho Conhecer / Rever'),
    )

	dreamer_name = models.CharField('Nome do Sonhador', max_length=255, default=None)
	dreamer_age = models.CharField('Idade do Sonhador', max_length=255, default=None)
	dreamer_address = models.CharField('Endereço do Sonhador', max_length=255, default=None)
	dreamer_health_conditions = models.TextField('Condições Médicas e Expectativa de Vida', default=None)
	
	contact_name = models.CharField('Nome do Contato', max_length=255, default=None)
	contact_email = models.CharField('E-mail do Contato', max_length=255, default=None)
	contact_phone = models.CharField('Telefone do Contato', max_length=255, default=None)
	contact_liason = models.CharField('Relacionamento com Sonhador (Ex. filho, cuidador)', max_length=255, default=None)
	
	inmate = models.BooleanField('Está Internado?', default=False)
	local = models.CharField('Local de Internação', max_length=255, default=None, null=True)
	local_address = models.CharField('Endereço do Local de Internação', max_length=255, default=None, null=True)
	local_name = models.CharField('Nome do Contato do Local de Internação', max_length=255, default=None, null=True)
	local_phone = models.CharField('Telefone do Contato do Local de Internação', max_length=255, default=None, null=True)
	
	medical_approved = models.BooleanField('Tem Aprovação Médica para a Realização do Sonho?', default=False)
	parental_approved = models.BooleanField('Tem Aprovação do Responsável para a Realização do Sonho?', default=False)
	
	description = models.TextField('Descrição Detalhada do Sonho', default=None)
	
	category = models.CharField('Categoria', max_length=20, choices=CATEGORY, default=None, null=True)
	status = models.CharField('Status', max_length=20, choices=STATUS, default='novo', null=True)
	planning_description = models.TextField('Planejamento do Sonho', default=None, null=True)

	class Meta:
		# verbose_name = 'Gestão de Sonhos'
		verbose_name_plural = 'Sonhos'


