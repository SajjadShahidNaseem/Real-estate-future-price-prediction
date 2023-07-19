<!DOCTYPE html>
<html>
<meta name="viewport" content="width=device-width, initial-scale=1">
<head>
	<script type="text/javascript" src="mjava/functions.js"></script>
</head>
<body>
<center> <img src="../Desktop/9407/is.png" width="200" height="170"> <center>
<h1> <center> D12 CDA SECTOR <center> </h1>
<link rel="stylesheet" href="project.css">
<div class="topnav">
  <a href="home.html">Home</a>
  <a class="active"  href="predict.php">Price Predictor</a>
  <a href="contact.html">Contact</a>
  <a href="about.html">About</a>
</div>
<div class="con">
<img src="../Desktop/9407/cc.png" style="width:100%;">
<div class="cont"><br><br>
<center>
<fieldset>
<legend> Fill The Form </legend>
<br>
<form action="" method="post">

<div id="show1">
	

<div id="show_loc">
<label for="loc">Property Location:</label>

	<script type="text/javascript">
		getAllLocations();
	</script>
	<select id="location" onchange="">
	<option value="">Select location</option>
</select>
</div>


</div>
<br><br>



<input type="button" name="Submit" value="Submit" onclick="submitData();">
</form>
<div id="show_res">
	
</div>
</fieldset>
</center>
</body>
</html>