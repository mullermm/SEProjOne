<?php
  $targetdir = '../subpages_student/';   
      // name of the directory where the files should be stored
      

  $targetfile = "UploadedTranscript.txt";

  move_uploaded_file($_FILES['file']['tmp_name'], $targetdir . $targetfile);

  $output = shell_exec('python C:\xampp\htdocs\src\TranscriptScanner\TranscriptScanner.py');

  header("Location: ../subpages_student/course_planner.php");





  
?>
