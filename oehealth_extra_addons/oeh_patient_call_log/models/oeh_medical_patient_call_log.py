##############################################################################
#    Copyright (C) 2017 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from odoo import fields, api, models, _
from odoo.exceptions import UserError
import datetime

# Patient Call Logs Management

class OeHealthPatientCallLog(models.Model):
    _name = 'oeh.medical.patient.call.log'
    _description = 'Patient Call Logs Management'

    CALL_TYPE = [
        ('Phone', 'Phone'),
        ('Email', 'Email'),
        ('SMS', 'SMS'),
        ('Other', 'Other'),
    ]

    name = fields.Char(string='Call Log #', size=64, readonly=True, default=lambda *a: '/')
    call_type = fields.Selection(CALL_TYPE, string="Call Type", required=True)
    log_date = fields.Datetime('Date/Time of contact', required=True, default=lambda *a: datetime.datetime.now())
    person_in_charge = fields.Many2one('res.users', string='Person In Charge', required=True, default=lambda self: self.env.uid)
    patient = fields.Many2one('oeh.medical.patient', string='Patient', help="Patient Name", required=True)
    call_log = fields.Text(string='Call Log', required=True)
    patient_id = fields.Char(string='Patient ID', size=64)

    @api.model
    def create(self, vals):
        sequence = self.env['ir.sequence'].next_by_code('oeh.medical.patient.call.log')
        vals['name'] = sequence
        return super(OeHealthPatientCallLog, self).create(vals)

    @api.multi
    def onchange_patient(self, patient):
        if patient:
            patient_id = self.env['oeh.medical.patient'].browse(patient)
            return {'value': {'patient_id': patient_id.identification_code}}
        return {}

    @api.multi
    def write(self, vals):
        for clog in self:
            if clog.person_in_charge.id != self.env.uid:
                raise UserError(_('Only the person in charge is allowed to update the details'))
        return super(OeHealthPatientCallLog, self).write(vals)

    # Inheriting Patient module to add "Call Logs" screen reference
class OeHealthPatient(models.Model):
    _inherit='oeh.medical.patient'
    call_log_ids = fields.One2many('oeh.medical.patient.call.log', 'patient', string='Call Logs')
