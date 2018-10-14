<?php

$major_select = $_POST["major"];


// Get course info + Split string into classes and numbers
session_start();
$completed = str_split($_SESSION['completed_courses'], 3);
$active = str_split($_SESSION['active_courses'], 3);

// Get completed course begining e.i. COM~100 into array
$completed_prop = [];
$j = 0;
for ($i = 0; $i < sizeof($completed); $i++) {
    if ($i % 2 == 0) {
        $completed_prop[$j] = (string) ($completed[$i] . '~' . $completed[$i + 1]);
        $j++;
    }
}
// Get active course begining e.i. COM~100 into array
$active_prop = [];
$j = 0;
for ($i = 0; $i < sizeof($active); $i++) {
    if ($i % 2 == 0) {
        $active_prop[$j] = (string) ($active[$i] . '~' . $active[$i + 1]);
        $j++;
    }
}

// Open write and read files
$all_courses = fopen("../src/courses.csv", "r");
$maj_prog_csv = fopen("../src/major_prog.csv", "w");
$counter = 0;

fwrite($maj_prog_csv, "Department~Course Number~Course Title~Credits~Course Description~Core Curiculum~Prerequisites~Status" . "\n");

while (($line = fgets($all_courses)) !== false) {

    $line = trim(preg_replace('/\s\s+/', ' ', $line));
    if (substr($line, 0, 3) === $major_select) {

        if (in_array(substr($line, 0, 7), $completed_prop)) {
            fwrite($maj_prog_csv, $line . "~Completed\n");
        } elseif (in_array(substr($line, 0, 7), $active_prop)) {
            fwrite($maj_prog_csv, $line . "~Active\n");
        } else {
            fwrite($maj_prog_csv, $line . "~Not Taken\n");
        }

        $counter++;
    }
}
fwrite($maj_prog_csv, $active_prop[1]);
rewind($all_courses);






header('Location: major_progress.php');
?>
