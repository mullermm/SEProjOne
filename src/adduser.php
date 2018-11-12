<html>

    <?php
    $firstname_in = filter_var($_POST["firstname"], FILTER_SANITIZE_STRING);
    $lastname_in = filter_var($_POST["lastname"], FILTER_SANITIZE_STRING);
    $username_in = filter_var($_POST["username"], FILTER_SANITIZE_STRING);
    $pass = 'null';
    $status = 'student';


    $csv1 = fopen("csv/Augs_Users.csv", "a");
    $csv2 = fopen("csv/Augs_Users_Names.csv", "a");


    $entry1 = $firstname_in . ' ,' . $lastname_in . ' ,' . $username_in . ' ,' . $pass . ' ,' . $status;
    $entry2 = $firstname_in . ' ,' . $lastname_in . ' ,' . $username_in . ' ,' . $status;



    fputcsv($csv1, explode(' ,', $entry1));
    fputcsv($csv2, explode(' ,', $entry2));

    fclose($csv1);
    fclose($csv2);

    header('Location: ../subpages_admin/add_student.php');
    ?>

</html>