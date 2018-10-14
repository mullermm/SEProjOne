

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
$completed = str_split($_SESSION['completed_courses'], 3);
$active = str_split($_SESSION['active_courses'], 3);

// Get completed course begining e.i. COM~100 into array
$completed_prop = [];
$j = 0;
for ($i = 0; $i < sizeof($completed); $i++) {
    if ($i % 2 == 0) {
        $completed_prop[$j] = (string) ($completed[$i] . '~' . $completed[$i + 1]);
        $j++;
    }
}

// Get active course begining e.i. COM~100 into array
$active_prop = [];
$j = 0;
for ($i = 0; $i < sizeof($active); $i++) {
    if ($i % 2 == 0) {
        $active_prop[$j] = (string) ($active[$i] . '~' . $active[$i + 1]);
        $j++;
    }
}

// Open write and read files
$all_courses = fopen("../src/courses.csv", "r");
$courses_completed = fopen("../src/courses_completed.csv", "w");
$courses_active = fopen("../src/courses_active.csv", "w");

// Match classes and write to completed course csv
fwrite($courses_completed, "Department~Course Number~Course Title~Credits~Course Description~Core Curiculum~Prerequisites" . "\n");
for ($i = 0; $i < sizeof($completed_prop); $i++) {
    while (($line = fgets($all_courses)) !== false) {

        if (strpos($line, $completed_prop[$i]) !== false) {
            fwrite($courses_completed, $line);
        }
    }
    rewind($all_courses);
}

fwrite($courses_active, "Department~Course Number~Course Title~Credits~Course Description~Core Curiculum~Prerequisites" . "\n");
for ($i = 0; $i < sizeof($active_prop); $i++) {
    while (($line = fgets($all_courses)) !== false) {

        if (strpos($line, $active_prop[$i]) !== false) {
            fwrite($courses_active, $line);
        }
    }
    rewind($all_courses);
}


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


