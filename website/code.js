function initialize(){

    //Variablen deklarieren
    var allowsound = false;
    var playStopButton = document.getElementById("playStopButton");
    var socket = io.connect();
	
	socket.on("position", function(data){

		document.getElementById("label").innerHTML = `Tierform: ${data.x}`;

        //Daten von Python in Variable gespeichert
		var tierform = `${data.x}`;
	
		// if(tierform=="Kreis"){
        //     //Darstellen des Bildes Kreis
        //     document.getElementById("animal_img").innerHTML = '<img src="images/kreis.jpg" alt="" width="320" height="240" />';
        //     //Wenn Button gedrückt kann Sound abgespielt werden (Disablen vom Sound damit er nicht unendlich oft kommt)
        //     if(allowsound==true){
        //         playCat();
        //         allowsound=false;
        //     }
            
		// }
        if(tierform=="Katze"){
            //Darstellen des Bildes Katze
            document.getElementById("animal_img").innerHTML = '<img src="images/katze.jpg" alt="" width="320" height="240" />';
            //Enablen von Button Katze
            //document.getElementById("katze").disabled = false;
            //Wenn Button gedrückt kann Sound abgespielt werden (Disablen vom Sound damit er nicht unendlich oft kommt)
            if(allowsound==true){
                playCat();
                allowsound=false;
            }
		}
		else if(tierform=="Elefant"){
            //Darstellen des Bildes Elefant
            document.getElementById("animal_img").innerHTML = '<img src="images/elefant.jpg" alt="" width="320" height="240" />';
            //Enablen von Button Elefant
            //document.getElementById("elefant").disabled = false;
            //Wenn Button gedrückt kann Sound abgespielt werden (Disablen vom Sound damit er nicht unendlich oft kommt)
            if(allowsound==true){
                playElefant();
                allowsound=false;
            }
        }
        else if(tierform=="Ente"){
            //Darstellen des Bildes Elefant
            document.getElementById("animal_img").innerHTML = '<img src="images/ente.jpg" alt="" width="320" height="240" />';
            //Enablen von Button Elefant
            //document.getElementById("elefant").disabled = false;
            //Wenn Button gedrückt kann Sound abgespielt werden (Disablen vom Sound damit er nicht unendlich oft kommt)
            if(allowsound==true){
                playDuck();
                allowsound=false;
            }
		}
		
    });
    
    //Listener, damit GOOGLE erlaubt wird, das Sound abgespielt werden darf (BENUTZEREINGABE dank neuer RICHTLINIE)
    playStopButton.addEventListener("click", function (e) {
        allowsound = true;
    });
}
 
//Laden und abspielen vom Katzensound
function playCat() {

    var context = new AudioContext();
    var sound = new Audio("sounds/katze.mp3");
    sound.crossOrigin = "anonymous";
    var source = context.createMediaElementSource(sound);
    source.connect(context.destination);

    sound.play();
}
 
//Laden und abspielen vom Elefantensound
function playElefant() {

    var context = new AudioContext();
    var sound = new Audio("sounds/elefant.mp3");
    sound.crossOrigin = "anonymous";
    var source = context.createMediaElementSource(sound);
    source.connect(context.destination);

    sound.play();
}

//Laden und abspielen vom Katzensound
function playDuck() {

    var context = new AudioContext();
    var sound = new Audio("sounds/duck.mp3");
    sound.crossOrigin = "anonymous";
    var source = context.createMediaElementSource(sound);
    source.connect(context.destination);

    sound.play();
}

