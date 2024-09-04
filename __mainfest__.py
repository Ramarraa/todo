# __manifest__.py
{
    'name': 'Todo App',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'Simple Todo App',
    'description': 'A simple Odoo module for managing tasks.',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/todo_task_views.xml',
        'data/todo_task_data.xml',
    ],
    'installable': True,
    'application': True,

}
