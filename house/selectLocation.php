<?php
$loc=$_GET['loc'];

$loc=str_replace(" ", "", $loc);
// $loc=explode(",", $loc);
// $loc1="".(string)$loc[0]."@".trim((string)$loc[1]);

$output = shell_exec("python selectLocation.py $loc");

 echo ($output);
?>