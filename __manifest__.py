{
    'name': 'Chấm công test',
    'version': '1.0',
    'summary': 'Thực tập',
    'description': 'Chấm công nhân viên',
    'category': 'Other',
    'author': 'Team odoo Biên hòa',
    'sequence': 1,
    'website': 'https://hunglq16286.github.io/github/',
    'depends': [],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/teams_view.xml',
        'views/nhanviens_view.xml',
        'views/nhapgio_view.xml',
    ],
    'application': True
}