document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("userInput").addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});

function sendMessage() {
    let userInput = document.getElementById("userInput").value.trim();
    let chatbox = document.getElementById("chatbox");

    if (userInput === "") return;

    let userMessage = `<p class="user-message">${userInput}</p>`;
    chatbox.innerHTML += userMessage;

    if (userInput.toUpperCase() === "TIMETABLE") {
        fetch("/api/timetable")
            .then(response => response.json())
            .then(data => {
                let timetableContent = document.getElementById("timetable-content");
                timetableContent.innerHTML = "<pre>" + JSON.stringify(data, null, 2) + "</pre>";
            });
    } else {
        chatbox.innerHTML += `<p class="bot-message">I don't understand.</p>`;
    }

    document.getElementById("userInput").value = "";
}
