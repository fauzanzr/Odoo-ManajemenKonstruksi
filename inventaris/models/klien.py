from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class inventaris(models.Model):
    _name = "manajemen_proyek.klien"
    _rec_name = "nama"
    _inherit = 'mail.thread'
    _description = "Pengelolaan Data Klien"

    nama = fields.Char(string="Nama", required=True, tracking=True)
    jenisKelamin = fields.Selection(
        [('laki-laki', 'Laki-Laki'), ('perempuan', 'Perempuan')], string="Jenis Kelamin", required=True, tracking=True)
    perusahaan = fields.Char(string="Nama Perusahaan", tracking=True)
    alamat = fields.Char(string="Alamat", required=True, tracking=True)
    telepon = fields.Char(string="Telepon", required=True, tracking=True)
    email = fields.Char(string="Email", required=True, tracking=True)
    ref = fields.Char(string="Referensi", default=lambda self: _('New'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code(
                'manajemen_proyek.klien')
            return super(inventaris, self).create(vals_list)
