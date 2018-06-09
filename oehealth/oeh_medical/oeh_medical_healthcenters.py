##############################################################################
#    Copyright (C) 2017 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

import logging
from odoo import api, fields, models, _
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.translate import _

_logger = logging.getLogger(__name__)

# Health Center Management

class OeHealthCenters(models.Model):
    _name = 'oeh.medical.health.center'
    _description = "Information about the health centers"
    _inherits={
        'res.partner': 'partner_id',
    }

    HEALTH_CENTERS = [
        ('Hospital', 'Hospital'),
        ('Nursing Home', 'Nursing Home'),
        ('Clinic', 'Clinic'),
        ('Community Health Center', 'Community Health Center'),
        ('Military Medical Facility', 'Military Medical Facility'),
        ('Other', 'Other'),
    ]

    @api.multi
    def _building_count(self):
        oe_buildings = self.env['oeh.medical.health.center.building']
        for hec in self:
            domain = [('institution', '=', hec.id)]
            buildings_ids = oe_buildings.search(domain)
            buildings = oe_buildings.browse(buildings_ids)
            bu_count = 0
            for bul in buildings:
                bu_count+=1
            hec.building_count = bu_count
        return True

    @api.multi
    def _pharmacy_count(self):
        oe_pharmacies = self.env['oeh.medical.health.center.pharmacy']
        for hec in self:
            domain = [('institution', '=', hec.id)]
            pharmacies_ids = oe_pharmacies.search(domain)
            pharmacies = oe_pharmacies.browse(pharmacies_ids)
            pha_count = 0
            for pha in pharmacies:
                pha_count+=1
            hec.building_count = pha_count
        return True


    partner_id = fields.Many2one('res.partner', string='Related Partner', required=True,ondelete='cascade', help='Partner-related data of the hospitals')
    health_center_type = fields.Selection(HEALTH_CENTERS, string='Type', help="Health center type", index=True)
    info = fields.Text('Extra Information')
    building_count = fields.Integer(compute=_building_count, string="Buildings")
    pharmacy_count = fields.Integer(compute=_pharmacy_count, string="Pharmacies")

    @api.model
    def create(self, vals):
        vals["is_institution"] = True
        vals["is_company"] = True
        health_center = super(OeHealthCenters, self).create(vals)
        return health_center

    @api.multi
    def onchange_state(self, state_id):
        if state_id:
            state = self.env['res.country.state'].browse(state_id)
            return {'value': {'country_id': state.country_id.id}}
        return {}

# Health Center Building

class OeHealthCentersBuilding(models.Model):
    _name = 'oeh.medical.health.center.building'
    _description = "Health Centers buildings"

    @api.multi
    def _ward_count(self):
        oe_wards = self.env['oeh.medical.health.center.ward']
        for building in self:
            domain = [('building', '=', building.id)]
            wards_ids = oe_wards.search(domain)
            wards = oe_wards.browse(wards_ids)
            wa_count = 0
            for war in wards:
                wa_count+=1
            building.ward_count = wa_count
        return True

    @api.multi
    def _bed_count(self):
        oe_beds = self.env['oeh.medical.health.center.beds']
        for building in self:
            domain = [('building', '=', building.id)]
            beds_ids = oe_beds.search(domain)
            beds = oe_beds.browse(beds_ids)
            be_count = 0
            for bed in beds:
                be_count+=1
            building.bed_count = be_count
        return True

    name = fields.Char(string='Name', size=128, required=True, help="Name of the building within the institution")
    institution = fields.Many2one('oeh.medical.health.center', string='Health Center',required=True)
    code = fields.Char (string='Code', size=64)
    info = fields.Text (string='Extra Info')
    ward_count = fields.Integer(compute=_ward_count, string="Wards")
    bed_count = fields.Integer(compute=_bed_count, string="Beds")

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The building name must be unique !')
    ]

# Health Center Wards Management

