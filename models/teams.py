from odoo import fields, models, api


class Teams(models.Model):
    _name = 'chamcong.teams'
    _description = 'Thông tin tổ đội'

    name = fields.Char(string="Tên tổ/đội", required=True)
    description = fields.Text(string="Ghi chú")
    nhanviens_id = fields.One2many(comodel_name="chamcong.nhanviens", inverse_name="teams_id", string="Nhân viên")
    # nếu thêm store = "True" thì nó sẽ lưu và db, để cập nhật thay đổi thì dùng api depend
    nhanviens_count = fields.Integer(string="Số lượng", compute="_get_nhanviens_count", store="True")

    @api.depends("nhanviens_id")
    def _get_nhanviens_count(self):
        for Teams in self:
            Teams.nhanviens_count = len(self.nhanviens_id)

    state = fields.Selection(selection=[('onboard', 'Hoạt động'), ('leave', 'Tạm ngưng')], string='Trạng thái',
                             default='onboard')
