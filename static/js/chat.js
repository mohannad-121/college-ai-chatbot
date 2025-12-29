function sendMessage() {
    const input = document.getElementById("msg");
    const message = input.value;

    fetch("/api/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("chat-box").innerHTML +=
            "<p><b>You:</b> " + message + "</p>" +
            "<p><b>Bot:</b> " + data.reply + "</p>";
        input.value = "";
    });
}

function startVoice() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";

    recognition.onresult = function(event) {
        document.getElementById("msg").value = event.results[0][0].transcript;
        sendMessage();
    };

    recognition.start();
}
