
<html>

<?php

// variable initialization
$current_user = session_start(); echo $_SESSION['current_user'];
$the_big_array = [];
$filename = '../src/csv/Augs_Users.csv';
$failure = TRUE;

// putting the database (csv) into a multidimensional array - super unsecure 
if (($h = fopen("{$filename}", "r")) !== FALSE) {
    while (($data = fgetcsv($h, 1000, ",")) !== FALSE) {
        $data = str_replace(' ', '', $data);
        $the_big_array[] = $data;
    }

    fclose($h);
}
                
//For all the users in the array
for ($i = 0; $i < sizeof($the_big_array); $i++) {
    
    //if the user in the array matches the current user
    if ($the_big_array[$i][2] == $current_user) {
        
        //if that user is an admin, go to admin page
        if ($the_big_array[$i][4] != "admin") {
            header('Location: ../subpages_student/home-student.php');
        } 
        else{
            header('Location: ../subpages_admin/home-admin.php');
        }

    }
}

?>

</html>