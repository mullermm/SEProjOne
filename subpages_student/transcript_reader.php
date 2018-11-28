<?php
  $targetdir = '../subpages_student/';   
      // name of the directory where the files should be stored
      

  $targetfile = "Transcript.txt";

  move_uploaded_file($_FILES['file']['tmp_name'], $targetdir . $targetfile);

<<<<<<< HEAD
  $output = shell_exec('python /Applications/XAMPP/xamppfiles/htdocs/TranscriptScanner.py');
=======
>>>>>>> 12578401c0ece02503569b6a91fb4a363be373d9

  header("Location: ../subpages_student/course_planner.php");





  
?>
