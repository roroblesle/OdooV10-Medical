# -*- encoding: utf-8 -*-
##############################################################################
#    Copyright (C) 2017 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from odoo import fields, models

class OeHealthPediatricsNewBorn(models.Model):
    _name = "oeh.medical.pediatrics.growth.chart.who"

    SEX = [
        ('m', 'Male'),
        ('f', 'Female'),
    ]

    MEASURE = [
        ('p', 'Percentiles'),
        ('z', 'Z-scores'),
    ]

    INDICATOR = [
        ('l/h-f-a', 'Length/height for age'),
        ('w-f-a', 'Weight for age'),
        ('bmi-f-a', 'Body mass index for age (BMI for age)'),
    ]

    indicator = fields.Selection(INDICATOR, string='Indicator', required=True)
    measure = fields.Selection(MEASURE, string='Measure', required=True)
    sex = fields.Selection(SEX, string='Sex')
    month = fields.Integer(string='Month')
    type = fields.Char(string='Type', size=56)
    value = fields.Float(string='Value')