// loading models based on select bike brand
$("#id_brand").change(function () {
    var url = $("#bikeForm").attr("data_models_url");  // get the url of the `load_models` view
    var brand_id = $(this).val();  // get the selected brand ID from the HTML input

    $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/bikes/ajax/load_models/)
        data: {
            'brand': brand_id       // add the brand id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_models` view function
            $("#id_bikemodel").html(data);  // replace the contents of the model input with the data that came from the server
        }
    });
});


