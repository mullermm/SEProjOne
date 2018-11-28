<?php
<<<<<<< HEAD
  $targetdir = '../';   
      // name of the directory where the files should be stored
      

  $targetfile = "UploadedTranscript.txt";

  move_uploaded_file($_FILES['file']['tmp_name'], $targetdir . $targetfile);

  $output = shell_exec('python /Applications/XAMPP/xamppfiles/htdocs/TranscriptScanner.py');
=======
  $targetdir = '../subpages_student/';   
      // name of the directory where the files should be stored
      

  $targetfile = "Transcript.txt";

  move_uploaded_file($_FILES['file']['tmp_name'], $targetdir . $targetfile);

<<<<<<< HEAD
  $output = shell_exec('python /Applications/XAMPP/xamppfiles/htdocs/TranscriptScanner.py');
=======
>>>>>>> 6e2d8210717a3ac78f2ae5986285f2a56c2be55c
>>>>>>> Nghia

  header("Location: ../subpages_student/course_planner.php");





  
?>
