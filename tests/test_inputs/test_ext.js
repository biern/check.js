Ext.define('VideoID.view.administration.GroupVIDNodeTree', {
    extend: 'Ext.tree.Panel',
    xtype: 'groupvidnodetree',
    rootVisible:false,
    requires: [
        'VideoID.lib.treecheckcolumn'
    ],

    plugins: [
        Ext.create('Ext.grid.plugin.CellEditing', {
            clicksToEdit: 1
        })
    ],

    columns: [{
        xtype: 'treecolumn',
        text: _('Nazwa strony'),
        dataIndex: 'name',
        flex: 1
    }, {
        xtype: 'treecheckcolumn',
        text: _('V'),
        dataIndex: 'perm-view',
        width: 40
    }, {
        xtype: 'treecheckcolumn',
        text: _('P'),
        dataIndex: 'perm-publish',
        width: 40
    }, {
        xtype: 'treecheckcolumn',
        text: _('E'),
        dataIndex: 'perm-edit',
        width: 40
    }, {
        xtype: 'treecheckcolumn',
        text: _('A'),
        dataIndex: 'perm-add',
        width: 40
    }, {
        xtype: 'treecheckcolumn',
        text: _('D'),
        dataIndex: 'perm-delete',
        width: 40
    }]
});


Ext.define('VideoID.view.administration.EditGroup', {
    extend:'VideoID.view.administration.GenericEditRBACGroup',
    alias: 'widget.editgroup',
    xtype: 'editgroup',
    id: 'edit-group',
    requires: [
        'Ext.toolbar.Toolbar',
        'Ext.data.TreeStore',
        'Ext.grid.plugin.CellEditing'
    ],
    width: 500,

    initComponent: function () {

        var treeview = Ext.create('VideoID.view.administration.GroupVIDNodeTree', {
            store: 'GroupVIDNodeTree',
            id: 'groupvidnodetree_id'
        });

        this.callParent(arguments);

        this.add({
            title:_('Uprawnienia'),
            expanded: true,
            items: [treeview]
        });
        
        Ext.direct.Manager.addProvider({
            "type":"remoting",
            "url":"/extadmin/extdirect/GroupRouter/",
            "actions":{
                "GroupRouter":[{
                    "name":"getPermissionsTree",
                    "len":1
                }]
            },
            "namespace":"Remote"
        });

    }
});
