from openerp.osv import osv, fields


class module_module(osv.osv):
    _name = 'ir.module.module'
    _inherit = 'ir.module.module'
    _columns = {
        'developer_id': fields.many2many('res.users', string="Developer"),
    }


class res_users(osv.osv):
    _name = "res.users"
    _inherit = "res.users"
    _columns = {
        'modules_to_update_ids': fields.many2many('ir.module.module', 'developer_id', string="Modules to update"),
    }

    def save_modules_list(self, cr, uid, ids, context=None):
        pass

    def update_modules_list(self, cr, uid, context=None):
        res = False
        user = self.browse(cr, uid, uid, context=context)

        if user and user.modules_to_update_ids:
            ids = [x.id for x in user.modules_to_update_ids]
            res = self.pool.get('ir.module.module').button_immediate_upgrade(cr, uid, ids, context=context)
        return res
