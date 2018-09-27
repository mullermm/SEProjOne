
<html>



    <?php
    $Query_username = 'admin';

    $Query_pass = '12345';


    if (($_POST["name"] == $Query_username) && $_POST["pass"] == $Query_pass) {
        header('Location: home.html');
    } else {
        header('Location: sdfsfsd.html');
    }
    ?>

</html>