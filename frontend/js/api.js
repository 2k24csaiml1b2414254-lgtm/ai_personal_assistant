const BASE_URL = "http://127.0.0.1:8000";

async function sendMessage(message) {
    try {
        const response = await fetch(`${BASE_URL}/chat`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        if (!response.ok) {
            return "Server error: " + response.status;
        }

        const data = await response.json();

        return data.response;

    } catch (error) {
        console.error(error);
        return "Something went wrong!";
    }
}