# -*- coding: utf-8 -*-
{
    'name': "Construction management",
    'summary': """
        melacak inventaris bahan dan perlatan untuk kontruksi termasuk pengelolaan bahan""",

    'description': """Modul ini digunakan untuk mengintegrasikan semua proses bisnis yang ada di PT. Garuda Nusantara Construction, mulai dari manajemen pelaporan, analisis biaya, pengelolaan bahan dan lain sebagainya.""",
    'author': "Kelompok3_SIB3D",
    'website': "",
    'category': 'Construction',
    'sequence': -100,
    'version': '1.0.0',
    'depends': ['base', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'report/report.xml',
        'report/inventaris_card.xml',
        'views/faktur.xml',
        'views/lokasi.xml',
        'views/templates.xml',
        'views/biaya.xml',
        'views/jobdesk.xml',
        'views/manajemenProyek.xml',
        'views/klien.xml',
        'views/resiko2.xml',
        'data/sequence.xml',
        'data/sequence_1.xml',
        'data/sequence_2.xml',
    ],
    'demo': [
        'views/views.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
