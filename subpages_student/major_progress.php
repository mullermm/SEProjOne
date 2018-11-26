
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
                            <b>Major Progress</b></h1>
                        <p>View your progress in your major</p>
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
                            <h2>Select a Major</h2>
                            <p>Select a major to review your progress within your field</p>
                        </div>
                    </div>

                    <div class="col-md-5">
                        <div class="content-box">


                            <form action="majorselect.php" method="post">
                                <div class="choice">
                                    <select name="major">
                                        <option disabled selected value> -- select an option -- </option>
                                        <option value="ACC">Accounting</option>
                                        <option value="AIS">American Indian Studies</option>
                                        <option value="ECO">Applied Economics</option>
                                        <option value="ART">Art History</option>
                                        <option value="ART">Art</option>
                                        <option value="BIO">Biology</option>
                                        <option value="BIO">Biophysics</option>
                                        <option value="PSY">Biopsychology</option>
                                        <option value="BUS">Business Administration and Economics</option>
                                        <option value="BUS">Business Administration and Economics</option>
                                        <option value="BUS">Business Administration</option>
                                        <option value="CHM">Chemistry</option>
                                        <option value="PSY">Clinical Psychology</option>
                                        <option value="COM">Communication Arts/Literature</option>
                                        <option value="COM">Communication Studies, Film, and New Media</option>
                                        <option value="COM">Communication Studies</option>
                                        <option value="CSC">Computational Economics</option>
                                        <option value="CSC">Computational Philosophy</option>
                                        <option value="CSC">Computer Science</option>
                                        <option value="CSC">Creative Writing</option>
                                        <option value="CCS">Cross-Cultural Studies</option>
                                        <option value="THP">Directing/Dramaturgy/Playwriting</option>
                                        <option value="ECO">Economics</option>
                                        <option value="EDC">Education</option>
                                        <option value="EDC">Elementary Education</option>
                                        <option value="ENL">English Literature, Language, and Theory</option>
                                        <option value="ENL">English</option>
                                        <option value="ENV">Environmental Studies</option>
                                        <option value="WEL">Exercise Science</option>
                                        <option value="FLM">Film</option>
                                        <option value="MAT">Finance</option>
                                        <option value="FRE">French</option>
                                        <option value="WST">Gender, Sexuality, and Women's Studies</option>
                                        <option value="GER">German</option>
                                        <option value="WST">Global Women's and Gender Studies</option>
                                        <option value="ART">Graphic Design</option>
                                        <option value="HPE">Health Education</option>
                                        <option value="HPE">Health, Physical Education, and Exercise Science</option>
                                        <option value="HIS">History</option>
                                        <option value="HON">Honors Program</option>
                                        <option value="HUM">Interdisciplinary Studies</option>
                                        <option value="BUS">International Business</option>
                                        <option value="HUM">International Relations</option>
                                        <option value="EDC">K-12 English as a Second Language</option>
                                        <option value="CCS">Languages and Cross-Cultural Studies</option>
                                        <option value="SCI">Life Sciences</option>
                                        <option value="MIS">Management Information Systems</option>
                                        <option value="BUS">Management</option>
                                        <option value="MKT">Marketing</option>
                                        <option value="MAT">Mathematical Economics</option>
                                        <option value="MAT">Mathematics</option>
                                        <option value="HIS">Medieval Studies</option>
                                        <option value="MUS">Music Business</option>
                                        <option value="MUS">Music Education</option>
                                        <option value="MUS">Music Performance</option>
                                        <option value="MUS">Music Therapy</option>
                                        <option value="MUS">Music</option>
                                        <option value="COM">New Media</option>
                                        <option value="THP">Performance</option>
                                        <option value="PHI">Philosophy</option>
                                        <option value="WEL">Physical Education</option>
                                        <option value="PHY">Physics</option>
                                        <option value="POL">Political Science and Economics</option>
                                        <option value="POL">Political Science</option>
                                        <option value="PA">Pre-Dentistry</option>
                                        <option value="HPE">Pre-Health Science</option>
                                        <option value="POL">Pre-Law</option>
                                        <option value="PA">Pre-Medical</option>
                                        <option value="PA">Pre-Pharmacy</option>
                                        <option value="WEL">Pre-Physical Therapy</option>
                                        <option value="WEL">Pre-Physician Assistant</option>
                                        <option value="RLN">Pre-Seminary</option>
                                        <option value="COM">Promotional Communication</option>
                                        <option value="PSY">Psychology and Law</option>
                                        <option value="PSY">Psychology</option>
                                        <option value="POL">Public Policy and Political Change</option>
                                        <option value="RLN">Religion</option>
                                        <option value="EDC">Secondary Education (license only)</option>
                                        <option value="WST">Sexuality Studies</option>
                                        <option value="PSY">Social Psychology</option>
                                        <option value="SWK">Social Work</option>
                                        <option value="SOC">Sociology</option>
                                        <option value="PHY">Space Physics</option>
                                        <option value="SPA">Spanish</option>
                                        <option value="EDC">Special Education: Academic Behavioral Strategist</option>
                                        <option value="ART">Studio Art</option>
                                        <option value="THP">Theater</option>
                                        <option value="RLN">Theology and Public Leadership</option>
                                        <option value="URB">Urban Studies</option>
                                        <option value="ART">Web Design</option>
                                    </select> 
                                    <br><br>
                                    <input type="submit" value="Submit">

                                    </form>


                                </div>
                        </div>

                    </div>
                </div>
        </section>

        <section id="addcourses">
            <div class="container">
                <div class="row">
                    <iframe src="major_prog_dir.php" seamless></iframe>
                </div>
            </div>
        </section>

        <section id="addcourses">
            <div class="container">
                <div class="row">
                    <iframe src="major_prog_dir.php" seamless></iframe>
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

