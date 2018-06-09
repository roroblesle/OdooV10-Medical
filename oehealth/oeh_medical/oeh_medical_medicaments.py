##############################################################################
#    Copyright (C) 2015 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from odoo import api, fields, models, _


# Medicines
class OeHealthMedicines(models.Model):
    _name = 'oeh.medical.medicines'
    _description = "Information about the medicines"
    _inherits={
        'product.product': 'product_id',
    }

    MEDICAMENT_TYPE = [
        ('Medicine', 'Medicine'),
        ('Vaccine', 'Vaccine'),
    ]

    product_id = fields.Many2one('product.product', string='Related Product', required=True,ondelete='cascade', help='Product-related data of the medicines')
    therapeutic_action = fields.Char(string='Therapeutic effect', size=128, help="Therapeutic action")
    composition = fields.Text(string='Composition',help="Components")
    indications = fields.Text(string='Indication',help="Indications")
    dosage = fields.Text(string='Dosage Instructions',help="Dosage / Indications")
    overdosage = fields.Text(string='Overdosage',help="Overdosage")
    pregnancy_warning = fields.Boolean(string='Pregnancy Warning', help="Check when the drug can not be taken during pregnancy or lactancy")
    pregnancy = fields.Text(string='Pregnancy and Lactancy',help="Warnings for Pregnant Women")
    adverse_reaction = fields.Text(string='Adverse Reactions')
    storage = fields.Text(string='Storage Conditions')
    info = fields.Text(string='Extra Info')
    medicament_type = fields.Selection(MEDICAMENT_TYPE, string='Medicament Type')

# Medicaments Configuration
class OeHealthDoseUnit(models.Model):
    _name = "oeh.medical.dose.unit"
    _description = "Medical Dose Unit"
    name = fields.Char(string='Unit', size=32, required=True)
    desc = fields.Char(string='Description', size=64)

class OeHealthDrugRoute(models.Model):
    _name = "oeh.medical.drug.route"
    _description = "Medical Drug Route"
    name = fields.Char(string='Route', size=32, required=True)
    code = fields.Char(string='Code', size=64)

class OeHealthDrugForm(models.Model):
    _name = "oeh.medical.drug.form"
    _description = "Medical Dose Form"
    name = fields.Char(string='Form', size=32, required=True)
    code = fields.Char(string='Code', size=64)

class OeHealthDosage (models.Model):
    _name = "oeh.medical.dosage"
    _description = "Medicines Dosage"
    name = fields.Char(string='Frequency', size=256, help='Common dosage frequency')
    code = fields.Char(string='Code', size=64, help='Dosage Code, such as SNOMED, 229798009 = 3 times per day')
    abbreviation = fields.Char(string='Abbreviation', size=64, help='Dosage abbreviation, such as tid in the US or tds in the UK')
