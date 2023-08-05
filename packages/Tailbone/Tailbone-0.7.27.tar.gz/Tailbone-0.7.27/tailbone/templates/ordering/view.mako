## -*- coding: utf-8; -*-
<%inherit file="/batch/view.mako" />

<%def name="extra_javascript()">
  ${parent.extra_javascript()}
  <script type="text/javascript">
    $(function() {

        $('.load-worksheet').click(function() {
            % if vendor_cost_count is not Undefined and vendor_cost_threshold is not Undefined and vendor_cost_count > vendor_cost_threshold:
                if (! confirm("This vendor has ${'{:,d}'.format(vendor_cost_count)} cost records.\n\n" +
                              "It is not recommended to use Order Form mode for such a large catalog.\n\n" +
                              "Are you sure you wish to do it anyway?")) {
                    return;
                }
            % endif
            $(this).button('disable').button('option', 'label', "Working, please wait...");
            location.href = '${url('ordering.worksheet', uuid=batch.uuid)}';
        });

    });
  </script>
</%def>

<%def name="extra_styles()">
  ${parent.extra_styles()}
  ${h.stylesheet_link(request.static_url('tailbone:static/css/purchases.css'))}
</%def>

<%def name="context_menu_items()">
  ${parent.context_menu_items()}
  % if request.has_perm('{}.download_excel'.format(permission_prefix)):
      <li>${h.link_to("Download {} as Excel".format(model_title), url('{}.download_excel'.format(route_prefix), uuid=batch.uuid))}</li>
  % endif
</%def>

${parent.body()}
