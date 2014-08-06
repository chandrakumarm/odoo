from openerp.osv import fields, osv

class card_register(osv.osv_memory):
    _name = 'card.register'
    _description = 'Card Registration'
    
    _columns = {
        'card_number': fields.char('Card Number'),
    }

    def action_register(self, cr, uid, ids, context=None):
        active_model = context.get('active_model')
        active_ids = context.get('active_ids')
        obj = self.browse(cr, uid, ids[0] ,context)
        self.pool.get(active_model).write(cr, uid, active_ids, {'card_no': obj.card_number})
        return True
             
card_register()