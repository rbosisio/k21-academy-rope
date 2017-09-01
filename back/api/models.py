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
	dream_needs = models.TextField('Necessidades do Sonho', default=None, null=True)

	class Meta:
		# verbose_name = 'Gestão de Sonhos'
		verbose_name_plural = 'Sonhos'

class AvailableDaysTimes(models.Model):
	DAYS = (
        ('seg', 'Segunda'),
        ('ter', 'Terça'),
        ('qua', 'Quarta'),
        ('qui', 'Quinta'),
        ('sex', 'Sexta'),
        ('sab', 'Sábado'),
        ('dom', 'Domingo')
    )
	day = models.CharField('Dia da semana', max_length=20, choices=DAYS, default=None)

	TIMES = (
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite')
    )
	time = models.CharField('Horário do dia', max_length=20, choices=TIMES, default=None)

	def __str__(self):
		days = dict(self.DAYS)
		times = dict(self.TIMES)
		return days[self.day] + " - " + times[self.time]

class Volunteer(models.Model):
	name = models.CharField('Nome', max_length=255, default=None)
	nickname = models.CharField('Apelido', max_length=255, default=None)
	birthdate = models.DateField('Data de nascimento', default=None)
	telephone = models.CharField('Telefone', max_length=255, default=None)
	cellphone = models.CharField('Celular', max_length=255, default=None)
	email = models.CharField('Email', max_length=255, default=None)
	address = models.CharField('Endereço ', max_length=255, default=None)
	personal_characteristics = models.TextField('Características pessoais', default=None)
	talents = models.TextField('Talentos', default=None)

	available_days_times = models.ManyToManyField(AvailableDaysTimes)

	ASSIGNMENTS = (
        ('hunter', 'Hunter'),
        ('farm', 'Farm'),
        ('reg', 'REG')
    )
	assignment = models.CharField('Designação do voluntário ', max_length=20, choices=ASSIGNMENTS)

	STATUS = (
        ('novo', 'Novo'),
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado')
    )
	status = models.CharField('Designação do voluntário ', max_length=20, choices=STATUS, default=None)