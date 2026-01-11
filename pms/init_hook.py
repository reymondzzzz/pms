def pre_init_hook(env):
    """Odoo 19+ hook - receives env directly."""
    ResConfig = env["res.config.settings"]
    available_fields = ResConfig.fields_get()
    default_values = ResConfig.default_get(list(available_fields))

    # Only set pricelist fields that exist in this Odoo version
    pricelist_fields = {
        "group_product_pricelist": True,
        "group_sale_pricelist": True,  # May not exist in Odoo 19+
    }
    for field, value in pricelist_fields.items():
        if field in available_fields:
            default_values[field] = value

    ResConfig.sudo().create(default_values).execute()
    env["ir.config_parameter"].sudo().set_param(
        "product.product_pricelist_setting", "advanced"
    )
