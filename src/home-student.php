<!doctype html>
<html lang="en-US">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
        <link rel="stylesheet" href="style-home.css" type="text/css" />
        <link href="https://unpkg.com/ionicons@4.2.0/dist/css/ionicons.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900" rel="stylesheet">

        <title>Project 1</title>

    </head>

    <body>

        <nav class="navbar navbar-default navbar-expand-lg fixed-top custom-navbar">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="icon ion-md-menu"></span>
            </button>
            <img src="images/logo.png" class="img-fluid nav-logo-mobile" alt="Company Logo">
            <div class="collapse navbar-collapse" id="navbarNavDropdown">
                <div class="container">
                    <img src="images/logo.png" class="img-fluid nav-logo-desktop" alt="Company Logo">
                    <ul class="navbar-nav ml-auto nav-right" data-easing="easeInOutExpo" data-speed="1250" data-offset="65">
                        <li class="nav-item nav-custom-link">
                            <a class="nav-link" href="home-student.php">Home <i class="icon ion-ios-arrow-forward icon-mobile"></i></a>
                        </li>
                        <li class="nav-item nav-custom-link">
                            <a class="nav-link" href="#addcourses">Course Catalog<i class="icon ion-ios-arrow-forward icon-mobile"></i></a>
                        </li>
                        <li class="nav-item nav-custom-link">
                            <a class="nav-link" href="#addcourses2">Major Progress<i class="icon ion-ios-arrow-forward icon-mobile"></i></a>
                        </li>
                        <li class="nav-item nav-custom-link">
                            <a class="nav-link" href="#pricing">Course Progress<i class="icon ion-ios-arrow-forward icon-mobile"></i></a>
                        </li>
                        <li class="nav-item nav-custom-link">
                            <a class="nav-link" href="#pricing">Payment Portal<i class="icon ion-ios-arrow-forward icon-mobile"></i></a>
                        </li>

                    </ul>
                </div>
            </div>
        </nav>

        <section id="hero">
            <div class="container">
                <div class="row">

                    <div class="col-md-7 content-box hero-content">
                        <span>Augsburg University</span>
                        <h1>Welcome <?php
                            session_start();
                            echo $_SESSION['current_user'];
                            ?>
                            <br>
                            <b> Student Portal</b></h1>
                        <p>The Augsburg Student Home Page</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="addcourses">
            <div class="container">
                <div class="row">
                    <div class="col-md-5">
                        <div class="content-box">
                            <span>Augsburg University</span>
                            <h2>Course Catalog</h2>
                            <p>View all upcoming courses and sections</p>
                            <a href="#" class="btn btn-regular">View Courses</a>
                        </div>
                    </div>
                    <div class="col-md-7">
                        <img src="images/demo-image.png" class="img-fluid" alt="Demo image">
                    </div>
                </div>
            </div>
        </section>

        <section id="addcourses2">
            <div class="container">
                <div class="row">
                    <div class="col-md-7">
                        <img src="images/sec.png" class="img-fluid" alt="Demo image">
                    </div>
                    <div class="col-md-5">
                        <div class="content-box">
                            <span>Augsburg University</span>
                            <h2>Major Progress</h2>
                            <p>View the progress you've made in any given major or minor</p>
                            <a href="#" class="btn btn-regular">View Major Progress</a>
                        </div>
                    </div>

                </div>
            </div>
        </section>



        <section id="pricing">
            <div class="container">
                <div class="title-block">
                    <h2>Course Progress</h2>
                    <p>View active courses and completed courses</p>
                    <a href="#" class="btn btn-regular">View Course Progress</a>
                </div>

            </div>
        </section>


        <section id="studentdir">
            <div class="container">
                <div class="title-block">
                    <h2>Payment Portal</h2>
                    <p>Enter payment portal to resolve tuition payment as well as tickets</p>
                    <a href="#" class="btn btn-regular">Payment Portal</a>
                </div>

            </div>
        </section>


        <section id="call-to-action">
            <div class="container text-center">
                <h2>Something Can Go Here</h2>
                <div class="title-block">
                    <p>Words and such can go here for the bottom of page summary and what not</p>
                    <a href="#" class="btn btn-regular">A button of sorts</a>
                </div>
            </div>
        </section>

        <footer>
            <div class="container">
                <div class="row">

                    <div class="col-md-6">
                        <h5>Main Tools</h5>
                        <ul>
                            <li><a href="#">Course Catalog</a></li>
                            <li><a href="#">Major Progress</a></li>
                            <li><a href="#">Course Progress</a></li>
                            <li><a href="#">Payment Portal</a></li>
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