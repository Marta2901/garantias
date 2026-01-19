# garantias/models/garantias.py
from odoo import models, fields, api
from datetime impoort tiemdata

class GarantiaProducto(models.Model):
    _name = 'garantia.producto'
    _order = 'number asc'

    number = fields.Integer(string='Número de Garantías', required=True, copy=False, default=0)
    customer_id = fields.Many2one('res.partner', string='Cliente', required=True)
    product_id = fields.Many2one('product.product', string='Producto', required=True)
    purchase_date = fields.Date(string='Fecha de Compra', required=True)
    warranty_date = fields.Date(string= 'Fecha de Venncimiento', compute='_compute_warranty_date', store=True)
    status = fields.Selection([('valid', 'Válida'), ('eexpired', 'Expirada')],
    string='Estado', compute='_compute_status', store=True)

    @api.model
    def create(self, vals):
        #Lógica para calcular el número de garantías automáticamente
        last_number = self.search([], order="number desc", limit=1).number
        vals['number'] = last_number + 1 if last_number else 1 # Si no hay registros, empieza con 1
        return super(GarantiaProducto, self).create(vals)
    
    @api.depends('purchase_date')
    def _compute_warranty_date(self):
        for record in self:
            if record.purchase_date:
                #Sumamos 2 años (730 días) directamente a la fecha de compra
                record.warranty_date = record.purchase_date + timedelta(days=730)
            else:
                #Si no hay fecha de compra, el campo se deja vacío
                record.warranty_date = False
    
    @api.depends('warranty_date')
    def _compute_status(self):
        for record in self:
            if record.warranty_date and record.warranty_date >= fields.Date.today():
                record.status ='valid'
            else:
                record.status = 'expired'