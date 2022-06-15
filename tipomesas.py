# -*- coding: utf-8 -*-
from odoo import models, fields

class tipomesas(models.Model):
    _name = "restaurante3.tipomesas"

    name = fields.Char(string='NumeroMesa')
    descripcion = fields.Char(string='Descripcion')
    clavemesa = fields.Char(string='ClaveMesa')
    
    _sql_constraints = [
        ('unique_tipomesa', 'unique (namemesa)', 'ya existe!')
    ]