<?php
  $targetdir = '../';   
      // name of the directory where the files should be stored
      

  $targetfile = "Transcript.txt";

  move_uploaded_file($_FILES['file']['tmp_name'], $targetdir . $targetfile);

  $output = shell_exec('/usr/bin/python /Applications/XAMPP/xamppfiles/htdocs/src/TranscriptScanner/TranscriptScanner.py');






  header("Location: ../subpages_student/course_planner.php");





  
?>
