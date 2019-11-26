function initialize(){
	
	var socket = io.connect();
	
	socket.on("position", function(data){

		document.getElementById("label").innerHTML = `Tierform: ${data.x}`;


		//Funktioniert noch nicht
		var tierform = `${data.x}`;

		console.log(tierform);
		while(true){
		if(tierform=="Kreis"){
			document.getElementById("animal_img").innerHTML = "Kreis";
		}
		else if(tierform=="Katze"){
			document.getElementById("animal_img").innerHTML = '<img src="images/katze.jpg" alt="" width="240" height="71" />';
		}
		else if(tierform=="Elefant"){
			document.getElementById("animal_img").innerHTML = "Elefant";
		}
	}
	});



}
