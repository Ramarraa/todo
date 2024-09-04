# models/todo_task.py
from odoo import fields, models

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Todo Task'

    name = fields.Char('Task Name', required=True)
    due_date = fields.Date('Due Date')
    description = fields.Text('Description')
    assign_to_id = fields.Many2one('res.partner', string='Assigned to')
    state = fields.Selection([
        ('new', 'New'),
        ('progress', 'In Progress'),
        ('complete', 'Completed'),
    ], string='Status', default='new')
