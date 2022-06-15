# -*- coding: utf-8 -*-
from odoo import models, fields

class compras(models.Model):
    _name = "restaurante3.compras"

    name = fields.Char(string='ClaveCompra')
    fecha = fields.Char(string='Fecha')
    producto = fields.Many2one('restaurante3.productos',require='True',String='Nombre del Producto')
    cantidad = fields.Char(string='Cantidad ')
    descripcion = fields.Char(string='Descripcion')
    precio = fields.Integer(string='Precio')
    importe = fields.Integer(string='Importe')
    proveedor = fields.Many2one('restaurante3.proveedores', require='True', string='Proveedor')
    
    _sql_constraints = [
        ('unique_compra', 'unique (name)', 'La compra ya existe!')
    ]