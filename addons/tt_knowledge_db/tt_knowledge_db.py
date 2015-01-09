#coding: utf-8
from osv import osv, fields

class document_page_tag(osv.osv):
    def _get_my_id(self, cr, uid, ids, context=None):
        return ids

    def _get_tag_ids(self, cr, uid, ids, context=None):
        res = []
        page_obj = self.pool.get('document.page')
        for page in page_obj.read(cr, uid, ids, context=context):
            tag_ids = page.get('tag_ids')
            if tag_ids:
                res.extend(tag_ids)
        return res

    def _popularity_count(self, cr, uid, ids, name, args, context=None):
        res = {}
        for tag in self.browse(cr, uid, ids, context=context):
            res[tag.id] = len(tag.page_ids) if tag.page_ids else 0
        return res

    _name = 'document.page.tag'
    _order = 'popularity desc,name'
    _columns = {
        'name': fields.char('Name', size=50, required=True),
        'popularity': fields.function(_popularity_count, type='integer', string='Popularity',
                                      store={
                                          'document.page': (_get_tag_ids, ['tag_ids'], 10),
                                          'document.page.tag': (_get_my_id, ['page_ids'], 10)
                                      }),
        'page_ids': fields.many2many('document.page', rel='document_page_tag_rel', id1='tag_id', id2='page_id',
                                              domain=[('type', '=', 'content')], string='Pages'),
    }

class document_page(osv.osv):
    _inherit = 'document.page'

    _columns = {
        'tag_ids': fields.many2many('document.page.tag', rel='document_page_tag_rel', id1='page_id', id2='tag_id',
                                 string='Tags'),
    }