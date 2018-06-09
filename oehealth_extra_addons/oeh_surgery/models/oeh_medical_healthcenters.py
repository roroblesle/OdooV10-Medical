# -*- encoding: utf-8 -*-
##############################################################################
#    Copyright (C) 2017 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from odoo import fields, api, models, _
from odoo.exceptions import UserError

# Operating Theaters (OT) Management
class OeHealthCentersOperatingRooms(models.Model):

    OT_STATES = [
        ('Free', 'Free'),
        ('Reserved', 'Reserved'),
        ('Occupied', 'Occupied'),
        ('Not Available', 'Not Available'),
    ]

    _name = 'oeh.medical.health.center.ot'
    _description = "Information about the health centers operating theaters"

    name = fields.Char(string='Operation Theater Name', size=32, required=True)
    building = fields.Many2one('oeh.medical.health.center.building', string='Building')
    info = fields.Text(string='Extra Info')
    state = fields.Selection(OT_STATES, string='Status', default=lambda *a: 'Free')

    _sql_constraints = [
            ('name_bed_uniq', 'unique (name)', 'The operation theater name is already occupied !')]


    # Preventing deletion of a operating theaters which is not in draft state
    @api.multi
    def unlink(self):
        for healthcenter in self.filtered(lambda healthcenter: healthcenter.state in ['Draft','Not Available']):
            raise UserError(_('You can not delete operating theaters(s) which is in "Reserved" or "Occupied" state !!'))
        return super(OeHealthCentersOperatingRooms, self).unlink()

    @api.multi
    def action_surgery_set_to_not_available(self):
        return self.write({'state': 'Not Available'})

    @api.multi
    def action_surgery_set_to_available(self):
        return self.write({'state': 'Free'})

class OeHealthCentersBuilding(models.Model):

    @api.multi
    def _ot_count(self):
        result = {}
        oe_ot = self.env['oeh.medical.health.center.ot']
        for building in self:
            domain = [('building', '=', building.id)]
            ot_ids = oe_ot.search(domain)
            ots = oe_ot.browse(ot_ids)
            ot_count = 0
            for ot in ots:
                ot_count+=1
            building.ot_count = ot_count
        return result

    _inherit = 'oeh.medical.health.center.building'
    ot_count = fields.Integer(compute=_ot_count, string="Operation Theaters")
