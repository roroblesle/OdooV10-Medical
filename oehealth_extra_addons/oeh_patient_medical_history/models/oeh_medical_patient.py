##############################################################################
#    Copyright (C) 2017 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from odoo import fields, api, models, _

 # Inheriting Patient module to add fields to record patient medical histories
class OeHealthPatient(models.Model):
    _inherit='oeh.medical.patient'

    hbv_infection_chk = fields.Boolean(string='HBV Infection')
    hbv_infection_remarks = fields.Text(string='HBV Infection Remarks')
    dm_chk = fields.Boolean(string='DM')
    dm_remarks = fields.Text(string='DM Remarks')
    ihd_chk = fields.Boolean(string='IHD')
    ihd_remarks = fields.Text(string='IHD Remarks')
    cold_chk = fields.Boolean(string='Cold')
    cold_remarks = fields.Text(string='Cold Remarks')
    hypertension_chk = fields.Boolean(string='Hypertension')
    hypertension_remarks = fields.Text(string='Hypertension Remarks')
    surgery_chk = fields.Boolean(string='Surgery')
    surgery_remarks = fields.Text(string='Surgery Remarks')
    others_past_illness = fields.Text(string='Others Past Illness')
    nsaids_chk = fields.Boolean(string='Nsaids')
    nsaids_remarks = fields.Text(string='Nsaids Remarks')
    aspirin_chk = fields.Boolean(string='Aspirin')
    aspirin_remarks = fields.Text(string='Aspirin Remarks')
    laxative_chk = fields.Boolean(string='Laxative')
    laxative_remarks = fields.Text(string='Laxative Remarks')
    others_drugs = fields.Text(string='Others Drugs')
    lmp_chk = fields.Boolean(string='LMP')
    lmp_dt = fields.Date(string='Date')
    menorrhagia_chk = fields.Boolean(string='Menorrhagia')
    menorrhagia_remarks = fields.Text(string='Menorrhagia Remarks')
    dysmenorrhoea_chk = fields.Boolean(string='Dysmenorrhoea')
    dysmenorrhoea_remarks = fields.Text(string='Dysmenorrhoea Remarks')
    bleeding_pv_chk = fields.Boolean(string='Bleeding PV')
    bleeding_pv_remarks = fields.Text(string='Bleeding PV Remarks')
    last_pap_smear_chk = fields.Boolean(string='Last PAP smear')
    last_pap_smear_remarks = fields.Text(string='Last PAP smear Remarks')


