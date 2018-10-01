
<html>

    <?php
    // putting the database (csv) into a multidimensional array - super unsecure 
    $filename = 'Augs_Students.csv';

    $login_query = $_POST["name"];
    $password_query = $_POST["pass"];





    $the_big_array = [];

    if (($h = fopen("{$filename}", "r")) !== FALSE) {
        while (($data = fgetcsv($h, 1000, ",")) !== FALSE) {
            $the_big_array[] = $data;
        }

        fclose($h);
    }
    //var_dump($the_big_array[1][2]);


    // check login against array

    for ($i = 1; $i < sizeof($the_big_array); $i++) {

        if ($the_big_array[$i][2] == $login_query) {
            if ($the_big_array[$i][3] == $login_query) {
                if ($the_big_array[$i][4] == "student") {
                    header('Location: home-student.html');
                } elseif ($the_big_array[$i][4] == "admin") {
                    header('Location: home-admin.html');
                }
            }
        }
    }
    header('Location: incorrect.html');
    
    
    ?>

</html>