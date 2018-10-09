
<html>

    <?php
    // sanitize input to avois injections
    $login_query = filter_var($_POST["name"], FILTER_SANITIZE_STRING);
    $password_query = filter_var($_POST["pass"], FILTER_SANITIZE_STRING);


    // Access databse in mlab
    //$m = new MongoClient("mongodb://$reader:$12345A@localhost");
    
    
    // variable initialization
    $current_user = '';
    $the_big_array = [];
    $filename = 'Augs_Users.csv';
    $failure = TRUE;

    // putting the database (csv) into a multidimensional array - super unsecure 
    if (($h = fopen("{$filename}", "r")) !== FALSE) {
        while (($data = fgetcsv($h, 1000, ",")) !== FALSE) {
            $data = str_replace(' ', '', $data);
            $the_big_array[] = $data;
        }

        fclose($h);
    }


    for ($i = 0; $i < sizeof($the_big_array); $i++) {

        if ($the_big_array[$i][2] == $login_query) {

            if ($the_big_array[$i][3] == $password_query) {

                $current_user = (string) $the_big_array[$i][0] . " " . (string) $the_big_array[$i][1];

                session_start();
                $_SESSION['current_user'] = $current_user;

                $failure = FALSE;

                if ($the_big_array[$i][4] == "student") {
                    header('Location: home-student.php');
                } elseif ($the_big_array[$i][4] == "admin") {
                    header('Location: home-admin.php');
                }
            }
        }
    }

    if ($failure) {
        session_start();
        $_SESSION['login_fail'] = True;
        header('Location: ../public/index.php');
        
    }
    ?>

</html>