# Inheriting Appointment module to add fields to record patient medical histories
class OeHealthAppointment(models.Model):
    _inherit='oeh.medical.appointment'

    hbv_infection_chk = fields.Boolean(string='HBV Infection', readonly=True, states={'Scheduled': [('readonly', False)]})
    hbv_infection_remarks = fields.Text(string='HBV Infection Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    dm_chk = fields.Boolean(string='DM', readonly=True,states={'Scheduled': [('readonly', False)]})
    dm_remarks = fields.Text(string='DM Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    ihd_chk = fields.Boolean(string='IHD', readonly=True,states={'Scheduled': [('readonly', False)]})
    ihd_remarks = fields.Text(string='IHD Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    cold_chk = fields.Boolean(string='Cold', readonly=True,states={'Scheduled': [('readonly', False)]})
    cold_remarks = fields.Text(string='Cold Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    hypertension_chk = fields.Boolean(string='Hypertension', readonly=True,states={'Scheduled': [('readonly', False)]})
    hypertension_remarks = fields.Text(string='Hypertension Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    surgery_chk = fields.Boolean(string='Surgery', readonly=True,states={'Scheduled': [('readonly', False)]})
    surgery_remarks = fields.Text(string='Surgery Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    others_past_illness = fields.Text(string='Others Past Illness', readonly=True,states={'Scheduled': [('readonly', False)]})
    nsaids_chk = fields.Boolean(string='Nsaids', readonly=True,states={'Scheduled': [('readonly', False)]})
    nsaids_remarks = fields.Text(string='Nsaids Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    aspirin_chk = fields.Boolean(string='Aspirin', readonly=True,states={'Scheduled': [('readonly', False)]})
    aspirin_remarks = fields.Text(string='Aspirin Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    laxative_chk = fields.Boolean(string='Laxative', readonly=True,states={'Scheduled': [('readonly', False)]})
    laxative_remarks = fields.Text(string='Laxative Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    others_drugs = fields.Text(string='Others Drugs', readonly=True,states={'Scheduled': [('readonly', False)]})
    lmp_chk = fields.Boolean(string='LMP', readonly=True,states={'Scheduled': [('readonly', False)]})
    lmp_dt = fields.Date(string='Date', readonly=True,states={'Scheduled': [('readonly', False)]})
    menorrhagia_chk = fields.Boolean(string='Menorrhagia', readonly=True,states={'Scheduled': [('readonly', False)]})
    menorrhagia_remarks = fields.Text(string='Menorrhagia Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    dysmenorrhoea_chk = fields.Boolean(string='Dysmenorrhoea', readonly=True,states={'Scheduled': [('readonly', False)]})
    dysmenorrhoea_remarks = fields.Text(string='Dysmenorrhoea Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    bleeding_pv_chk = fields.Boolean(string='Bleeding PV', readonly=True,states={'Scheduled': [('readonly', False)]})
    bleeding_pv_remarks = fields.Text(string='Bleeding PV Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    last_pap_smear_chk = fields.Boolean(string='Last PAP smear', readonly=True,states={'Scheduled': [('readonly', False)]})
    last_pap_smear_remarks = fields.Text(string='Last PAP smear Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})


    @api.multi
    def onchange_patient_history(self, patient=False):
        hbv_infection = False
        hbv_infection_remarks = ''
        dm_chk = False
        dm_remarks = ''
        ihd_chk = False
        ihd_remarks = ''
        cold_chk = False
        cold_remarks = ''
        hypertension_chk = False
        hypertension_remarks = ''
        surgery_chk = False
        surgery_remarks = ''
        others_past_illness = ''
        nsaids_chk = False
        nsaids_remarks = ''
        aspirin_chk = False
        aspirin_remarks = ''
        laxative_chk = False
        laxative_remarks = ''
        others_drugs = ''
        lmp_chk = False
        lmp_dt = None
        menorrhagia_chk = False
        menorrhagia_remarks = ''
        dysmenorrhoea_chk = False
        dysmenorrhoea_remarks = ''
        bleeding_pv_chk = False
        bleeding_pv_remarks = ''
        last_pap_smear_chk = False
        last_pap_smear_remarks = ''

        if patient:
            patient_history_record = self.env['oeh.medical.patient'].browse(patient)
            hbv_infection = patient_history_record and patient_history_record.hbv_infection_chk or False
            hbv_infection_remarks = patient_history_record and patient_history_record.hbv_infection_remarks or ''
            dm_chk = patient_history_record and patient_history_record.dm_chk or False
            dm_remarks = patient_history_record and patient_history_record.dm_remarks or ''
            ihd_chk = patient_history_record and patient_history_record.ihd_chk or False
            ihd_remarks = patient_history_record and patient_history_record.ihd_remarks or ''
            cold_chk = patient_history_record and patient_history_record.cold_chk or False
            cold_remarks = patient_history_record and patient_history_record.cold_remarks or ''
            hypertension_chk = patient_history_record and patient_history_record.hypertension_chk or False
            hypertension_remarks = patient_history_record and patient_history_record.hypertension_remarks or ''
            surgery_chk = patient_history_record and patient_history_record.surgery_chk or False
            surgery_remarks = patient_history_record and patient_history_record.surgery_remarks or ''
            others_past_illness = patient_history_record and patient_history_record.others_past_illness or ''
            nsaids_chk = patient_history_record and patient_history_record.nsaids_chk or False
            nsaids_remarks = patient_history_record and patient_history_record.nsaids_remarks or ''
            aspirin_chk = patient_history_record and patient_history_record.aspirin_chk or False
            aspirin_remarks = patient_history_record and patient_history_record.aspirin_remarks or ''
            laxative_chk = patient_history_record and patient_history_record.laxative_chk or False
            laxative_remarks = patient_history_record and patient_history_record.laxative_remarks or ''
            others_drugs = patient_history_record and patient_history_record.others_drugs or ''
            lmp_chk = patient_history_record and patient_history_record.lmp_chk or False
            lmp_dt = patient_history_record and patient_history_record.lmp_dt or ''
            menorrhagia_chk = patient_history_record and patient_history_record.menorrhagia_chk or False
            menorrhagia_remarks = patient_history_record and patient_history_record.menorrhagia_remarks or ''
            dysmenorrhoea_chk = patient_history_record and patient_history_record.dysmenorrhoea_chk or False
            dysmenorrhoea_remarks = patient_history_record and patient_history_record.dysmenorrhoea_remarks or ''
            bleeding_pv_chk = patient_history_record and patient_history_record.bleeding_pv_chk or False
            bleeding_pv_remarks = patient_history_record and patient_history_record.bleeding_pv_remarks or ''
            last_pap_smear_chk = patient_history_record and patient_history_record.last_pap_smear_chk or False
            last_pap_smear_remarks = patient_history_record and patient_history_record.last_pap_smear_remarks or ''
        return {'value': {'hbv_infection_chk': hbv_infection,
                          'hbv_infection_remarks': hbv_infection_remarks,
                          'dm_chk': dm_chk,
                          'dm_remarks': dm_remarks,
                          'ihd_chk': ihd_chk,
                          'ihd_remarks': ihd_remarks,
                          'cold_chk': cold_chk,
                          'cold_remarks': cold_remarks,
                          'hypertension_chk': hypertension_chk,
                          'hypertension_remarks': hypertension_remarks,
                          'surgery_chk': surgery_chk,
                          'surgery_remarks': surgery_remarks,
                          'others_past_illness': others_past_illness,
                          'nsaids_chk': nsaids_chk,
                          'nsaids_remarks': nsaids_remarks,
                          'aspirin_chk': aspirin_chk,
                          'aspirin_remarks': aspirin_remarks,
                          'laxative_chk': laxative_chk,
                          'laxative_remarks': laxative_remarks,
                          'others_drugs': others_drugs,
                          'lmp_chk': lmp_chk,
                          'lmp_dt': lmp_dt,
                          'menorrhagia_chk': menorrhagia_chk,
                          'menorrhagia_remarks': menorrhagia_remarks,
                          'dysmenorrhoea_chk': dysmenorrhoea_chk,
                          'dysmenorrhoea_remarks': dysmenorrhoea_remarks,
                          'bleeding_pv_chk': bleeding_pv_chk,
                          'bleeding_pv_remarks': bleeding_pv_remarks,
                          'last_pap_smear_chk': last_pap_smear_chk,
                          'last_pap_smear_remarks': last_pap_smear_remarks,
                          }
                }


# Inheriting Walkin module to add fields to record patient medical histories
class OeHealthAppointmentWalkin(models.Model):
    _inherit='oeh.medical.appointment.register.walkin'

    hbv_infection_chk = fields.Boolean(string='HBV Infection', readonly=True,states={'Scheduled': [('readonly', False)]})
    hbv_infection_remarks = fields.Text(string='HBV Infection Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    dm_chk = fields.Boolean(string='DM', readonly=True,states={'Scheduled': [('readonly', False)]})
    dm_remarks = fields.Text(string='DM Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    ihd_chk = fields.Boolean(string='IHD', readonly=True,states={'Scheduled': [('readonly', False)]})
    ihd_remarks = fields.Text(string='IHD Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    cold_chk = fields.Boolean(string='Cold', readonly=True,states={'Scheduled': [('readonly', False)]})
    cold_remarks = fields.Text(string='Cold Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    hypertension_chk = fields.Boolean(string='Hypertension', readonly=True,states={'Scheduled': [('readonly', False)]})
    hypertension_remarks = fields.Text(string='Hypertension Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    surgery_chk = fields.Boolean(string='Surgery', readonly=True,states={'Scheduled': [('readonly', False)]})
    surgery_remarks = fields.Text(string='Surgery Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    others_past_illness = fields.Text(string='Others Past Illness', readonly=True,states={'Scheduled': [('readonly', False)]})
    nsaids_chk = fields.Boolean(string='Nsaids', readonly=True,states={'Scheduled': [('readonly', False)]})
    nsaids_remarks = fields.Text(string='Nsaids Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    aspirin_chk = fields.Boolean(string='Aspirin', readonly=True,states={'Scheduled': [('readonly', False)]})
    aspirin_remarks = fields.Text(string='Aspirin Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    laxative_chk = fields.Boolean(string='Laxative', readonly=True,states={'Scheduled': [('readonly', False)]})
    laxative_remarks = fields.Text(string='Laxative Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    others_drugs = fields.Text(string='Others Drugs', readonly=True,states={'Scheduled': [('readonly', False)]})
    lmp_chk = fields.Boolean(string='LMP', readonly=True,states={'Scheduled': [('readonly', False)]})
    lmp_dt = fields.Date(string='Date', readonly=True,states={'Scheduled': [('readonly', False)]})
    menorrhagia_chk = fields.Boolean(string='Menorrhagia', readonly=True,states={'Scheduled': [('readonly', False)]})
    menorrhagia_remarks = fields.Text(string='Menorrhagia Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    dysmenorrhoea_chk = fields.Boolean(string='Dysmenorrhoea', readonly=True,states={'Scheduled': [('readonly', False)]})
    dysmenorrhoea_remarks = fields.Text(string='Dysmenorrhoea Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    bleeding_pv_chk = fields.Boolean(string='Bleeding PV', readonly=True,states={'Scheduled': [('readonly', False)]})
    bleeding_pv_remarks = fields.Text(string='Bleeding PV Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})
    last_pap_smear_chk = fields.Boolean(string='Last PAP smear', readonly=True,states={'Scheduled': [('readonly', False)]})
    last_pap_smear_remarks = fields.Text(string='Last PAP smear Remarks', readonly=True,states={'Scheduled': [('readonly', False)]})


    @api.multi
    def onchange_patient(self, patient):
        if patient:
            patient = self.env['oeh.medical.patient'].browse(patient)
            return {'value': {'dob': patient.dob,
                              'sex': patient.sex,
                              'marital_status': patient.marital_status,
                              'blood_type': patient.blood_type,
                              'rh': patient.rh,
                              'hbv_infection_chk': patient.hbv_infection_chk,
                              'hbv_infection_remarks': patient.hbv_infection_remarks,
                              'dm_chk': patient.dm_chk,
                              'dm_remarks': patient.dm_remarks,
                              'ihd_chk': patient.ihd_chk,
                              'ihd_remarks': patient.ihd_remarks,
                              'cold_chk': patient.cold_chk,
                              'cold_remarks': patient.cold_remarks,
                              'hypertension_chk': patient.hypertension_chk,
                              'hypertension_remarks': patient.hypertension_remarks,
                              'surgery_chk': patient.surgery_chk,
                              'surgery_remarks': patient.surgery_remarks,
                              'others_past_illness': patient.others_past_illness,
                              'nsaids_chk': patient.nsaids_chk,
                              'nsaids_remarks': patient.nsaids_remarks,
                              'aspirin_chk': patient.aspirin_chk,
                              'aspirin_remarks': patient.aspirin_remarks,
                              'laxative_chk': patient.laxative_chk,
                              'laxative_remarks': patient.laxative_remarks,
                              'others_drugs': patient.others_drugs,
                              'lmp_chk': patient.lmp_chk,
                              'lmp_dt': patient.lmp_dt,
                              'menorrhagia_chk': patient.menorrhagia_chk,
                              'menorrhagia_remarks': patient.menorrhagia_remarks,
                              'dysmenorrhoea_chk': patient.dysmenorrhoea_chk,
                              'dysmenorrhoea_remarks': patient.dysmenorrhoea_remarks,
                              'bleeding_pv_chk': patient.bleeding_pv_chk,
                              'bleeding_pv_remarks': patient.bleeding_pv_remarks,
                              'last_pap_smear_chk': patient.last_pap_smear_chk,
                              'last_pap_smear_remarks': patient.last_pap_smear_remarks}}
        return {}