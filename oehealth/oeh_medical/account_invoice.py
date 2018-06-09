##############################################################################
#    Copyright (C) 2017 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from odoo import api, SUPERUSER_ID, fields, models, _

class account_invoice(models.Model):
    _inherit = 'account.invoice'

    patient = fields.Many2one('oeh.medical.patient', string='Related Patient', help="Patient Name")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
