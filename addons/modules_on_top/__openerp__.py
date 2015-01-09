# coding: utf-8
{
    'name': 'Modules menu on system tray',
    'version': '1.1',
    'author': 'TT',
    'category': 'Crediting',
    'description': """
        This module adds button in system tray. This button display a new popup window with modules list.
    """,
    'depends': ['web'],
    'data': ['modules_on_top_view.xml'],
    'js': ['static/src/js/modules.js'],
    'qweb': ['static/src/xml/modules.xml'],
    'installable': True,
    'auto_install': False,
}
