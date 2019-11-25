function initialize(){
	
	var socket = io.connect();
	
	socket.on("position", function(data){

		document.getElementById("label").innerHTML = `Tierform: ${data.x}`;


		//Funktioniert noch nicht
		var tierform = `${data.x}`;
		console.log(`${data.x}`);
	
		if(tierform=="Kreis"){
			document.getElementById("animal_img").innerHTML = `Bljat`;
		}
	});



}
