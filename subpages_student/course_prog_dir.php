

<head>

    <!-- Bootstrap core CSS -->
    <link href="../css/bootstrap.min.css" rel="stylesheet">
    <link href="../css/dataTables.bootstrap.css" rel="stylesheet">

</head>


<div class="container-fluid">


    <div id='table-container'></div>

</div><!-- /.container -->


<!-- Bootstrap core JavaScript
================================================== -->
<!-- Placed at the end of the document so the pages load faster -->
<script type="text/javascript" src="../js/jquery.min.js"></script>
<script type="text/javascript" src="../js/bootstrap.min.js"></script>
<script type="text/javascript" src="../js/jquery.csv.min.js"></script>
<script type="text/javascript" src="../js/jquery.dataTables.min.js"></script>
<script type="text/javascript" src="../js/dataTables.bootstrap.js"></script>
<script type="text/javascript" src="../js/csv_to_html_table.js"></script>



<?php

// Get course info + Split string into classes and numbers
session_start();
$completed = $_SESSION['completed_courses'];
$active =  $_SESSION['active_courses'];

// Split string into classes and numbers
$completed_arr = str_split($completed, 3);
$active_arr = str_split($active, 3);



// Get completed course begining e.i. COM~100 into array 





// Get active course begining e.i. COM~100 into array
var_dump($completed_arr);






// Write the courses_active and courses_completed csv







?>






<script type="text/javascript">
    function format_link(link) {
        if (link)
            return "<a href='" + link + "' target='_blank'>" + link + "</a>";
        else
            return "";
    }

    CsvToHtmlTable.init({
        csv_path: '../src/courses_completed.csv',
        element: 'table-container',
        allow_download: true,
        csv_options: {separator: '~', delimiter: '`'},
        datatables_options: {"paging": false},
        custom_formatting: [[4, format_link]]
    });
</script>
