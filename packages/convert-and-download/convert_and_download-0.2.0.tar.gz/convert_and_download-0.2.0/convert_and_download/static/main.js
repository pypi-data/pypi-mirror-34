// Add new exporter

define([
    'jquery',
    'base/js/namespace',
    'base/js/utils'
], function(
    $,
    Jupyter,
    utils
) {
    function load_ipython_extension() {

        var old_selection_changed = Jupyter.NotebookList.prototype._selection_changed;
        Jupyter.NotebookList.prototype._selection_changed = function () {
            old_selection_changed.call(this);
            var only_notebooks_selected = true;
            var checked = 0;
            $('.list_item :checked').each(function(index, item) {
                var parent = $(item).parent().parent();
                checked++;
                if (only_notebooks_selected) {
                    if (parent.data('type') !== 'notebook') {
                        only_notebooks_selected = false;
                    }
                }
            });
            if (checked >= 1 && only_notebooks_selected) {
                $('.convert-download-button').css('display', 'inline-block');
            } else {
                $('.convert-download-button').css('display', 'none');
            }
        };

        convert_and_download = function() {
            var selected = [];
            $('.list_item :checked').each(function(index, item) {
                var parent = $(item).parent().parent();
                selected.push({
                    name: parent.data('name'),
                    path: parent.data('path'),
                    type: parent.data('type')
                });
            });
            var url = utils.url_path_join(utils.get_body_data("baseUrl"), 'dlconvert', 'pdf');
            for (var i in selected) {
                var item = selected[i];
                if (item.type === 'notebook') {
                    url = utils.url_path_join(url, utils.encode_uri_components(item.path));
                }
            }
            url = url + '?download=true';
            var w = window.open('', Jupyter._target);
            w.location = url;
        };

        $('<button/>')
            .addClass('convert-download-button btn btn-default btn-xs')
            .attr('title', 'Convert and Download Selected')
            .attr('aria-label', 'Convert and Download Selected')
            .text('Convert and Download Selected')
            .insertBefore('.shutdown-button')
            .css('display', 'none')
            .on('click', convert_and_download);

    };

    return {
        load_ipython_extension: load_ipython_extension
    };
});
