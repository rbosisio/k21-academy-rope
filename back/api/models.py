# encoding: utf-8

from django.db import models

# Create your models here.

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

	order = models.IntegerField('Ordem na lista', default=0)

	def __str__(self):
		days = dict(self.DAYS)
		times = dict(self.TIMES)
		return days[self.day] + " - " + times[self.time]

	class Meta:
		ordering = ('order',)
		verbose_name_plural = 'Dias / Horários Disponíveis'
		

class Volunteer(models.Model):
	name = models.CharField('Nome', max_length=255, default=None, null=True, blank=True)
	nickname = models.CharField('Apelido', max_length=255, default=None, null=True, blank=True)
	birthdate = models.DateField('Data de nascimento', default=None, null=True, blank=True)
	telephone = models.CharField('Telefone', max_length=255, default=None, null=True, blank=True)
	cellphone = models.CharField('Celular', max_length=255, default=None, null=True, blank=True)
	email = models.CharField('Email', max_length=255, default=None, null=True, blank=True)
	address = models.CharField('Endereço ', max_length=255, default=None, null=True, blank=True)
	personal_characteristics = models.TextField('Características pessoais', default=None, null=True, blank=True)
	talents = models.TextField('Talentos', default=None, null=True, blank=True)

	available_days_times = models.ManyToManyField(AvailableDaysTimes, blank=True)

	# ====================================================== Administrative fields ====================================================== #

	ASSIGNMENTS = (
        ('hunter', 'Hunter'),
        ('farm', 'Farm'),
        ('reg', 'REG')
    )
	assignment = models.CharField('Designação do voluntário ', max_length=20, choices=ASSIGNMENTS, default='hunter', null=True, blank=True)

	STATUS = (
        ('novo', 'Novo'),
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado')
    )

	status = models.CharField('Status ', max_length=20, choices=STATUS, default='novo', null=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Voluntários'

# ================================================================================================================================= #

class Partner(models.Model):
	name = models.CharField('Nome', max_length=255, default=None, null=True, blank=True)

	DOCUMENT_TYPE = (
        ('pf', 'Pessoa Física'),
        ('pj', 'Pessoa Jurídica'),
    )
	document_type = models.CharField('Opção de pessoa', max_length=20, choices=DOCUMENT_TYPE, default='pf')
	
	contact_name = models.CharField('Nome do contato', max_length=255, default=None, null=True, blank=True)
	document = models.CharField('Documento', max_length=255, default=None, null=True, blank=True)
	telephone = models.CharField('Telefone', max_length=255, default=None, null=True, blank=True)
	cellphone = models.CharField('Celular', max_length=255, default=None, null=True, blank=True)
	address = models.CharField('Endereço ', max_length=255, default=None, null=True, blank=True)

	has_specific_dream = models.BooleanField('Tem sonho específico?', default=False)
	money_help = models.BooleanField('Ajuda com dinheiro?', default=False)
	service_help = models.BooleanField('Ajuda com serviço?', default=False)

	help_description = models.TextField('Descrição da ajuda', default=None, null=True, blank=True)

	observation = models.TextField('Observações (Especificar doação)', default=None, null=True, blank=True)

	STATUS = (
        ('novo', 'Novo'),
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado')
    )
	status = models.CharField('Designação do voluntário ', max_length=20, choices=STATUS, default='novo', null=True, blank=True)
	
	available_days_times = models.ManyToManyField(AvailableDaysTimes, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Parceiros'

# ================================================================================================================================= #

class Dream(models.Model):

	STATUS = (
        ('novo', 'Novo'),
        ('inviavel', 'Inviavel'),
        ('aprovado', 'Aprovado'),
        ('realizado', 'Realizado')
    )

	CATEGORY = (
        ('sonho_ir', 'Sonho Ir'),
        ('sonho_fazer', 'Sonho Fazer'),
        ('sonho_conhecer_rever', 'Sonho Conhecer / Rever'),
    )

	dreamer_name = models.CharField('Nome do Sonhador', max_length=255, default=None, null=True, blank=True)
	dreamer_age = models.CharField('Idade do Sonhador', max_length=255, default=None, null=True, blank=True)
	dreamer_address = models.CharField('Endereço do Sonhador', max_length=255, default=None, null=True, blank=True)
	dreamer_health_conditions = models.TextField('Condições Médicas e Expectativa de Vida', default=None, null=True, blank=True)
	
	contact_name = models.CharField('Nome do Contato', max_length=255, default=None, null=True, blank=True)
	contact_email = models.CharField('E-mail do Contato', max_length=255, default=None, null=True, blank=True)
	contact_phone = models.CharField('Telefone do Contato', max_length=255, default=None, null=True, blank=True)
	contact_liason = models.CharField('Relacionamento com Sonhador (Ex. filho, cuidador)', max_length=255, default=None, null=True, blank=True)
	
	inmate = models.BooleanField('Está Internado?', default=False)
	local = models.CharField('Local de Internação', max_length=255, default=None, null=True, blank=True)
	local_address = models.CharField('Endereço do Local de Internação', max_length=255, default=None, null=True, blank=True)
	local_name = models.CharField('Nome do Contato do Local de Internação', max_length=255, default=None, null=True, blank=True)
	local_phone = models.CharField('Telefone do Contato do Local de Internação', max_length=255, default=None, null=True, blank=True)
	
	medical_approved = models.BooleanField('Tem Aprovação Médica para a Realização do Sonho?', default=False)
	parental_approved = models.BooleanField('Tem Aprovação do Responsável para a Realização do Sonho?', default=False)
	
	description = models.TextField('Descrição Detalhada do Sonho', default=None, null=True, blank=True)
	
	# ====================================================== Administrative fields ====================================================== #

	dreamer_nickname = models.CharField('Apelido do sonhador', max_length=255, default=None, null=True, blank=True)

	significative_days = models.CharField('Data importante pro sonho, caso exista', max_length=255, default=None, null=True, blank=True)
	impediment_days = models.TextField('Dias no qual o sonho não pode ser realizado (Dias de tratamento, etc)', default=None, null=True, blank=True)
	mental_health = models.CharField('Condição mental do sonhador', max_length=255, default=None, null=True, blank=True)

	uses_health_device = models.BooleanField('Sonhador usa algum dispositivo?', default=False)
	health_device_description = models.TextField('Descreva o dispositivo', default=None, null=True, blank=True)

	MOBILITY = (
        ('caminha_sozinho', 'Caminha sozinho'),
        ('caminha_auxiliado', 'Caminha com auxilio'),
        ('cadeira_rodas', 'Cadeira de rodas'),
        ('acamado', 'acamado'),
    )
	mobility = models.CharField('Como é a mobilidade do sonhador?', max_length=255, choices=MOBILITY, default='caminha_sozinho', null=True, blank=True)

	doctor_name = models.CharField('Médico responsável', max_length=255, default=None, null=True, blank=True)
	doctor_contact = models.CharField('Contato do médico', max_length=255, default=None, null=True, blank=True)

	how_did_know_us = models.TextField('Como soube do trabalho da Rope', default=None, null=True, blank=True)
	
	linked_partners = models.ManyToManyField(Partner, blank=True, related_name="Parceiros conectados +")
	linked_volunteers = models.ManyToManyField(Volunteer, blank=True, related_name="Voluntários conectados +")
	linked_transport = models.TextField('Transporte', default=None, null=True, blank=True)
	linked_food = models.TextField('Alimentação', default=None, null=True, blank=True)

	special_care = models.TextField('Cuidados especiais (banheiro, alimentação e locomoção)', default=None, null=True, blank=True)

	spendings = models.TextField('Valores gastos', default=None, null=True, blank=True)

	category = models.CharField('Categoria', max_length=20, choices=CATEGORY, default='sonho_ir', null=True, blank=True)
	status = models.CharField('Status', max_length=20, choices=STATUS, default='novo', null=True, blank=True)
	planning_description = models.TextField('Planejamento do Sonho', default=None, null=True, blank=True)
	
	observations = models.TextField('Mais alguma informação importante (Restrição alimentar, autonomia pra ir ao banheiro, etc)', default=None, null=True, blank=True)
	
	dream_nickname = models.CharField('Apelido do sonho (Esse campo será publicado)', max_length=255, default=None, null=True, blank=True)
	dream_short_description = models.TextField('Descrição rápida do sonho para página aberta (Esse campo será publicado)', default=None, null=True, blank=True)
	
	dream_needs = models.TextField('Necessidades do Sonho (Esse campo será publicado)', default=None, null=True, blank=True)
	needs_attended = models.TextField('Necessidades Atendidas', default=None, null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Sonhos'

# ================================================================================================================================= #

