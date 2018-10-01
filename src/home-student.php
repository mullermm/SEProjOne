<!doctype html>
<html lang="en-US">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">

        <!-- Custom Css -->
        <link rel="stylesheet" href="style-home.css" type="text/css" />

        <!-- Ionic icons -->
        <link href="https://unpkg.com/ionicons@4.2.0/dist/css/ionicons.min.css" rel="stylesheet">

        <!-- Google Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900" rel="stylesheet">

        <title>Prroject 1</title>
    </head>

    <body>

        <!-- N A V B A R -->
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
                            <a class="nav-link" href="home.html">Home <i class="icon ion-ios-arrow-forward icon-mobile"></i></a>
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
        <!-- E N D  N A V B A R -->

        <!-- H E R O -->
        <section id="hero">
            <div class="container">
                <div class="row">

                    <div class="col-md-7 content-box hero-content">
                        <span>Augsburg University</span>
                        <h1><?php echo var_dump($current_user[1]); ?>Student <b>Portal</b></h1>
                        <p>The Augsburg Student Home Page</p>
                    </div>
                </div>
            </div>
        </section>
        <!-- E N D  H E R O -->

        <!-- E N D  M A R K E T I N G -->
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
        <!-- E N D  M A R K E T I N G -->

        <!-- E N D  M A R K E T I N G -->
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
        <!-- E N D  M A R K E T I N G -->



        <!-- P R I C I N G -->
        <section id="pricing">
            <div class="container">
                <div class="title-block">
                    <h2>Course Progress</h2>
                    <p>View active courses and completed courses</p>
                    <a href="#" class="btn btn-regular">View Course Progress</a>
                </div>

            </div>
        </section>
        <!-- E N D  P R I C I N G -->


        <!-- T E S T I M O N I A L S -->
        <section id="studentdir">
            <div class="container">
                <div class="title-block">
                    <h2>Payment Portal</h2>
                    <p>Enter payment portal to resolve tuition payment as well as tickets</p>
                    <a href="#" class="btn btn-regular">Payment Portal</a>
                </div>

            </div>
        </section>
        <!-- E N D  T E S T I M O N I A L S -->


        <!-- C A L L  T O  A C T I O N -->
        <section id="call-to-action">
            <div class="container text-center">
                <h2>Something Can Go Here</h2>
                <div class="title-block">
                    <p>Words and such can go here for the bottom of page summary and what not</p>
                    <a href="#" class="btn btn-regular">A button of sorts</a>
                </div>
            </div>
        </section>
        <!-- E N D  C A L L  T O  A C T I O N -->

        <!--  F O O T E R  -->
        <footer>
            <div class="container">
                <div class="row">
                    <div class="col-md-3">
                        <h5>Seo Ranking</h5>
                        <ul>
                            <li><a href="#">Pricing</a></li>
                            <li><a href="#">Affiliate Program</a></li>
                            <li><a href="#">Developer API</a></li>
                            <li><a href="#">Support</a></li>
                            <li><a href="#">Video Tutorials</a></li>
                        </ul>
                    </div>
                    <div class="col-md-3">
                        <h5>Main Tools</h5>
                        <ul>
                            <li><a href="#">Rank Tracker</a></li>
                            <li><a href="#">Backlink Checker</a></li>
                            <li><a href="#">Keyword Generator</a></li>
                            <li><a href="#">Serp Checker</a></li>
                            <li><a href="#">Site Audit</a></li>
                        </ul>
                    </div>
                    <div class="col-md-3">
                        <h5>Blog</h5>
                        <ul>
                            <li><a href="#">Get High Quality Backlinks</a></li>
                            <li><a href="#">Top Google Searches</a></li>
                            <li><a href="#">Avoid Google Penalties</a></li>
                            <li><a href="#">White Hat SEO Tips</a></li>
                            <li><a href="#">Google Trends</a></li>
                        </ul>
                    </div>
                    <div class="col-md-3">
                        <h5>Company</h5>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur scelerisque, tortor nec mattis feugiat, velit purus euismod odio, quis vulputate velit urna.</p>
                        <p><a href="mailto:sales@theseocompany.com" class="external-links">sales@theseocompany.com</a></p>
                    </div>
                </div> 
                <div class="divider"></div>
                <div class="row">
                    <div class="col-md-6 col-xs-12">
                        <a href="#"><i class="icon ion-logo-facebook"></i></a>
                        <a href="#"><i class="icon ion-logo-instagram"></i></a>
                        <a href="#"><i class="icon ion-logo-twitter"></i></a>
                        <a href="#"><i class="icon ion-logo-youtube"></i></a>
                    </div>
                    <div class="col-md-6 col-xs-12">
                        <small>2018 &copy; All rights reserved. Made by <a href="http://templune.com/" target="blank" class="external-links">Templune</a></small>
                    </div>
                </div>
            </div>
        </footer>
        <!--  E N D  F O O T E R  -->


        <!-- External JavaScripts -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
    </body>
</html>