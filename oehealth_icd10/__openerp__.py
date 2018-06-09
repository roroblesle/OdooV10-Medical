# -*- encoding: utf-8 -*-
##############################################################################
#    Copyright (C) 2017 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

{
    'name': 'oeHealth ICD-10',
    'version': '1.0',
    'author': 'Braincrew Apps',
    'category': 'Generic Modules/Medical',
    'summary': 'International Classification of Diseases',
    'depends': ['oehealth'],
    'description': """

    World Health Organization - International Classification of Diseases for MEDICAL (10th revision)

    """,
    "website": "http://oehealth.in",
    "init": [],
    "data": [
              "data/oeh_disease_categories.xml",
              "data/oeh_diseases.xml",
            ],
    "active": False
}
