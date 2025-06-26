function sendMessage() {
    const input = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    const query = input.value.trim();

    if (!query) return;

    // Display user message
    const userMessage = document.createElement('div');
    userMessage.className = 'message user-message';
    userMessage.textContent = query;
    chatBox.appendChild(userMessage);

    // Send query to backend
    fetch('/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query })
    })
    .then(response => response.json())
    .then(data => {
        // Display bot response
        const botMessage = document.createElement('div');
        botMessage.className = 'message bot-message';
        botMessage.textContent = data.response;
        chatBox.appendChild(botMessage);
        chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll
    })
    .catch(error => console.error('Error:', error));

    input.value = ''; // Clear input
}

// Allow pressing Enter to send message
document.getElementById('user-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') sendMessage();
});
