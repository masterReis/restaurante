# -*- coding: utf-8 -*-
from odoo import models, fields

class menuorden(models.Model):
    _name = "restaurante3.menuorden"

    name = fields.Char(string='ClaveMenu')
    platillo = fields.Char(string='Platillo')
    precio = fields.Integer(string='Precio')
    
    _sql_constraints = [
        ('unique_orden', 'unique (name)', 'La orden ya existe!')
    ]