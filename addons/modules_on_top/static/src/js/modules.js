openerp.modules_on_top = function (session) {
    var _t = session.web._t,
       _lt = session.web._lt;

    var QWeb = session.web.qweb;

    session.web.ModulesMenu = session.web.Widget.extend({
        template:'modules_on_top.ModulesMenu',

        start: function () {
            var self = this;
            this._super.apply(this, arguments);

            this.$el.on('click', '.oe_dropdown_menu li a[data-menu]', function(ev) {
                ev.preventDefault();
                var f = self['on_menu_' + $(this).data('menu')];
                if (f) {
                    f($(this));
                }
            });
        },

        on_menu_update: function() {
            new session.web.Model("res.users").call("update_modules_list", []).then(function(res) {
                session.client.action_manager.do_action(res);
            });
            /*alert('update');*/
        },

        on_menu_modules_list: function() {
            var action = {
                    type: 'ir.actions.act_window',
                    res_model: 'res.users',
                    res_id: this.session.uid,
                    view_mode: 'form',
                    view_type: 'form',
                    views: [[false, 'form']],
                    target: 'new',
                    context: {
                        'form_view_ref': 'modules_on_top.view_users_modules_list_form'
                    }
            };
            session.client.action_manager.do_action(action);
        }
    }),



    session.web.UserMenu.include({
        do_update: function(){
            var self = this;
            this._super.apply(this, arguments);
            this.update_promise.then(function() {
                var modules_button = new session.web.ModulesMenu();
                modules_button.appendTo(session.webclient.$el.find('.oe_systray'));
            });
        }
    });





}
