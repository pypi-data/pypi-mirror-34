define([
    'base/js/namespace',
    'jquery',
    'base/js/utils',
    'base/js/dialog'
], function(Jupyter, $, utils, dialog) {

    var file_suffix = "-jupygit___.ipynb";

    Jupyter.original_name = "";

    function make_request() {
        var clean_url = utils.url_path_join(utils.get_body_data('baseUrl'), 'git/clean')
        var restore_url = utils.url_path_join(utils.get_body_data('baseUrl'), 'git/restore')
        var cookies = getCookies(document.cookie);
        var _xsrf = cookies["_xsrf"];
        var notebook_path = Jupyter.notebook.notebook_path;

        if(Jupyter.original_name === "") {
            Jupyter.original_name = Jupyter.notebook.notebook_name;
            var new_name = Jupyter.original_name.substring(0, Jupyter.original_name.length - 6) + file_suffix

            data = {
                'name': Jupyter.original_name,
                'path': notebook_path
            }

            Jupyter.notebook.rename(new_name).then(function (){
                // Duplicate notebook:
                $.ajax({
                    type: "POST",
                    headers: {
                        "X-XSRFToken": cookies["_xsrf"]
                    },
                    url: clean_url,
                    data: data,
                    success: function(d) {
                        alert("Now you can go ahead and commit your notebook! do not forget to press the button again when you are done")
                        $("#jupygit-button span").text("Keep working");
                    }
                });
            });
        } else {
            data = {
                'name': Jupyter.original_name,
                'path': notebook_path
            }
            $.ajax({
                type: "POST",
                headers: {
                    "X-XSRFToken": cookies["_xsrf"]
                },
                url: restore_url,
                data: data,
                success: function(d) {
                    Jupyter.notebook.rename(Jupyter.original_name).then(function (){
                        Jupyter.original_name = "";
                        alert("You can now keep working");
                        $("#jupygit-button span").text("Prepare notebook");
                    });
                }
            });
        }
    }

    function getCookies(cookie) {
        var dictionary = {};
        var parts = cookie.split(";")
        
        parts.forEach(function (s) {
          var trimmed = s.trim();
          var i = trimmed.indexOf("=");
          dictionary[trimmed.slice(0, i)] = trimmed.slice(i + 1)
        });
        
        return dictionary;
      }

    function place_button() {
        if (!Jupyter.toolbar) {
            $([Jupyter.events]).on("app_initialized.NotebookApp", place_button);
            return;
        }

        Jupyter.toolbar.add_buttons_group([{
            id: 'jupygit-button',
            label: 'Prepare notebook',
            icon: 'fa-git',
            help: 'Clean and prepare your notebook to be commited to Git',
            callback: make_request
        }])
    }

    function load_ipython_extension() {
        console.log("Loading");
	    place_button();
    }

    return {
	    load_ipython_extension: load_ipython_extension
    };

});