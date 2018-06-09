##############################################################################
#    Copyright (C) 2017 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from odoo import api, fields, models

# Domiciliary Unit Management

class OeHealthDomiciliaryUnit(models.Model):
    _name = 'oeh.medical.domiciliary.unit'
    _description = 'Domiciliary Unit Management'

    DWELLING = [
        ('Single / Detached House', 'Single / Detached House'),
        ('Apartment', 'Apartment'),
        ('Townhouse', 'Townhouse'),
        ('Factory', 'Factory'),
        ('Building', 'Building'),
        ('Mobile House', 'Mobile House'),
    ]

    MATERIAL = [
        ('Concrete', 'Concrete'),
        ('Adobe', 'Adobe'),
        ('Wood', 'Wood'),
        ('Mud / Straw', 'Mud / Straw'),
        ('Stone', 'Stone'),
    ]

    ROOF_TYPE = [
        ('Concrete', 'Concrete'),
        ('Adobe', 'Adobe'),
        ('Wood', 'Wood'),
        ('Thatched', 'Thatched'),
        ('Mud / Straw', 'Mud / Straw'),
        ('Stone', 'Stone'),
    ]

    HOUSING = [
        ('Shanty, deficient sanitary conditions', 'Shanty, deficient sanitary conditions'),
        ('Small, crowded but with good sanitary conditions', 'Small, crowded but with good sanitary conditions'),
        ('Comfortable and good sanitary conditions', 'Comfortable and good sanitary conditions'),
        ('Roomy and excellent sanitary conditions', 'Roomy and excellent sanitary conditions'),
        ('Luxury and excellent sanitary conditions', 'Luxury and excellent sanitary conditions'),
    ]

    name = fields.Char(string='Code', size=128, required=True)
    desc = fields.Char(string='Desc', size=25, required=True)
    address_street = fields.Char(string='Street', size=25)
    address_street_number = fields.Integer(string='Street #')
    address_street_bis = fields.Char(string='Apartment', size=25)
    address_district = fields.Char(string='District', size=25, help="Neighborhood, Village, Barrio....")
    address_municipality = fields.Char(string='Municipality', size=25, help="Municipality, Township, county ..")
    address_city = fields.Char(string='City', size=25)
    address_zip = fields.Char(string='Zip Code', size=25)
    address_country = fields.Many2one('res.country', string='Country', help='Country')
    address_state = fields.Many2one('res.country.state', string='State', help='State')
    institution = fields.Many2one('oeh.medical.health.center', string='Health Center')
    picture = fields.Binary(string="Picture")
    dwelling = fields.Selection(DWELLING, string='Type')
    materials = fields.Selection(MATERIAL, string='Material')
    roof_type = fields.Selection(ROOF_TYPE, string='Roof')
    total_surface = fields.Integer(string='Surface', help="Surface in sq. meters")
    bedrooms = fields.Integer(string='Bedrooms')
    bathrooms = fields.Integer(string='Bathrooms')
    housing = fields.Selection(HOUSING, string='Conditions', help="Housing and sanitary living conditions")
    sewers = fields.Boolean(string='Sanitary Sewers')
    water = fields.Boolean(string='Running Water')
    trash = fields.Boolean(string='Trash recollection')
    electricity = fields.Boolean(string='Electrical supply')
    gas = fields.Boolean(string='Gas supply')
    telephone = fields.Boolean(string='Telephone')
    television = fields.Boolean(string='Television')
    internet = fields.Boolean(string='Internet')

    _sql_constraints = [('name_uniq', 'unique(name)', 'The Domiciliary Unit name must be unique')]

    @api.multi
    def onchange_state(self, state_id):
        if state_id:
            state = self.env['res.country.state'].browse(state_id)
            return {'value': {'country_id': state.country_id.id}}
        return {}