const API_URL = "http://localhost:8000";

export async function userPrompt(question) {
    const response = await fetch(`${API_URL}/userprompt`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question: question
        })
    });

    if (!response.ok) {
        throw new Error("Unable to process your question");
    }

    return await response.json();
}