class OeHealthCentersWards(models.Model):
    _name = "oeh.medical.health.center.ward"

    GENDER = [
        ('Men Ward','Men Ward'),
        ('Women Ward','Women Ward'),
        ('Unisex','Unisex'),
    ]

    WARD_STATES = [
        ('Beds Available','Beds Available'),
        ('Full','Full'),
    ]

    @api.multi
    def _bed_count(self):
        oe_beds = self.env['oeh.medical.health.center.beds']
        for ward in self:
            domain = [('ward', '=', ward.id)]
            beds_ids = oe_beds.search(domain)
            beds = oe_beds.browse(beds_ids)
            be_count = 0
            for bed in beds:
                be_count+=1
            ward.bed_count = be_count
        return True

    name = fields.Char(string='Name', size=128, required=True, help="Ward / Room code")
    institution = fields.Many2one('oeh.medical.health.center',string='Health Center', required=True)
    building = fields.Many2one('oeh.medical.health.center.building',string='Building', required=True)
    floor = fields.Integer(string='Floor Number')
    private = fields.Boolean(string='Private Room',help="Check this option for private room")
    bio_hazard = fields.Boolean(string='Bio Hazard',help="Check this option if there is biological hazard")
    telephone = fields.Boolean(string='Telephone access')
    ac = fields.Boolean(string='Air Conditioning')
    private_bathroom = fields.Boolean(string='Private Bathroom')
    guest_sofa = fields.Boolean(string='Guest sofa-bed')
    tv = fields.Boolean(string='Television')
    internet = fields.Boolean(string='Internet Access')
    refrigerator = fields.Boolean(string='Refrigerator')
    microwave = fields.Boolean(string='Microwave')
    gender = fields.Selection(GENDER,string='Gender',default=lambda *a: 'Unisex')
    state = fields.Selection(WARD_STATES,string='Status',default='Beds Available')
    info = fields.Text('Extra Info')
    bed_count = fields.Integer(compute=_bed_count, string="Beds")

    _sql_constraints = [
        ('name_ward_uniq', 'unique (name,building)', 'The ward name is already configured in selected building !')
    ]

# Beds Management
class OeHealthCentersBeds(models.Model):

    BED_TYPES = [
        ('Gatch Bed','Gatch Bed'),
        ('Electric','Electric'),
        ('Stretcher','Stretcher'),
        ('Low Bed','Low Bed'),
        ('Low Air Loss','Low Air Loss'),
        ('Circo Electric','Circo Electric'),
        ('Clinitron','Clinitron'),
    ]

    BED_STATES = [
        ('Free', 'Free'),
        ('Reserved', 'Reserved'),
        ('Occupied', 'Occupied'),
        ('Not Available', 'Not Available'),
    ]

    CHANGE_BED_STATUS = [
        ('Mark as Reserved', 'Mark as Reserved'),
        ('Mark as Not Available', 'Mark as Not Available'),
    ]
    _name = 'oeh.medical.health.center.beds'
    _description = "Information about the health centers beds"
    _inherits={
        'product.product': 'product_id',
    }

    product_id = fields.Many2one('product.product', string='Related Product', required=True, ondelete='cascade', help='Product-related data of the hospital beds')
    institution = fields.Many2one('oeh.medical.health.center',string='Health Center')
    building = fields.Many2one('oeh.medical.health.center.building', string='Building')
    ward = fields.Many2one('oeh.medical.health.center.ward','Ward', domain="[('building', '=', building)]", help="Ward or room", ondelete='cascade')
    bed_type = fields.Selection(BED_TYPES,string='Bed Type', required=True, default=lambda *a: 'Gatch Bed')
    telephone_number = fields.Char (string='Telephone Number', size=128, help="Telephone Number / Extension")
    info = fields.Text(string='Extra Info')
    state = fields.Selection(BED_STATES, string='Status', default='Free')
    change_bed_status = fields.Selection(CHANGE_BED_STATUS, string='Change Bed Status')

    _sql_constraints = [
        ('name_bed_uniq', 'unique (name,ward)', 'The bed name is already configured in selected ward !')
    ]

    @api.multi
    def onchange_bed_status(self, change_bed_status, state):
        res = {}
        if state and change_bed_status:
            if state=="Occupied":
                raise UserError(_('Bed status can not change if it already occupied!'))
            else:
                if change_bed_status== "Mark as Reserved":
                    res = self.write({'state': 'Reserved'})
                else:
                    res = self.write({'state': 'Not Available'})
        return res

    # Preventing deletion of a beds which is not in draft state
    @api.multi
    def unlink(self):
        for beds in self.filtered(lambda beds: beds.state in ['Free','Not Available']):
            raise UserError(_('You can not delete bed(s) which is in "Reserved" or "Occupied" state !!'))
        return super(OeHealthCentersBeds, self).unlink()

    @api.model
    def create(self, vals):
        if vals.get('change_bed_status') and vals.get('state') and vals.get('state')=="Occupied":
            raise AccessError(_('Bed status can not change if it already occupied!'))
        vals["is_bed"] = True
        beds = super(OeHealthCentersBeds, self).create(vals)
        return beds

    @api.multi
    def write(self, vals):
        if 'change_bed_status' in vals:
            if vals.get('change_bed_status') in ('Mark as Reserved','Mark as Not Available'):
                for beds in self.filtered(lambda beds: beds.state in ['Occupied']):
                    raise AccessError(_('Bed status can not change if it already occupied!'))
        return super(OeHealthCentersBeds, self).write(vals)
