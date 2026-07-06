const chatBox = document.getElementById("chat-box");
const input = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

function addMessage(text, sender) {
    const div = document.createElement("div");
    div.classList.add("message", sender);
    // preserve newlines from API response
    div.style.whiteSpace = "pre-wrap";
    div.textContent = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
    return div;
}

function showTyping() {
    const div = document.createElement("div");
    div.classList.add("message", "bot", "typing");
    div.innerHTML = "<span></span><span></span><span></span>";
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
    return div;
}

async function handleSend() {
    const message = input.value.trim();
    if (message === "") return;

    addMessage(message, "user");
    input.value = "";

    // disable while waiting
    sendBtn.disabled = true;
    input.disabled = true;

    const typingEl = showTyping();
    const reply = await sendMessage(message);
    typingEl.remove();

    addMessage(reply, "bot");

    sendBtn.disabled = false;
    input.disabled = false;
    input.focus();
}

sendBtn.addEventListener("click", handleSend);

input.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        handleSend();
    }
});