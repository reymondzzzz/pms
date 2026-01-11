# Copyright 2025 NN
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PmsRoomTypeImage(models.Model):
    """Additional images for room types (gallery)"""

    _name = "pms.room.type.image"
    _description = "Room Type Image"
    _inherit = ["image.mixin"]
    _order = "sequence, id"

    name = fields.Char(
        string="Name",
        required=True,
        help="Image title/name",
    )
    sequence = fields.Integer(
        default=10,
        help="Order of the image in the gallery",
    )
    image_1920 = fields.Image()
    room_type_id = fields.Many2one(
        string="Room Type",
        comodel_name="pms.room.type",
        ondelete="cascade",
        index=True,
        required=True,
    )
