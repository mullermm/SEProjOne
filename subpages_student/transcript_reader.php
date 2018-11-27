<?php
  $targetdir = '../subpages_student/';   
      // name of the directory where the files should be stored
      

  $targetfile = "Transcript.txt";

  move_uploaded_file($_FILES['file']['tmp_name'], $targetdir . $targetfile);


  header("Location: ../subpages_student/course_planner.php");





  
?>
