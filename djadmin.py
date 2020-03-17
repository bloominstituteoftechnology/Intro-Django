# -*- coding: utf-8 -*-

import six
from django.conf import settings
from django.contrib import admin
from django.contrib.admin.utils import model_format_dict
from django.db.models.fields import BLANK_CHOICE_DASH
from django.utils.timezone import template_localtime
from django.utils.translation import ugettext_lazy as _
from excel_response2 import ExcelResponse


if not hasattr(settings, 'DJANGO_ADMIN_DISABLE_DELETE_SELECTED') or settings.DJANGO_ADMIN_DISABLE_DELETE_SELECTED:
    admin.site.disable_action('delete_selected')


class AdvancedActionsModelAdmin(object):
    def get_action_choices(self, request, default_choices=BLANK_CHOICE_DASH):
        """
        Return a list of choices for use in a form object.  Each choice is a tuple (name, description).
        """
        actions_exclude = self.actions_exclude if hasattr(self, 'actions_exclude') else []
        choices = [] + default_choices
        for func, name, description in six.itervalues(self.get_actions(request)):
            if name in actions_exclude:
                continue
            choice = (name, description % model_format_dict(self.opts))
            choices.append(choice)
        return choices


class DeleteModelAdmin(object):
    actions = ['override_delete_selected']

    def override_delete_selected(modeladmin, request, queryset):
        for query in queryset:
            modeladmin.delete_model(request, query)

    override_delete_selected.short_description = _(u'Delete selected %(verbose_name_plural)s')


class ExportExcelModelAdmin(object):
    actions = ['export_excel']

    def export_excel(modeladmin, request, queryset):
        force_csv = (hasattr(settings, 'DJANGO_EXCEL_RESPONSE') and settings.DJANGO_EXCEL_RESPONSE) or (hasattr(modeladmin, 'force_csv') and modeladmin.force_csv)
        return ExcelResponse(queryset, output_name=modeladmin.model._meta.verbose_name_plural, force_csv=force_csv)

    export_excel.short_description = _(u'Export selected %(verbose_name_plural)s as Excel')


class AdvancedExportExcelModelAdmin(object):
    actions = ['advanced_export_excel']

    def excel_item(modeladmin, query, field):
        foo_field = 'get_{0}_display'.format(field)
        return unicode(getattr(query, foo_field)() if hasattr(query, foo_field) else template_localtime(getattr(query, field)))

    def excel_data(modeladmin, request, query, model_fields, has_extra_excel_fields):
        excel_item = [modeladmin.excel_item(query, field) for field in model_fields]
        return excel_item + list(modeladmin.add_extra_excel_fields(request, query)) if has_extra_excel_fields else excel_item

    def advanced_export_excel(modeladmin, request, queryset):
        has_excel_headers = hasattr(modeladmin, 'excel_headers')
        has_excel_headers_mapping = hasattr(modeladmin, 'excel_headers_mapping')
        has_excel_fields = hasattr(modeladmin, 'excel_fields')
        has_excel_fields_exclude = hasattr(modeladmin, 'excel_fields_exclude')
        has_extra_excel_fields = hasattr(modeladmin, 'extra_excel_fields')  # Add by call add_extra_excel_fields

        model_fields = list(modeladmin.excel_fields) if has_excel_fields else [f.name for f in modeladmin.model._meta.fields]
        if has_excel_fields_exclude:
            model_fields = [field for field in model_fields if field not in set(modeladmin.excel_fields_exclude)]

        excel_headers = modeladmin.excel_headers if has_excel_headers else (model_fields + list(modeladmin.extra_excel_fields) if has_extra_excel_fields else model_fields)
        excel_headers = [(modeladmin.excel_headers_mapping.get(header) or header) for header in excel_headers] if has_excel_headers_mapping else excel_headers

        excel_data = [excel_headers]
        excel_data += [modeladmin.excel_data(request, query, model_fields, has_extra_excel_fields) for query in queryset]

        force_csv = (hasattr(settings, 'DJANGO_EXCEL_RESPONSE') and settings.DJANGO_EXCEL_RESPONSE) or (hasattr(modeladmin, 'force_csv') and modeladmin.force_csv)

        return ExcelResponse(excel_data, output_name=modeladmin.model._meta.verbose_name_plural, force_csv=force_csv)

    advanced_export_excel.short_description = _(u'Advanced Export selected %(verbose_name_plural)s as Excel')


class ReadonlyModelAdmin(object):
    """ Readonly for Update. """
    def get_readonly_fields(self, request, obj=None):
        if not hasattr(self, 'readonly_fields_exclude'):
            self.readonly_fields_exclude = ()
        if obj:  # editing an existing object
            return tuple(set(self.readonly_fields) | set(f.name for f in self.model._meta.fields) - set(self.readonly_fields_exclude))
        return tuple(set(self.readonly_fields) - set(self.readonly_fields_exclude))


class Readonly2ModelAdmin(object):
    """ Readonly for Add/Update. """
    def get_readonly_fields(self, request, obj=None):
        if not hasattr(self, 'readonly_fields_exclude'):
            self.readonly_fields_exclude = ()
        return tuple(set(self.readonly_fields) | set(f.name for f in self.model._meta.fields) - set(self.readonly_fields_exclude))


class ReadOnlyModelAdmin(ReadonlyModelAdmin):
    """ Disables all editing capabilities. """
    change_form_template = 'admin/readonly_form.html'

    def __init__(self, *args, **kwargs):
        super(ReadOnlyModelAdmin, self).__init__(*args, **kwargs)

    def get_actions(self, request):
        actions = super(ReadOnlyModelAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass

    def delete_model(self, request, obj):
        pass

    def save_related(self, request, form, formsets, change):
        pass


class ChangeOnlyModelAdmin(object):
    """ Disables add/delete capabilities. """
    def get_actions(self, request):
        actions = super(ChangeOnlyModelAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def delete_model(self, request, obj):
        pass


class DeleteonlyModelAdmin(object):
    """ Disables add/change capabilities. """
    change_form_template = 'admin/deleteonly_form.html'

    def has_add_permission(self, request):
        return False


class DeleteOnlyModelAdmin(ReadonlyModelAdmin, DeleteonlyModelAdmin):
    """ Disables add/change capabilities, fields readonly. """


class AddOnlyModelAdmin(ReadonlyModelAdmin):
    """ Disables delete/change capabilities, fields readonly.. """
    change_form_template = 'admin/addonly_form.html'

    def __init__(self, *args, **kwargs):
        super(AddOnlyModelAdmin, self).__init__(*args, **kwargs)

    def get_actions(self, request):
        actions = super(AddOnlyModelAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    def delete_model(self, request, obj):
        pass


class SpecifiedQuantityQuerySetModelAdmin(object):
    """ Can Only Exist Specified Quantity QuerySet """
    def save_model(self, request, obj, form, change):
        # Change or Add
        if change:
            obj.save()
        # Assign ``specified_quantity_queryset`` as 1 when ``specified_quantity_queryset`` not exists
        if not hasattr(self, 'specified_quantity_queryset'):
            self.specified_quantity_queryset = 1
        # Assert whether ``specified_quantity_queryset`` is ``int`` or not
        assert isinstance(self.specified_quantity_queryset, int)
        if self.model.objects.count() >= self.specified_quantity_queryset:
            return
        obj.save()
