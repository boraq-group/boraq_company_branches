from odoo import api, fields, models, tools, _

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    _description = 'Purchase order'

    branch_id = fields.Many2one('company.branches', string='Branch', domain="[('company_id','=',company_id)]")
    
    
    def _prepare_invoice(self):
        """ Override """
        invoice_vals = super(PurchaseOrder, self)._prepare_invoice()
        invoice_vals.update({
            'branch_id': self.branch_id.id
        })
        print('=============================================== invoice_vals', invoice_vals)
        return invoice_vals

