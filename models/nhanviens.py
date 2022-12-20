from odoo import fields, models, api
from datetime import date


class Nhanviens(models.Model):
    _name = 'chamcong.nhanviens'
    _description = 'Thông tin nhân viên'

    name = fields.Char(string="Tên nhân viên", required="1")
    description = fields.Text(string="Ghi chú")
    dod = fields.Date(string="Năm sinh", required="1", default=date.today())
    phone = fields.Char(string="Số điện thoại", required=True)
    teams_id = fields.Many2one(comodel_name="chamcong.teams", string="Tổ/đội")
    state = fields.Selection(selection=[('onboard', 'Hoạt động'), ('leave', 'Tạm ngưng')], string='Trạng thái',
                             default='onboard')
    gender = fields.Selection(selection=[('1', 'Nam'), ('0', 'Nữ'), ('-1', 'Khác')], string='Giới tính', default='0')
    married = fields.Boolean(string='Hôn nhân', default=True)
    image_1920 = fields.Image(string="Ảnh đại diện")
    image_128 = fields.Image(string="Image 128", related="image_1920", max_width=128, max_height=128, store=True)