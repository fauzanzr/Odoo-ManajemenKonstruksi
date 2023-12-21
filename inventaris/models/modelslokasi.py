from odoo import models, fields, api, _

class inventaris(models.Model):
        _name = 'inventaris.lokasi'
        _description = 'lokasi Records '
        _inherit = 'mail.thread'

        # name = fields.Char(string='Code', required=True, tracking=True)
        alamat = fields.Text(string="Alamat Inventaris", tracking=True)
        notes = fields.Text(string="Keterangan Tempat", tracking=True)
        # capitalized_name = fields.Char(string='Capitalized Name', compute='_compute_capitalized_name', store=True)
        ref = fields.Char(string="Code Inventaris", default=lambda self:_('Alamat - Konstruksi'))
        faktur_ids = fields.One2many('inventaris.faktur', 'lokasi_id', string='Faktur')

        @api.model_create_multi
        def create(self, vals_list):
                for vals in vals_list:
                    vals['ref'] = self.env['ir.sequence'].next_by_code('alamat.konstruksi')
                return super(inventaris, self).create(vals_list)

        # @api.depends('name')
        # def _compute_capitalized_name(self):
        #         for rec in self:
        #                 if rec.name:
        #                         rec.capitalized_name = rec.name.upper()
        #                 else:
        #                         rec.capitalized_name = ''




