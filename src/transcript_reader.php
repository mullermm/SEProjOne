<?php

    $transcript_in = $_POST["transcript"];

    header("Location: ../subpages_student/course_planner.php");

?>

<script type="text/javascript">
    let transcript = '<?php print $transcript_in ?>';


</script>
