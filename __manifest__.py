{
    'name': 'Product Category Lock',
    'version': '1.0',
    'summary': 'Evita modificaciones accidentales a las categorías de producto',
    'description': 'Bloquea la edición y eliminación de categorías de producto para proteger configuraciones automáticas.',
    'author': 'Diego Gajardo',
    'website': 'https://holdconet.cl,
    'category': 'Inventory',
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_category_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
