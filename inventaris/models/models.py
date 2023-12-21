from odoo import models, fields, api, _

class inventaris(models.Model):
        _name = 'inventaris.inventaris'
        _description = 'Inventory Records '
        _inherit = 'mail.thread'

        name = fields.Char(string='Nama Bahan', required=True, tracking=True)
        Kuantitas = fields.Float(string='Jumlah dalam Kg', tracking=True)
        Kuantitas2 = fields.Float(string='Jumlah dalam Gram', compute='_hitung_gram', tracking=True)
        # lokasi = fields.Char(string='Lokasi Awal Bahan', tracking=True)
        notes = fields.Text(string="Keterangan")
        tanggal = fields.Datetime(string="Tanggal Kedatangan Bahan", tracking=True)
        capitalized_name = fields.Char(string='Capitalized Name', compute='_compute_capitalized_name', store=True)
        ref = fields.Char(string="Code Inventaris", default=lambda self:_('Bahan Konstruksi'))
        faktur_id = fields.Many2one('inventaris.faktur', string='Faktur')


        @api.model_create_multi
        def create(self, vals_list):
                for vals in vals_list:
                    vals['ref'] = self.env['ir.sequence'].next_by_code('bahan.konstruksi')
                return super(inventaris, self).create(vals_list)

        @api.depends('name')
        def _compute_capitalized_name(self):
                for rec in self:
                        if rec.name:
                                rec.capitalized_name = rec.name.upper()
                        else:
                                rec.capitalized_name = ''

        @api.depends('Kuantitas')
        def _hitung_gram(self):
                for record in self:
                        record.Kuantitas2 = record.Kuantitas * 1000




