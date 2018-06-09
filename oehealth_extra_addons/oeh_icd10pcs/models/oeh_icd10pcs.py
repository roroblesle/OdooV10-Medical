# -*- encoding: utf-8 -*-
##############################################################################
#    Copyright (C) 2017 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from odoo import fields, models, _


class OeHealthIC10Procedures(models.Model):
    _name = 'oeh.medical.procedure'
    _description = 'IC10 Procedure Codes'

    name = fields.Char(string='Code', size=16, required=True)
    description = fields.Char(string='Long Text', size=256, required=True)

