from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class inventaris(models.Model):
    _name = "manajemen_proyek.jobdesk"
    _rec_name = "nama"
    _inherit = 'mail.thread'
    _description = "Pengelolaan Jobdesk Perusahaan"

    nama = fields.Char(string="Nama", required=True, tracking=True)
    deskripsi = fields.Text(string="Deskripsi", required=True, tracking=True)
    ref = fields.Char(string="Referensi", default=lambda self: _('New'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code(
                'manajemen_proyek.jobdesk')
            return super(inventaris, self).create(vals_list)