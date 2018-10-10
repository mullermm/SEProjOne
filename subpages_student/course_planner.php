<!doctype html>
<html lang="en-US">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
    <link rel="stylesheet" href="../css/style-home.css" type="text/css" />
    <link href="https://unpkg.com/ionicons@4.2.0/dist/css/ionicons.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900" rel="stylesheet">

    <title>Project 1</title>

</head>

<body>

<!-- N A V B A R -->
<nav class="navbar navbar-default navbar-expand-lg fixed-top custom-navbar">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="icon ion-md-menu"></span>
    </button>
    <img src="../src/images/logo.png" class="img-fluid nav-logo-mobile" alt="Company Logo">
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <div class="container">
            <a href="../src/home-student.php"><img src="../src/images/logo.png" class="img-fluid nav-logo-desktop" alt="Company Logo"></a>
            <ul class="navbar-nav ml-auto nav-right" data-easing="easeInOutExpo" data-speed="1250" data-offset="65">
                <li class="nav-item nav-custom-link">
                    <a class="nav-link" href="../src/home-student.php">Return to Portal Home <i class="icon ion-ios-arrow-forward icon-mobile"></i></a>
                </li>
                <li class="nav-item nav-custom-link">


            </ul>
        </div>
    </div>
</nav>
<!-- E N D  N A V B A R -->

<section id="hero">
    <div class="container">
        <div class="row">

            <div class="col-md-7 content-box hero-content">
                <span>Augsburg University</span>
                <h1> <?php
                    session_start();
                    echo $_SESSION['current_user'];
                    ?>
                    <br>
                    <b>View Pending Courses</b></h1>
                <p>Submit your current transcript to view future courses required for degree completion</p>
            </div>
        </div>
    </div>
</section>

<section id="addcourses">
    <div class="container">
        <div class="row">



            <div class="col-md-7">
                <div class="content-box">
                    <span>Augsburg University</span>
                    <h2>Plan Your Future</h2>
                    <p>Upload your transcript in a PDF format to view your future courses</p>
                </div>
            </div>


            <div class="col-md-5">
                <div class="content-box">

                    <!-- DO NOT USE THIS, I FEAR BAD THINGS MAY HAPPEN -->
                    <form action="../src/add-transcript.php" method="post" onsubmit="return confirm('TEST DO NOT RUN');">
                        <br><br>
                        <input id = "a" type="file" name="firstname" value="">
                        <br>
                        <input onclick="verify()" type="submit" value="Enter" class="btn btn-regular">
                    </form>


                </div>
            </div>


        </div>
    </div>
</section>


<footer>
    <div class="container">
        <div class="row">

            <div class="col-md-6">
                <h5>Site Links</h5>
                <ul>
                    <li><a href="../src/home-student.php">Return to Portal Home</a></li>
                </ul>
            </div>

            <div class="col-md-6">
                <h5>Augsburg University</h5>
                <p>Set in a vibrant neighborhood at the heart of the Twin Cities, Augsburg offers undergraduate and graduate degrees to students of diverse backgrounds.</p>
                <p><a href="mailto:fake@fake.com" class="external-links">fake@fake.com</a></p>
            </div>
        </div>
        <div class="divider"></div>
        <div class="row">
            <div class="col-md-6 col-xs-12">
                <a href="https://www.facebook.com/AugsburgUniversity/"><i class="icon ion-logo-facebook"></i></a>
                <a href="https://www.instagram.com/augsburguniversity/?hl=en"><i class="icon ion-logo-instagram"></i></a>
                <a href="https://twitter.com/augsburgu?lang=en"><i class="icon ion-logo-twitter"></i></a>
                <a href="https://www.youtube.com/channel/UCH87WIDHvBPqH3XsCCupoLA"><i class="icon ion-logo-youtube"></i></a>
            </div>
        </div>
    </div>
</footer>


<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
</body>
</html>