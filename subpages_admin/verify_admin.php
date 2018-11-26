
<html>

<?php
// sanitize input to avois injections
$login_query = filter_var($_POST["name"], FILTER_SANITIZE_STRING);
$password_query = filter_var($_POST["pass"], FILTER_SANITIZE_STRING);


// variable initialization
$current_user =session_start(); echo $_SESSION['current_user'];
$the_big_array = [];
$filename = 'csv/Augs_Users.csv';
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
        if ($the_big_array[$i][4] == "admin") {
            header('Location: home-admin.php');
        } 
    }
}

//If failure, go back to student home
if ($failure) {
    session_start();
    $_SESSION['login_fail'] = True;
    header('Location: ../home-student.php');
    
}
?>

</html>