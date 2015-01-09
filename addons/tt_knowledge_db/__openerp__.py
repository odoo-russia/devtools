{
    'name': 'Knowledge Database',
    'version': '1.0',
    'category': 'Knowledge Management',
    'author': 'Transparent Technologies',
    'license': 'AGPL-3',
    'depends': ['base', 'document_page'],
    'data': [
        'tt_knowledge_db_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'description': '''
    The module adds tags and some usability improvement to the "document_page" module.
    '''
}