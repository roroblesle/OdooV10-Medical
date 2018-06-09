##############################################################################
#    Copyright (C) 2016 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from odoo import api, fields, models, _


class oeHealthPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'Partner'

    is_insurance_company = fields.Boolean(string='Insurance Company', help='Check if the party is an Insurance Company')
    is_institution = fields.Boolean(string='Institution', help='Check if the party is a Medical Center')
    is_doctor = fields.Boolean(string='Health Professional', help='Check if the party is a health professional')
    is_patient = fields.Boolean(string='Patient', help='Check if the party is a patient')
    is_person = fields.Boolean(string='Person', help='Check if the party is a person.')
    is_pharmacy = fields.Boolean(string='Pharmacy', help='Check if the party is a Pharmacy')
    ref = fields.Char(size=256, string='SSN', help='Patient Social Security Number or equivalent')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
