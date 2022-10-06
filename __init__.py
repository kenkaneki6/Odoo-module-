# -*- coding: utf-8 -*-
#improting from odoo
from odoo import models, fields

#
class SaleOrder(models.Model):
    _inherit = 'sale_order'

    spokentoclient = fields.Boolean('Spoken to client', required=True)