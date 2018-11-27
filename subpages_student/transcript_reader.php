<?php
  $targetdir = '../subpages_student';   
      // name of the directory where the files should be stored
  $targetfile = $targetdir.$_FILES['file']['name'];

  if (move_uploaded_file($_FILES['file']['tmp_name'], $targetfile)) {
    header("Location: ../subpages_student/course_planner.php");
  } else { 
    header("Location: ../subpages_student/course_catalog.php");
  }


  header("Location: ../subpages_student/course_planner.php");
?>
