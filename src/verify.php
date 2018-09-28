
<html>



    <?php
    $Query_username = 'admin';

    $Query_pass = '12345';


    if (($_POST["name"] == 'admin') && ($_POST["pass"] == '12345')) {
        header('Location: home-admin.html');
    } elseif (($_POST["name"] == 'student') && ($_POST["pass"] == '12345')) {
        header('Location: home-student.html');
    } else{
        header('Location: incorrect.html');
    }
    ?>

</html>