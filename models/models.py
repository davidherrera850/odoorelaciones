# -*- coding: utf-8 -*-

from odoo import models, fields, api

class odoo58(models.Model):
	_name = 'odoo58.odoo58'
	_description = 'odoo58.odoo58'

	name = fields.Char('DNI',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	pais = fields.Char(string='pais',required=True)

	equipo_id = fields.Many2one('odoo58.equipo', string='nombre equipo')

class equipo(models.Model):
	_name = 'odoo58.equipo'
	_description = 'odoo58.equipo'

	name = fields.Char('codequipo',required=True)
	nombreequipo = fields.Char(string='nombreequipo',required=True)
	siglas = fields.Char(string='siglas',required=True)

	jugadores_ids = fields.One2many('odoo58.odoo58', 'equipo_id', string='jugador equipo')
	partidos_ids = fields.Many2many('odoo58.partidos', string='numero partidos')
	doctores_id = fields.Many2one('odoo58.doctores', string='nombre doctor')
	ligas_id = fields.Many2one('odoo58.doctores', string='nombre liga')


class presidente(models.Model):
	_name = 'odoo58.presidente'
	_description = 'odoo58.presidente'

	name = fields.Char('codpresi',required=True)
	nombrepresi = fields.Char(string='nombrepresi',required=True)
	nacionalidad = fields.Char(string='nacionalidad',required=True)

class entrenador(models.Model):
	_name = 'odoo58.entrenador'
	_description = 'odoo58.entrenador'

	name = fields.Char('codentrenador',required=True)
	nombreentrenador = fields.Char(string='nombreentrenador',required=True)
	dnientrenador = fields.Char(string='dnientrenador',required=True)

class estadio(models.Model):
	_name = 'odoo58.estadio'
	_description = 'odoo58.estadio'

	name = fields.Char('codestadio',required=True)
	nombreestadio = fields.Char(string='nombreestadio',required=True)
	ciuda = fields.Char(string='ciuda',required=True)

class doctores(models.Model):
	_name = 'odoo58.doctores'
	_description = 'odoo58.doctores'

	name = fields.Char('coddoctor',required=True)
	nombredoctor = fields.Char(string='nombredoctor',required=True)
	especialidad = fields.Char(string='especialidad',required=True)

	mediequipos_id = fields.One2many('odoo58.equipo', 'doctores_id', string='doctor')

class liga(models.Model):
	_name = 'odoo58.liga'
	_description = 'odoo58.liga'

	name = fields.Char('codliga',required=True)
	nombreliga = fields.Char(string='nombreliga',required=True)
	numeroequipos = fields.Char(string='numeroequipos',required=True)

	ligaequipo_id = fields.One2many('odoo58.equipo', 'ligas_id', string='liga')


class arbitro(models.Model):
	_name = 'odoo58.arbitro'
	_description = 'odoo58.arbitro'

	name = fields.Char('codarbitro',required=True)
	nombrearbitro = fields.Char(string='nombrearbitro',required=True)
	origen = fields.Char(string='origen',required=True)

	parti_id = fields.Many2many('odoo58.partidos', string='Partido')

class partidos(models.Model):
	_name = 'odoo58.partidos'
	_description = 'odoo58.partidos'

	name = fields.Char('codpartido',required=True)
	equipolo = fields.Char(string='equipolo',required=True)
	equipovi = fields.Char(string='equipovi',required=True)

	equipos_ids = fields.Many2many('odoo58.equipo','partidos_ids', string='Partidos')
	arbitros_id = fields.Many2many('odoo58.arbitro','parti_id', string='Arbitro')


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
