function getAllLocations() {
	// body...
	
	document.getElementById('show1').innerHTML="<h1><i>Please Wait...</i></h1>";
	var xhttp=new XMLHttpRequest();		
	xhttp.onreadystatechange=function()
	{
		if(this.readyState==4 && this.status==200)
		{
			document.getElementById('show1').innerHTML=this.responseText;
		}
	};
	xhttp.open("GET","getAllLocations.php",true);
	xhttp.send();
}

function changeDate() {
	// body...
	var dat=document.getElementById('ye').value;

	document.getElementById('dat_show').innerHTML=dat;
}

function selectLocation() {
	// body...
	var loc=document.getElementById('loc').value;
	// alert(loc);
	if (loc=="") 
	{
		getAllLocations();
	}
	else
	{
		document.getElementById('show2').innerHTML="<h1><i>Please Wait...</i></h1>";
		var xhttp=new XMLHttpRequest();		
	xhttp.onreadystatechange=function()
	{
		if(this.readyState==4 && this.status==200)
		{
			document.getElementById('show2').innerHTML=this.responseText;
		}
	};
	xhttp.open("GET","selectLocation.php?loc="+loc,true);
	xhttp.send();

	}
}

function selectMarla() {
	// body...
	var loc=document.getElementById('loc').value;
	var sq=document.getElementById('sq').value;
	if (sq=="") 
	{
		selectLocation();
	}
	else
	{
		document.getElementById('show3').innerHTML="<h1><i>Please Wait...</i></h1>";
		var merge="loc="+loc+"&marla="+sq;
		var xhttp=new XMLHttpRequest();		
		xhttp.onreadystatechange=function()
		{
			if(this.readyState==4 && this.status==200)
			{
				document.getElementById('show3').innerHTML=this.responseText;
			}
		};
		xhttp.open("POST","selectMarla.php",true);
		xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xhttp.send(merge);
	}

	}

	function submitData() {
		// body...
		var loc=document.getElementById('loc').value;
		var sq=document.getElementById('sq').value; 
		var bed=document.getElementById('bed').value; 
		var dat=document.getElementById('ye').value;

		if (loc=="") 
		{
			alert("Please select a location!");
			return;
		}
		else if (sq=="")
		{
			alert("Please Specify area in Marlas!")
			return;
		}
		else if (bed=="") 
		{
			alert("Please Specify No of Bedrooms!");
			return;
		}
		else if (dat=="")
		 {
		 	alert("Please Select a Date!");
		 	return;
		 }
		 else
		 {
		 	document.getElementById('show_res').innerHTML="<h1><i>Please Wait...</i></h1>";
		 	var merge="loc="+loc+"&marla="+sq+"&bed="+bed+"&dat="+dat;
		 	var xhttp=new XMLHttpRequest();		
		xhttp.onreadystatechange=function()
		{
			if(this.readyState==4 && this.status==200)
			{
				document.getElementById('show_res').innerHTML=this.responseText;
			}
		};
		xhttp.open("POST","submitData.php",true);
		xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xhttp.send(merge);

		 }


	}

