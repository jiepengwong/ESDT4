<?php

?>


<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width">

    <title> Catalogue </title>

    <link rel="stylesheet" href="">
    <!--[if lt IE 9]>
    <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
    <!-- Bootstrap libraries -->
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css'
    rel='stylesheet'
    integrity='sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC'
    crossorigin='anonymous'>

    <!-- Latest compiled and minified JavaScript -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
</head>

    <body>

<div id="main-container" class="container">

    <h1 class="display-4">Items on Sale!</h1>
    <div id='cards'></div>

</div>

<script>
        // Helper function to display error message
function showError(message) {
    // Hide the table and button in the event of error
    $('#itemTable').hide();
    $('#addItemBtn').hide();

    // Display an error under the main container
    $('#main-container')
        .append("<label>"+message+"</label>");
}

// anonymous async function 
// - using await requires the function that calls it to be async
$(async() => {
    // Change serviceURL to your own
    var serviceURL = "http://127.0.0.1:5001/items";
    // var serviceURL = "http://192.168.1.5:5000/item";

    try {
        const response =
            await fetch(
            serviceURL, { method: 'GET' }
        );
        const result = await response.json();
            if (response.status === 200) {

            // success case
            var items = result.Success; 
            // console.log(items)
            // finding all available items {status = open} to be shown on UI
            var itemsOpen = [];
            for (let i = 0; i < items.length; i++) {
                const element = items[i];
                if (element.item_status == "open") {
                    itemsOpen.push(element)
                }
            }
            // console.log(itemsOpen)
            var card = "";
            for (const item of itemsOpen) {
                cardDetails =
                        "<h5 class='card-title'>" + item.item_name + "</h5>" +
                        "<p class='card-text'>" + item.category + "</p>" +
                        "<p class='card-text'>" + item.description + "</p>" +
                        "<a href='http://127.0.0.1:5001/items/" + item._id + "' class='btn btn-primary'>More Details</a>";
                card += "<div class='card' style='width: 18rem;'> <div class='card-body'>" + cardDetails + "</div> </div>";
            }
                // add all the rows to the table
                $('#cards').append(card);
            } else if (response.status == 404) {
                // No items
                showError(result.message);
            } else {
                // unexpected outcome, throw the error
                throw response.status;
            }
        } catch (error) {
            // Errors when calling the service; such as network error, 
            // service offline, etc
            showError
            ('There is a problem retrieving item data, please try again later.<br />' + error);
        } // error
});
</script>

        <!-- BOOTSTRAP -->    
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" 
        integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" 
        crossorigin="anonymous"></script>

    </body>

</html>