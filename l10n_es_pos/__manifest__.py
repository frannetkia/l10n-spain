# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Punto de venta adaptado a la legislación española",
    "category": "Sales/Point Of Sale",
    "author": "Tecnativa, "
    "Aselcis Consulting, "
    "Acysos S.L., "
    "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-spain",
    "license": "AGPL-3",
    "version": "14.0.2.1.0",
    "depends": ["point_of_sale"],
    "data": ["views/pos_templates.xml", "views/pos_views.xml"],
    "qweb": [
        "static/src/xml/pos.xml",
        "static/src/xml/Screens/OrderManagementScreen/OrderRow.xml",
        "static/src/xml/Screens/OrderManagementScreen/OrderList.xml",
    ],
    "installable": True,
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
}
