from odoo import api, fields, models, tools, _

class AccountInvoice(models.Model):
    _inherit = "account.move"

    branch_id = fields.Many2one('company.branches', string='Branch')
    
    