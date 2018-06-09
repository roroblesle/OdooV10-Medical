# -*- encoding: utf-8 -*-
##############################################################################
#    Copyright (C) 2017 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from odoo import fields, api, models, _
import datetime

class OeHealthPatientMedicalCert(models.Model):
    _name = 'oeh.medical.patient.medical.cert'
    _description = 'Patient Medical Certificate Management'

    @api.multi
    def _get_duration(self):
        for obj in self:
            start_date = datetime.datetime.strptime(obj.start_date, "%Y-%m-%d")
            end_date = datetime.datetime.strptime(obj.end_date, "%Y-%m-%d")
            duration = end_date - start_date
            obj.no_of_days = duration.days
        return True

    name = fields.Char(string='MC #', size=64, readonly=True, default=lambda *a: '/')
    start_date = fields.Date(string='From Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    no_of_days = fields.Integer(compute=_get_duration, string="No of Days")
    issue_date = fields.Date(string='DateTime MC is issued', required=True, default=lambda *a: datetime.datetime.now())
    patient = fields.Many2one('oeh.medical.patient', string='Patient', help="Patient Name", required=True)
    doctor = fields.Many2one('oeh.medical.physician', string='Physician', domain=[('is_pharmacist','=',False)], help="Health professional", required=True)
    institution = fields.Many2one('oeh.medical.health.center', string='Institution', help="Institution where doctor works")
    reason = fields.Text(string='Reason', required=True)

    @api.model
    def create(self,vals):
        sequence = self.env['ir.sequence'].next_by_code('oeh.medical.patient.medical.cert')
        vals['name'] = sequence
        return super(OeHealthPatientMedicalCert, self).create(vals)


    @api.multi
    def print_patient_medical_cert(self):
        '''
        This function prints the patient medical cert
        '''
        return self.env['report'].get_action(self, 'oehealth_extra_addons.report_patient_medical_cert')

# Inheriting Patient module to add "Medical Certificate" screen reference
class OeHealthPatient(models.Model):
    _inherit='oeh.medical.patient'
    medical_cert_ids = fields.One2many('oeh.medical.patient.medical.cert', 'patient', string='Medical Certificates')