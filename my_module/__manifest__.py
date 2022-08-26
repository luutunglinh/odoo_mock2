# -*- coding: utf-8 -*-
{
    'name': "My first module",  # Module title
    'summary': "Manage books easily",  # Module subtitle phrase
    'description': """
Manage Library
==============
Description related to library.
    """,  # Supports reStructuredText(RST) format
    'author': "Parth Gajjar",
    'website': "http://www.example.com",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['base','report_xlsx','hr'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/report_excel_wizard.xml',
        'data/data.xml',
        'views/vss_car.xml',
        'views/vss_parking.xml',
        'views/vss_menu.xml',
        'report/vss_paper.xml',
    ],

    # This demo data files will be loaded if db initialize with demo data (commented because file is not used in this example)
    # 'demo': [
    #     'data/demo.xml'
    # ],
}
