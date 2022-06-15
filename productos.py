# -*- coding: utf-8 -*-
from odoo import models, fields

class productos(models.Model):
    _name = "restaurante3.productos"

    name = fields.Char(string='ClaveProducto')
    producto = fields.Char(string='Producto')
    cantidad = fields.Integer(string='Cantidad')
    precio = fields.Integer(string='Precio')
    proveedor = fields.Many2one('restaurante3.proveedores', require='True', string='Proveedor')
    
    _sql_constraints = [
        ('unique_producto', 'unique (name)', 'El producto ya existe!')
    ]