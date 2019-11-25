//Sound funktioniert noch nicht
var playStopButton = document.getElementById("playStopButton");
var isPlaying = false;

var context = new AudioContext();
var sound = new Audio("sounds/katze.mp3");
sound.crossOrigin = "anonymous";
var source = context.createMediaElementSource(sound);
source.connect(context.destination);

playStopButton.addEventListener("click", function (e) {
    if (isPlaying) {
        sound.pause();
        playStopButton.innerHTML = "Play";
    } else {
        sound.play();
        playStopButton.innerHTML = "Stop";
    }

    isPlaying = !isPlaying;
});

sound.addEventListener("ended", function (e) {
    isPlaying = false;
    playStopButton.innerHTML = "Play";
});

