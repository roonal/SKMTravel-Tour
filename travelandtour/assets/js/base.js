(function($) {
    $(function() {
        var selectField = $('#id_role_id'),
            verified = $('#id_package_guide');

        function toggleVerified(value) {
            value == 'Guide' ? verified.show() : verified.hide();
        }

        // show/hide on load based on pervious value of selectFields
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());
        });
    });
})(django.jQuery);