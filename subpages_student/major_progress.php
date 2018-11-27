
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

        <?php
            $output=shell_exec('python C:\xampp\htdocs\src\majors\Major.py');
        ?>

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


                            <form action="#" method="post">
                                <div class="choice">
                                    <select name="major">
                                        <option disabled selected value> -- select an option -- </option>
                                        <option value="0">American Indian Studies</option>
                                        <option value="1">Art History</option>
                                        <option value="2">Art Education</option>
                                        <option value="3">Graphic Design</option>
                                        <option value="4">Studio Art</option>
                                        <option value="5">Biology BA</option>
                                        <option value="6">Biology BS</option>
                                        <option value="7">Biopsychology</option>
                                        <option value="8">Life Sciences</option>
                                        <option value="9">Accounting</option>
                                        <option value="10">Finance</option>
                                        <option value="11">International Business</option>
                                        <option value="12">Managment</option>
                                        <option value="13">Marketing</option>
                                        <option value="14">Managment Information Systems</option>
                                        <option value="15">Music Business</option>
                                        <option value="16">Cross Cultural Studies</option>
                                        <option value="17">Chemistry ACS</option>
                                        <option value="18">Chemistry</option>
                                        <option value="19">CChemistry NON ACS</option>
                                        <option value="20">Communication Studies</option>
                                        <option value="21">Computational Economics</option>
                                        <option value="22">Computational Philosophy</option>
                                        <option value="23">Computer Science BA</option>
                                        <option value="24">Computer Science BS</option>
                                        <option value="25">Applied Economics</option>
                                        <option value="26">Business Economics</option>
                                        <option value="27">Economics</option>
                                        <option value="28">Mathematical Economics</option>
                                        <option value="29">Elementary Education</option>
                                        <option value="30">Elementary Education Comm Arts</option>
                                        <option value="31">Elementary Education General Science</option>
                                        <option value="32">Elementary Education Math</option>
                                        <option value="33">Elementary Education Social Studies</option>
                                        <option value="34">English Commication Arts</option>
                                        <option value="35">English Creative Writing</option>
                                        <option value="36">English Literature</option>
                                        <option value="37">Enviormental Studies</option>
                                        <option value="38">Enviormental Studies HECUA</option>
                                        <option value="39">Secondary Education</option>
                                        <option value="40">Social Studies</option>
                                        <option value="41">English Second Language</option>
                                        <option value="42">Film Production</option>
                                        <option value="43">Theory Culture</option>
                                        <option value="44">French</option>
                                        <option value="45">German</option>
                                        <option value="46">History</option>
                                        <option value="47">Exercise Science BA</option>
                                        <option value="48">Exercise Science Pre-Health BS</option>
                                        <option value="49">Health Education</option>
                                        <option value="50">Physical Education</option>
                                        <option value="51">Interdisciplinary Studies</option>
                                        <option value="52">Internation Relations</option>
                                        <option value="53">International Relations Business</option>
                                        <option value="54">Mathematics BA</option>
                                        <option value="55">Mathematics BS</option>
                                        <option value="56">Mathematics Teaching</option>
                                        <option value="57">Medieval Studies</option>
                                        <option value="58">Music</option>
                                        <option value="59">Music Business</option>
                                        <option value="60">Music Education</option>
                                        <option value="61">Music Performance</option>
                                        <option value="62">Music Therapy</option>
                                        <option value="63">New Media</option>
                                        <option value="64">New Media Game Design</option>
                                        <option value="65">New Media Promotional Communication</option>
                                        <option value="66">New Media Web Design</option>
                                        <option value="67">Nursing</option>
                                        <option value="68">Philosophy</option>
                                        <option value="69">Biophysics</option>
                                        <option value="70">Physics BA</option>
                                        <option value="71">Physics BS</option>
                                        <option value="72">Spacephysics</option>
                                        <option value="73">Political Science and Economics</option>
                                        <option value="74">Politcal Science</option>
                                        <option value="75">Political Science Prelaw</option>
                                        <option value="76">Political Science Public Policy</option>
                                        <option value="77">Clinical Psychology</option>
                                        <option value="78">Psychology</option>
                                        <option value="79">Psychology and Law</option>
                                        <option value="80">Social Psychology</option>
                                        <option value="81">Religion</option>
                                        <option value="82">Theology and Public Leadership</option>
                                        <option value="83">Sociology</option>
                                        <option value="84">Spanish</option>
                                        <option value="85">Special Education</option>
                                        <option value="86">Social Work</option>
                                        <option value="87">Theater</option>
                                        <option value="88">Theater Design Technical</option>
                                        <option value="89">Theater Directing</option>
                                        <option value="90">Theater Performance</option>
                                        <option value="91">Urban Studies</option>
                                        <option value="92">Womens Studies</option>

                                    </select> 
                                    <br><br>
                                    <input type="submit" name="submit" value="Submit">
                                    </form>
                                    <?php
                                        if(isset($_POST['submit'])){
                                            $major = $_POST['major'];  // Storing Selected Value In Variable
                                            $output = shell_exec('python C:\xampp\htdocs\src\majors\Class_Progress.py ' . $major);
                                        }
                                    ?>

                                </div>
                        </div>

                    </div>
                </div>
        </section>
        <h1>
        Completed Courses
        </h1>
        <section id="donecourses">
            <div class="container">
                <div class="row">
                    <iframe src="donecourses.php" seamless></iframe>
                </div>
            </div>
        </section>
        <h1>
        Courses To Complete
        </h1>
        <section id="todocourses">
            <div class="container">
                <div class="row">
                    <iframe src="todocourses.php" seamless></iframe>
                </div>
            </div>
        </section>
        <h1>
        Major Progress
        </h1>
        <section id="addmajors">
            <div class="container">
                <div class="row">
                    <iframe src="major_picker.php" seamless></iframe>
                </div>
            </div>
        </section>

        <h1>
        Minor Progress
        </h1>
        <section id="addminors">
            <div class="container">
                <div class="row">
                    <iframe src="major_picker.php" seamless></iframe>
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

