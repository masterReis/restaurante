# -*- coding: utf-8 -*-
from odoo import models, fields

class pedidos(models.Model):
    _name = "restaurante3.pedidos"

    tipomesas = fields.Many2many('restaurante3.tipomesas')
    name = fields.Char(string='ClavePedido')
    fechapedido = fields.Char(string='Fecha')
    folio = fields.Char(string='Folio')
    orden = fields.Many2many('restaurante3.menuorden',require='True',string='Orden')
    descripcion = fields.Char(string='Descripcion')
    empleados = fields.Many2one('restaurante3.empleados',require='True',string='Empleados')
    cliente = fields.Many2one('restaurante3.clientes',require='True',string='Cliente')
    
    
    _sql_constraints = [
        ('unique_pedido', 'unique (name)', 'El pedido ya existe!')
    ]