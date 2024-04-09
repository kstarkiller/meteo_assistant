function getServerUrl() {
    // Indiquer l'URL de base du serveur
    var serverUrl = 'report-gen.f3fdgrcvg7cgd2c3.francecentral.azurecontainer.io:8000'; 
    return serverUrl;
}

function displayLoadingMessage() {
    document.getElementById('loadingMessage').style.display = 'block';
}

function hideLoadingMessage() {
    document.getElementById('loadingMessage').style.display = 'none';
}

function updateAudioSourceAndDisplay() {
    var city = document.getElementById('city').value;
    var date = document.getElementById('date').value;
    var audioSource = document.getElementById('audioSource');
    var audioElement = document.getElementById('audioElement');

    // Utiliser la fonction getServerUrl pour obtenir l'URL de base du serveur
    audioSource.src = 'http://' + getServerUrl() + '/weather_request/?city=' + city + '&date=' + date;

    audioElement.onloadstart = function() {
        displayLoadingMessage();
    };

    audioElement.onloadeddata = function() {
        hideLoadingMessage();
        audioElement.style.display = 'block';
        audioElement.play();
    };

    audioElement.load();
}