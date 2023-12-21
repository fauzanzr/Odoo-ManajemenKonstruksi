from odoo import models, fields, api


class inventaris(models.Model):
    _name = 'biaya.models'
    _description = 'biaya models'

    id_laporan = fields.Integer(string='Id_Laporan', required=True)
    ringkasan_biaya = fields.Char(string="Ringkasan Biaya", required=True)
    jumlah_total_biaya = fields.Integer(string="Jumlah Total Biaya", required=True)
    catatan = fields.Char(string='Catatan', required=True)