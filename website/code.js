function initialize(){

    var allowsound = false;
    var playStopButton = document.getElementById("playStopButton");
    var socket = io.connect();
	
	socket.on("position", function(data){

		document.getElementById("label").innerHTML = `Tierform: ${data.x}`;

		var tierform = `${data.x}`;
	
		if(tierform=="Kreis"){
            document.getElementById("animal_img").innerHTML = '<img src="images/kreis.jpg" alt="" width="320" height="240" />';
            if(allowsound==true){
                    playCat();
		    allowsound=false;
            }
            
		}
		else if(tierform=="Katze"){
            document.getElementById("animal_img").innerHTML = '<img src="images/katze.jpg" alt="" width="320" height="240" />';
            if(allowsound==true){
                playCat();
		    allowsound=false;
            }
		}
		else if(tierform=="Elefant"){
            document.getElementById("animal_img").innerHTML = '<img src="images/elefant.jpg" alt="" width="320" height="240" />';
            if(allowsound==true){
                playElefant();
		    allowsound=false;
            }
		}
		
    });
    
    
    playStopButton.addEventListener("click", function (e) {
        allowsound = true;
    });
}

   
function playCat() {

    var context = new AudioContext();
    var sound = new Audio("sounds/katze.mp3");
    sound.crossOrigin = "anonymous";
    var source = context.createMediaElementSource(sound);
    source.connect(context.destination);

    sound.play();
}

  
function playElefant() {

    var context = new AudioContext();
    var sound = new Audio("sounds/elefant.mp3");
    sound.crossOrigin = "anonymous";
    var source = context.createMediaElementSource(sound);
    source.connect(context.destination);

    sound.play();
}

