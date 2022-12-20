from odoo import fields, models, api
from datetime import *


class Nhapgio(models.Model):
    _name = 'chamcong.nhapgio'
    _description = 'Nhập giờ làm'
    _rec_name = 'ngaynhap'

    description = fields.Text(string="Ghi chú")
    teams = fields.Many2one(comodel_name="chamcong.teams", string="Tổ/đội")
    nhanviens = fields.Many2one(comodel_name="chamcong.nhanviens", inverse_name="teams_id", string="Nhân viên",
                                   domain="[('teams_id', '=?', teams)]")

    @api.onchange('teams')
    def _onchange_teams_id(self):
        if self.teams and self.teams != self.nhanviens.teams_id:
            self.nhanviens = False

    @api.onchange('nhanviens')
    def _onchange_nhanviens_id(self):
        if self.nhanviens.teams_id:
            self.teams = self.nhanviens.teams_id


    ngaynhap = fields.Datetime(string='Ngày nhập', default=datetime.today())
    sogio = fields.Float(string='Giờ công', default=8.5)
