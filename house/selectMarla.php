<?php
$loc=$_POST['loc'];
$marla=$_POST['marla'];

$loc=str_replace(" ", "", $loc);
$data=$loc."@".$marla;
// $loc=explode(",", $loc);
// $loc1="".(string)$loc[0]."@".trim((string)$loc[1]);


$output = shell_exec("python selectMarla.py $data");

 echo ($output);
?>