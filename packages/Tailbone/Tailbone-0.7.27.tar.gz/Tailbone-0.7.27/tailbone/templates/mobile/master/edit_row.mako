## -*- coding: utf-8; -*-
<%inherit file="/mobile/master/edit.mako" />

<%def name="title()">${index_title} &raquo; ${parent_title} &raquo; ${instance_title} &raquo; Edit</%def>

<%def name="page_title()">${h.link_to(index_title, index_url)} &raquo; ${h.link_to(parent_title, parent_url)} &raquo; ${h.link_to(instance_title, instance_url)} &raquo; Edit</%def>

## TODO: this should not be necessary, correct?
## <%def name="buttons()">
##   <br />
##   ${h.submit('create', form.update_label)}
##   ${h.link_to("Cancel", form.cancel_url, class_='ui-btn ui-corner-all')}
## </%def>

<div class="form-wrapper">
##  ${form.render(buttons=capture(self.buttons))|n}
  ${form.render()|n}
</div><!-- form-wrapper -->

% if master.mobile_rows_deletable and request.has_perm('{}.delete_row'.format(permission_prefix)):
    ${h.form(url('mobile.{}.delete_row'.format(route_prefix), uuid=parent_instance.uuid, row_uuid=row.uuid))}
    ${h.csrf_token(request)}
    ${h.submit('submit', "Delete this Row")}
    ${h.end_form()}
% endif
