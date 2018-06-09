##############################################################################
#    Copyright (C) 2017 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from odoo import fields, models

# Genetics Management

class OeHealthGenetics(models.Model):
    _name = 'oeh.medical.genetics'
    _description = "Information about the genetics risks"

    DOMINANCE = [
        ('Dominant','Dominant'),
        ('Recessive','Recessive'),
    ]

    name = fields.Char(string='Official Symbol', size=16)
    long_name = fields.Char(string='Official Long Name', size=256)
    gene_id = fields.Char(string='Gene ID', size=8, help="Default code from NCBI Entrez database.")
    chromosome = fields.Char(string='Affected Chromosome', size=2, help="Name of the affected chromosome")
    location = fields.Char(string='Location', size=32, help="Locus of the chromosome")
    dominance = fields.Selection(DOMINANCE, string='Dominance', index=True)
    info = fields.Text(string='Information', size=128, help="Name of the protein(s) affected")
