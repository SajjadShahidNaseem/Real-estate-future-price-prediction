<?php
$loc=$_POST['loc'];
$marla=$_POST['marla'];
$bed=$_POST['bed'];
$dat=$_POST['dat'];

$loc=str_replace(" ", "", $loc);
$data=$loc."@".$marla."@".$bed."@".$dat;
// $loc=explode(",", $loc);
// $loc1="".(string)$loc[0]."@".trim((string)$loc[1]);


$output = shell_exec("python submitData.py $data");

 echo ($output);

?>