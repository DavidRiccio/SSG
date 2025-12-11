

from odoo import models, fields, api

from datetime import date 


class ListaTareas(models.Model):
    
    _name = 'lista_tareas.lista_tareas'
    _description = 'Lista de tareas'

    
    tarea = fields.Char(string='Tarea')
    asignado_a = fields.Many2one('res.users', string='Asignacion')
    prioridad = fields.Integer(string='Prioridad')
    realizada = fields.Boolean(string='Realizada')
    fecha_limite = fields.Date(string='Fecha Límite')
    fecha_creacion = fields.Date(string='Fecha de Creación', default=fields.Date.today,readonly=True )
    urgente = fields.Boolean(string='Urgente',compute='_value_urgente',store=True)    
    retrasada = fields.Boolean(string='Retrasada',compute='_compute_retrasada',store=True)   
     
    @api.depends('prioridad')
    def _value_urgente(self):
        for record in self:
            record.urgente = record.prioridad > 10
    
    @api.depends('realizada', 'fecha_limite')
    def _compute_retrasada(self):
        hoy = date.today()
        for record in self:
            es_retrasada = (
                not record.realizada and 
                record.fecha_limite and 
                record.fecha_limite < hoy
            )
            record.retrasada = es_retrasada