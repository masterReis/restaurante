# -*- coding: utf-8 -*-
from odoo import models,fields, api

class clientes(models.Model):
    _name = 'restaurante3.clientes'

    name = fields.Char(string='Nombre y Apellidos')
    numcliente = fields.Char(string='NumCliente')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    sexo = fields.Selection([('f','Femenino'),('m','Masculino')],string='Sexo')
    edad = fields.Integer(string='Edad')


    _sql_constraints = [
        ('unique_cliente', 'unique (name)', 'El cliente ya existe!')
    ]
