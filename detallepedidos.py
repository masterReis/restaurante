# -*- coding: utf-8 -*-
from odoo import models, fields

class detallepedidos(models.Model):
    _name = "restaurante3.detallepedidos"

    name = fields.Char(string='ClaveDetallePedido')
    nameme = fields.Many2one('restaurante3.pedidos',require='True',string='ClavePedido')
    fecha = fields.Char(string='Fecha')
    folio = fields.Integer(string='Folio')
    empleados = fields.Many2one('restaurante3.empleados',require='True',string='Empleado')
    tipomesas = fields.Many2many('restaurante3.tipomesas',require='True',string='Tipomesas')
    clientes = fields.Many2one('restaurante3.clientes',require='True',string='Cliente')
    orden = fields.Many2many('restaurante3.menuorden',require='True',String='Nombre de Orden')
    cantidad = fields.Integer(string='Cantidad')
    descripcion = fields.Char(string='Descripcion')
    importe = fields.Integer(string='Importe')
    
    _sql_constraints = [
        ('unique_detallepedido', 'unique (name)', 'El detallepedido ya existe!')
    ]