<head>

    <link href="../css/bootstrap.min.css" rel="stylesheet">
    <link href="../css/dataTables.bootstrap.css" rel="stylesheet">

</head>

<div class="container-fluid">
    
<?php
// $output=shell_exec('python src\majors\Major.py');
$output=shell_exec('python ../src/majors/Major.py');
print $output;

?>

    <div id='table-container'></div>

</div><!-- /.container -->

<script type="text/javascript" src="../js/jquery.min.js"></script>
<script type="text/javascript" src="../js/bootstrap.min.js"></script>
<script type="text/javascript" src="../js/jquery.csv.min.js"></script>
<script type="text/javascript" src="../js/jquery.dataTables.min.js"></script>
<script type="text/javascript" src="../js/dataTables.bootstrap.js"></script>
<script type="text/javascript" src="../js/csv_to_html_table.js"></script>




<script type="text/javascript">
    function format_link(link) {
        if (link)
            return "<a href='" + link + "' target='_blank'>" + link + "</a>";
        else
            return "";
    }

    CsvToHtmlTable.init({
        csv_path: 'major_progress.csv',
        element: 'table-container',
        allow_download: false,
        csv_options: {separator: '~', delimiter: '`'},
        datatables_options: {"paging": false},
        custom_formatting: [[4, format_link]]
    });
</script>