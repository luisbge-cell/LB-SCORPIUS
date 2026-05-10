async function sendMessage() {
    const input = document.getElementById('user-input');
    const chat = document.getElementById('chat-window');
    const msg = input.value;
    if(!msg) return;

    chat.innerHTML += `<p style="color:#888"><strong>Tú:</strong> ${msg}</p>`;
    input.value = '';

    const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ message: msg })
    });
    const data = await response.json();
    chat.innerHTML += `<p style="color:#ff3131"><strong>SCORPIUS:</strong> ${data.response}</p>`;
    chat.scrollTop = chat.scrollHeight;
}
