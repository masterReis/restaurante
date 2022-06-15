# -*- coding: utf-8 -*-
from odoo import models,fields

class empleados(models.Model):
    _name = 'restaurante3.empleados'

    name  = fields.Char(string='Nombre y Apellidos')
    numempleado = fields.Char(string='NumEmpleado')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    sexo = fields.Selection([('f','Femenino'),('m','Masculino')],string='Sexo')
    edad = fields.Integer(string='Edad')


    _sql_constraints = [
        ('unique_empleado', 'unique (name)', 'El empleado ya existe!')
    ]