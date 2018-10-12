<html>

    <?php
    $department_in = filter_var($_POST["department"], FILTER_SANITIZE_STRING);
    $course_number_in = filter_var($_POST["course-number"], FILTER_SANITIZE_STRING);
    $course_title_in = filter_var($_POST["course-title"], FILTER_SANITIZE_STRING);
    $credits_in = filter_var($_POST["credits"], FILTER_SANITIZE_STRING);
    $course_description_in = filter_var($_POST["course-description"], FILTER_SANITIZE_STRING);
    $core_curriculum_in = filter_var($_POST["core-curriculum"], FILTER_SANITIZE_STRING);
    $prerequisites_in = filter_var($_POST["prerequisites"], FILTER_SANITIZE_STRING);

    $csv = fopen("courses.csv", "a");

    $entry = $department_in . '~' . $course_number_in . '~' . $course_title_in . '~' . $credits_in . '~' . $course_description_in . '~' . $core_curriculum_in . '~' . $prerequisites_in;

    
    fputcsv($csv, explode('~', $entry));
 
    fclose($csv);

    header('Location: ../subpages_admin/course_catalog.php');
    ?>

</html>

