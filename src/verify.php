
<html>

    <?php
// Open the file for reading
    if (($h = fopen("cars.csv", "r")) !== FALSE) {
        while (($data = fgetcsv($h, 1000, ",")) !== FALSE) {
        }
        fclose($h);
    } else{
         header('Location: incorrect.html');
    }
    
    
    
    
    ?>

    <?php
    if (($_POST["name"] == 'admin') && ($_POST["pass"] == '12345')) {
        header('Location: home-admin.html');
    } elseif (($_POST["name"] == 'student') && ($_POST["pass"] == '12345')) {
        header('Location: home-student.html');
    } else {
        header('Location: incorrect.html');
    }
    ?>

</html>