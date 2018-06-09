# -*- encoding: utf-8 -*-
##############################################################################
#    Copyright (C) 2017 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from odoo import fields, models

class oeHealthPartner(models.Model):
    _inherit = 'res.partner'
    is_baby = fields.Boolean(string='Baby', help='Check if the party is a baby')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
