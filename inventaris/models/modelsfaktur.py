from odoo import models, fields, api, _

class inventaris(models.Model):
        _name = 'inventaris.faktur'
        _description = 'Faktur Records '
        _inherit = ['mail.thread', 'mail.activity.mixin']

        name = fields.Char(string='Name', required=True, tracking=True)
        harga = fields.Integer(string='Total Harga (Dalam Rp.)',tracking=True)
        supplier = fields.Text(string="Supplier", tracking=True)
        tanggal = fields.Datetime(string="Tanggal Pembuatan Struk", tracking=True)
        # capitalized_name = fields.Char(string='Capitalized Name', compute='_compute_capitalized_name', store=True)
        ref = fields.Char(string="Code Inventaris", default=lambda self:_('Faktur - Konstruksi'))
        inventaris_ids = fields.One2many('inventaris.inventaris', 'faktur_id', string='Inventaris', tracking=True)
        lokasi_id = fields.Many2one('inventaris.lokasi', string='ID Inventaris')
        lokasi_alamat = fields.Text(string='Alamat', related='lokasi_id.alamat', tracking=True)
        inventaris_bahan = fields.Text(string='Nama Bahan', compute='_compute_inventaris_bahan', tracking=True)
        ref = fields.Char(string="Code Faktur", default=lambda self: _('Faktur Konstruksi'))
        inventaris_ref = fields.Text(string='Code Inventaris', compute='_compute_inventaris_ref', tracking=True)
        inventaris_notes = fields.Text(string='Keterangan', compute='_compute_inventaris_notes', tracking=True)

        @api.model_create_multi
        def create(self, vals_list):
                for vals in vals_list:
                    vals['ref'] = self.env['ir.sequence'].next_by_code('faktur.konstruksi')
                return super(inventaris, self).create(vals_list)

        @api.depends('inventaris_ids.ref')
        def _compute_inventaris_ref(self):
                for record in self:
                        record.inventaris_ref = ', '.join([inventaris.ref for inventaris in record.inventaris_ids])

        @api.depends('inventaris_ids.notes')
        def _compute_inventaris_notes(self):
                for record in self:
                        record.inventaris_notes = ', '.join([inventaris.notes for inventaris in record.inventaris_ids])

        @api.depends('inventaris_ids.name')
        def _compute_inventaris_bahan(self):
                for record in self:
                        record.inventaris_bahan = ', '.join([inventaris.name for inventaris in record.inventaris_ids])

        # @api.depends('name')
        # def _compute_capitalized_name(self):
        #         for rec in self:
        #                 if rec.name:
        #                         rec.capitalized_name = rec.name.upper()
        #                 else:
        #                         rec.capitalized_name = ''




