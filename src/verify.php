
<html>

    <?php
    $filename = 'Augs_Students.csv';

    $the_big_array = [];

    if (($h = fopen("{$filename}", "r")) !== FALSE) {
        while (($data = fgetcsv($h, 1000, ",")) !== FALSE) {
            $the_big_array[] = $data;
        }

        fclose($h);
    }

    var_dump($the_big_array[1][1]);





    if (($_POST["name"] == 'admin') && ($_POST["pass"] == '12345')) {
        header('Location: home-admin.html');
    } elseif (($_POST["name"] == 'student') && ($_POST["pass"] == '12345')) {
        header('Location: home-student.html');
    }
    
    
    else {
        header('Location: incorrect.html');
    }
    ?>

</html>