from odoo import models, fields, api

class inventaris(models.Model):
    _name = "risk.risk"
    _description = "Resiko"

    idRisiko = fields.Integer(string="ID Risiko")
    namaRisiko = fields.Char(string="Nama Risiko")
    deskripsiRisiko = fields.Text(string="Deskripsi Risiko")
    dampakRisiko = fields.Text(string="Dampak Risiko")
    penyebabRisiko = fields.Text(string="Penyebab Risiko")

