var slotsProxy = {
    type: 'direct',
    api: {
        read: Remote.CMSRouter.getSlots
    },

    reader: {
        root: 'items',
        successProperty: 'success',
        totalProperty: 'total'
    }
};

Ext.define('VideoID.view.content.CMSBlockContextPanel', {
    extend: 'Ext.panel.Panel',
    frame: true,
    title: 'Zawartość',

    _createRecordPanel: function (parent, items, notlast) {
        var panel = Ext.create('Ext.panel.Panel', {
            frame: true,
            items: items
        });

        var button = Ext.create('Ext.button.Button', {
            text: 'usuń',
            handler: function () {
                parent.remove(panel);
            }
        });

        panel.items.add(button);

        if (notlast) {
            parent.insert(parent.items.length - 1, panel);
        } else {
            parent.add(panel);
        }

        return panel;
    },

    initComponent: function () {
        var i, j, item, match, button, fields,
            group, groupParent, parent,
            items = [],
            me = this;

        this.fields = JSON.parse(this.fields);

        for (i in this.fields) {
            item = this.fields[i];
            items.push(item);
        }

        // for (i = 0; i < this.list_fields.length; i++) {
        //     // Rodzic dla grup
        //     group = this.list_fields[i];
        //     fields = group['fields'];
        //     groupParent = Ext.create('Ext.panel.Panel', {
        //         title: group['label'],
        //         frame: true
        //     });
        //     for (j = 0; j < fields.length; j++) {
        //         this._createRecordPanel(groupParent, JSON.parse(fields[j]));
        //     }

        //     // Dodaj nowe pola
        //     button = Ext.create('Ext.button.Button', {
        //         text: 'dodaj',
        //         handler: function(groupName, n, groupParent, fieldTemplates) {
        //             return function () {
        //                 var items = [];
        //                 n += 1;
        //                 for (j = 0; j < fieldTemplates.length; j++) {
        //                     var field = JSON.parse(fieldTemplates[j][1]),
        //                         name = 'context__' + groupName + '__' + n + '__' + fieldTemplates[j][0];
        //                     field.name = name;
        //                     items.push(field);
        //                 }
        //                 me._createRecordPanel(groupParent, items, true);
        //             };
        //         }(group['name'], fields.length, groupParent, group['template_fields'])
        //     });
        //     groupParent.items.add(button);
        //     items.push(groupParent);
        // }


        Ext.apply(this, {
            items: items
        });
        this.callParent(arguments);
    }
});

Ext.define('VideoID.view.content.CMSBlockForm', {
    extend: 'VideoID.view.content.GenericEditCMSBlock',
    xtype: 'cmsblockform',
    name: 'CMSBlockForm',
    id: 'cmsblockform-id',

    initComponent: function () {
        var me = this;

        Ext.direct.Manager.addProvider({
            "type":"remoting",
            "url":"/extadmin/extdirect/CMSRouter/",
            "actions":{
                "CMSRouter":[{
                    "name":"getContextFields",
                    "formHandler": false,
                    "len": 1
                }]
            },
            "namespace":"Remote"
        });

        this.callParent(arguments);

        var templateField = this.templateField = this.getForm().getFields().findBy(function (field) {
            return field.name == 'template';
        });
        templateField.on('change', Ext.bind(this._onTemplateFieldChange, this));
        this.disableTemplateChanges();

        this.slotField = this.getForm().getFields().findBy(function (field) {
            return field.name == 'slot';
        });
        this._initSlotStore();

        this.vidnodeField = this.getForm().getFields().findBy(function (field) {
            return field.name == 'vidnode';
        });
        this.vidnodeField.on('change', Ext.bind(this._onVIDNodeFieldChange, this));
    },

    _initSlotStore: function () {
        this._slotStore = Ext.create('Ext.data.Store', {
            fields: ['name'],
            proxy: slotsProxy
        });
        Ext.apply(this.slotField, {
            store: this._slotStore,
            valueField: 'name'
        });
    },

    loadRecord: function (record) {
        var me = this;

        Remote.CMSRouter.getContextFields({'cmsblock_id': record.data.pk}, function(data){
            if (data['success']) {
                me.initContextPanel(data);
            }
        });
        return this.callParent(arguments);
    },

    initContextPanel: function (data) {
        var me = this;

        data = data || {};
        if (this._subform) {
            this.items.items[0].remove(this._subform);
        }

        this._subform = Ext.create('VideoID.view.content.CMSBlockContextPanel', {
            fields: data['fields'] || '[]',
            list_fields: data['list_fields'] || []
        });
        this.items.items[0].add(this._subform);
    },

    enableTemplateChanges: function () {
        this._templateFieldChangeTrigger = true;
        this.templateField.enable();
    },

    disableTemplateChanges: function () {
        this._templateFieldChangeTrigger = false;
        this.templateField.disable();
    },

    _onTemplateFieldChange: function (field, newValue, oldValue, options) {
        var me = this;

        if (!this._templateFieldChangeTrigger) {
            return;
        }

        if (newValue == null) {
            this.initContextPanel();
            return;
        }

        Remote.CMSRouter.getContextFields({'template': newValue }, function (data) {
            if (data['success']) {
                me.initContextPanel(data);
            }
        });
    },

    _onVIDNodeFieldChange: function (field, newValue, oldValue, options) {
        var me = this;

        if (newValue && parseInt(newValue)) {
            this._slotStore.load({
                params: { vidnodeId: newValue },
                callback: function (records, operation, success) {
                    // Zaznaczanie poprzednio zaznaczonego slotu jeśli takowy
                    // dalej istnieje, jeśli nie to ustawianie pierwszego możliwego
                    var i, r = null, current = me.slotField.value;
                    if (records && current) {
                        for (i = 0; i < records.length; i++) {
                            if (records[i].data.name == current) {
                                me.slotField.select(current);
                                return;
                            }
                        }
                    }
                    if (records && records[0]) {
                        me.slotField.select(records[0].data.name);
                    } else {
                        me.slotField.select('');
                    }
                }
            });
        } else {
            this._slotStore.removeAll();
        }
    },

    getForm: function () {
        // Hack hack hack - this.callParent w form.getValues nie działa - temu tak a nie inaczej
        var form = this.callParent(arguments),
            getValues = form.getValues,
            me = this;

        form.getValues = function () {
            var pattern,
                values = getValues.apply(form, arguments);
            values.contextWrapper = {};
            for (k in values) {
                if (values.hasOwnProperty(k)) {
                    if ((/context__/).exec(k)) {
                        values.contextWrapper[k] = values[k];
                    }
                }
            }
            return values;
        };

        return form;
    }
});
