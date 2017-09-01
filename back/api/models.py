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
	status = models.CharField('Status', max_length=20, choices=STATUS, default='novo')
	planning_description = models.TextField('Descrição do Planejamento', default=None)

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