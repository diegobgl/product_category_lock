from odoo import models, api, exceptions, _

class ProductCategory(models.Model):
    _inherit = 'product.category'

    @api.model
    def create(self, vals):
        """Permitir crear categorías nuevas."""
        return super(ProductCategory, self).create(vals)

    def write(self, vals):
        """Bloquear cambios en las categorías existentes."""
        raise exceptions.UserError(_('No se permite modificar las categorías de producto.'))

    def unlink(self):
        """Bloquear la eliminación de categorías existentes."""
        raise exceptions.UserError(_('No se permite eliminar categorías de producto.'))
