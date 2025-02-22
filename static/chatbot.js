function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    document.getElementById("userInput").value = "";  // Clear the input field after sending the message

    // Display user input in the chatbox
    document.getElementById("chatbox").innerHTML += `<p class="user-message">${userInput}</p>`;

    // Handling different commands
    if (userInput.toLowerCase() === "timetable") {
        fetch('/api/timetable')
            .then(response => response.json())
            .then(data => {
                let timetableInfo = '';
                data.forEach(entry => {
                    timetableInfo += `<p><strong>${entry.day}</strong> from ${entry.start_time} to ${entry.end_time}: ${entry.subject} (Teacher: ${entry.teacher})</p><hr>`;
                });
                document.getElementById("chatbox").innerHTML += `<p class="bot-message">Here is your timetable: ${timetableInfo}</p>`;
            });
    }
    else if (userInput.toLowerCase() === "student data") {
        fetch('/api/student_data')
            .then(response => response.json())
            .then(data => {
                let studentInfo = '';
                data.forEach(student => {
                    studentInfo += `<p>Name: ${student.name}</p><p>Roll No: ${student.roll_no}</p><hr>`;
                });
                document.getElementById("chatbox").innerHTML += `<p class="bot-message">Here is the student data: ${studentInfo}</p>`;
            });
    }
    else if (userInput.toLowerCase() === "canteen data") {
        fetch('/api/canteen_data')
            .then(response => response.json())
            .then(data => {
                let canteenInfo = '';
                data.forEach(item => {
                    canteenInfo += `<p>Item: ${item.food_item}</p><p>Price: ${item.price}</p><hr>`;
                });
                document.getElementById("chatbox").innerHTML += `<p class="bot-message">Here is the canteen menu: ${canteenInfo}</p>`;
            });
    }
    else {
        // Default response for unrecognized input
        document.getElementById("chatbox").innerHTML += `<p class="bot-message">Sorry, I didn't understand that. Try asking for 'TIMETABLE', 'STUDENT DATA', or 'CANTEEN DATA'.</p>`;
    }

    // Scroll to the latest message
    const chatbox = document.getElementById("chatbox");
    chatbox.scrollTop = chatbox.scrollHeight;
}
