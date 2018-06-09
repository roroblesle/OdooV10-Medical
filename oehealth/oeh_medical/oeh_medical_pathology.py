##############################################################################
#    Copyright (C) 2017 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from odoo import api, SUPERUSER_ID, fields, models, _


class OeHealthPathologyCategory(models.Model):
    _description='Disease Categories'
    _name = 'oeh.medical.pathology.category'

    name = fields.Char(string='Category Name', required=True, size=128)
    parent_id = fields.Many2one('oeh.medical.pathology.category', string='Parent Category', index=True)
    child_ids = fields.One2many('oeh.medical.pathology.category', 'parent_id', string='Children Category')
    active = fields.Boolean(string='Active', default=lambda *a: 1)

    _order = 'parent_id,id'


class OeHealthPathology(models.Model):
    _name = "oeh.medical.pathology"
    _description = "Diseases"

    name = fields.Char(string='Disease Name', size=128, help="Disease name", required=True)
    code = fields.Char(string='Code', size=32, help="Specific Code for the Disease (eg, ICD-10, SNOMED...)")
    category = fields.Many2one('oeh.medical.pathology.category', string='Disease Category')
    chromosome = fields.Char(string='Affected Chromosome', size=128, help="chromosome number")
    protein = fields.Char(string='Protein involved', size=128, help="Name of the protein(s) affected")
    gene = fields.Char(string='Gene', size=128, help="Name of the gene(s) affected")
    info = fields.Text(string='Extra Info')

    _sql_constraints = [
        ('code_uniq', 'unique (code)', 'The disease code must be unique')]

    @api.model
    def name_search(self, name, args=[], operator='ilike', limit=80):
        args2 = args[:]
        if name:
            args += [('name', operator, name)]
            args2 += [('code', operator, name)]
        ids = self.search(args, limit=limit)
        ids += self.search(args2, limit=limit)
        res = self.name_get()
        return res