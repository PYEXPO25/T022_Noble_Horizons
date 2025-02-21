document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("userInput").addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            event.preventDefault(); // Prevent default form submission
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
                let timetableMessage = `<p class="bot-message"><pre>${JSON.stringify(data, null, 2)}</pre></p>`;
                chatbox.innerHTML += timetableMessage;
                chatbox.scrollTop = chatbox.scrollHeight; // Auto-scroll
            })
            .catch(error => {
                chatbox.innerHTML += `<p class="bot-message">Error fetching timetable.</p>`;
            });
    } else {
        chatbox.innerHTML += `<p class="bot-message">I don't understand.</p>`;
    }

    document.getElementById("userInput").value = ""; // Clear input
    chatbox.scrollTop = chatbox.scrollHeight; // Auto-scroll
}
