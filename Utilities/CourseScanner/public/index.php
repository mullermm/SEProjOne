<!DOCTYPE html>
<html>

    <head>
        <meta charset="utf-8">
        <title>Project 1</title>
        <link rel="stylesheet" type="text/css" href="../css/style.css">
        <script src="../../react-0.14.3/react.js"></script>
        <script src="../../react-0.14.3/react-dom.js"></script>
    </head>

    <body>
        <div class = "image-back">
            <img src="images/Augsburg_Logo_Maroon.png" alt="Augsburg University">
        </div>

        <div id="login-wrapper">

            <form action="../src/verify.php" method="post">
                Username <input type="text" name="name"><br>
                Password <input type="password" name="pass"><br>
                <input class="login-button" type="submit" value="Submit">
            </form> 

        </div>
        <div id="login-wrapper">
            <?php
            session_start();

            if (isset($_SESSION['login_fail'])) {
                if ($_SESSION['login_fail']) {
                    echo "<p style='color:#CC0000'>Username or password incorrect</p>";
                    $_SESSION['login_fail'] = False;
                    exit();
                }
            }
            session_reset();
            ?>
        </div>


    </body>

</html>




















