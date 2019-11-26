
window.onload=function(){
    var playStopButton = document.getElementById("playStopButton");
    var isPlaying = false;

    
    var context = new AudioContext();
    var sound = new Audio("sounds/katze.mp3");
    sound.crossOrigin = "anonymous";
    var source = context.createMediaElementSource(sound);
    source.connect(context.destination);

    playStopButton.addEventListener("click", playSound);
    sound.addEventListener("click", sound);
    
}


function playSound() {
    if (isPlaying) {
        sound.pause();
        playStopButton.innerHTML = "Play";
    } else {
        sound.play();
        playStopButton.innerHTML = "Stop";
    }

    isPlaying = !isPlaying;
}


function sound(){
    isPlaying = false;
    playStopButton.innerHTML = "Play";
}


