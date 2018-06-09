##############################################################################
#    Copyright (C) 2017 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from odoo import fields, models

# Ethnic Groups Management

class OeHealthEthnicGroups(models.Model):
    _name = 'oeh.medical.ethnicity'
    _description = "Ethnic Groups"

    name = fields.Char(string='Ethnic Groups', size=256, required=True)

    _sql_constraints = [
            ('name_uniq', 'unique (name)', 'The ethnic group must be unique !')]