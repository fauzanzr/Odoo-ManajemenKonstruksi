from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class inventaris(models.Model):
    _name = "manajemen_proyek.manajproyek"
    _rec_name = "namaKontruksi"
    _inherit = 'mail.thread'
    _description = "Pengelolaan proyek perusahaan"

    namaKontruksi = fields.Char(
        string="Nama Kontruksi", required=True, tracking=True)
    jenisKontruksi = fields.Char(
        string="Jenis Kontruksi", required=True, tracking=True)
    namaKlien_id = fields.Many2one('manajemen_proyek.klien', string="Nama Klien", required=True, tracking=True)
    tglMulai = fields.Date(string="Tanggal Mulai",
                           required=True, tracking=True)
    tglSelesai = fields.Date(string="Tanggal Selesai",
                             required=True, tracking=True)
    namaJobdesk_id = fields.Many2many('manajemen_proyek.jobdesk', string="Nama Jobdesk",
                              required=True, tracking=True)
    catatan = fields.Text(string="Catatan", required=True, tracking=True)
    ref = fields.Char(string="Referensi", default=lambda self: _('New'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code(
                'manajemen_proyek.manajproyek')
            return super(inventaris, self).create(vals_list)
