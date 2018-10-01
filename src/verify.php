
<html>

    <?php
    // putting the database (csv) into a multidimensional array - super unsecure 
    $filename = 'Augs_Students.csv';

    $login_query = $_POST["name"];
    $password_query = $_POST["pass"];


    $string = str_replace(' ', '', $string);

    $current_user = '';
    $the_big_array = [];

    if (($h = fopen("{$filename}", "r")) !== FALSE) {
        while (($data = fgetcsv($h, 1000, ",")) !== FALSE) {
            $data = str_replace(' ', '', $data);
            $the_big_array[] = $data;
        }

        fclose($h);
    }
    //var_dump($the_big_array[1][3]);
    // check login against array

    for ($i = 0; $i < sizeof($the_big_array); $i++) {

        echo "<br>";
        var_dump($login_query);
        var_dump($the_big_array[$i][2]);
        echo "&nbsp;&nbsp;";
        var_dump($password_query);
        var_dump($the_big_array[$i][3]);

        if ($the_big_array[$i][2] == $login_query) {

            if ($the_big_array[$i][3] == $password_query) {

                $current_user = (string) $the_big_array[$i][0] . " " . (string) $the_big_array[$i][1];

                session_start();
                $_SESSION['current_user'] = $current_user;

                if ($the_big_array[$i][4] == "student") {
                    header('Location: home-student.php');
                } elseif ($the_big_array[$i][4] == "admin") {
                    header('Location: home-admin.php');
                }
            }
        }
    }
    //header('Location: incorrect.php');
    ?>

</html>