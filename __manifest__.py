# -*- coding: utf-8 -*-
{
    'name': 'Restaurante3',
    'version': '1.0',
    'category': 'FIVE START',
    'description': 'SISTEMA RESTAURANTE',
    'author': 'JULIO GOD',
    'maintainer': 'HUAWEI',
    'website': 'https://www.instagram.com/julioc.s.g/',
    'depends': ['base'],
    'data': [
        'views/clientes_view.xml',
        'views/empleados_view.xml',
        'views/menuorden_view.xml',
        'views/pedidos_view.xml',
        'views/productos_view.xml',
        'views/proveedores_view.xml',
        'views/compras_view.xml',
        'views/detallepedidos_view.xml',
        'reports/ticket.xml',
        'views/tipomesas_view.xml',
        'views/menu_view.xml',
        'security/pedidos.xml',
        'security/ir.model.access.csv',
        
    ],
    'installable': True,
    'auto_install': False,
}