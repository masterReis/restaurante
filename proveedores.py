# -*- coding: utf-8 -*-
from odoo import models,fields

class proveedores(models.Model):
    _name = 'restaurante3.proveedores'

    name = fields.Char(string='Clave')
    nombre = fields.Char(string='Nombre y Apellidos')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    sexo = fields.Selection([('f','Femenino'),('m','Masculino')],string='Sexo')
    edad = fields.Integer(string='Edad')
    serviciooproducto = fields.Many2one('restaurante3.productos',require='True',String='Servicio o Producto')


    _sql_constraints = [
        ('unique_proveedor', 'unique (name)', 'El proveedor ya existe!')
    ]

