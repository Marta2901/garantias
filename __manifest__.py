# garantias/__manifest__.py
{
    'name': 'Gestión de Garantías',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Gestión de garantías para productos vendidos.',
    'description': """
    Módulo para gestionar las garantías de productos vendidos a clientes.
    Permite registrar fechas de compra, fechas de vencimiento y calcular
    automáticamente el estado de la garantía.
    """,
    'author': 'Marta Enriquez',
    'depends': ['base', 'sale', 'contacts'], # Requiere módulos base, ventas y contactos
    'data': [
        'views/garantia_views.xml',
        'security/ir.model.access.csv',
    ],
    'icon': '/garantias/static/description/icon54.png',
    'installable': True,
    'application': True,
    }