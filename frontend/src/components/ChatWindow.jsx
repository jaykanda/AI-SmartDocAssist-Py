import { useState } from 'react'
import { userPrompt } from '../services/api';

function ChatWindow() {
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");
    const [sources, setSources] = useState([]);
    const [loading, setLoading] = useState(false);

    const handleAsk = async () => {
        if (!question.trim()) return;
        setLoading(true);
        setAnswer("");

        try {
            const result = await userPrompt(question);
            setAnswer(result.answer);
            setSources(result.sources);
        } catch (error) {
            console.error(error);
            setAnswer("Something went wrong. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ padding: "40px" }}>
            <h1>AI Smart Document Assistant</h1>
            <p>Please query about policy documents</p>
            <input type="text" value={question} onChange={(e) => setQuestion(e.target.value)}
                placeholder="Ask your question..." style={{ width: "400px", padding: "10px" }}
            />
            <button style={{ padding: "10px", margin: "10px" }} onClick={handleAsk} disabled={loading}>
                {loading ? "Processing..." : "Ask AI"}
            </button>
            {
                answer ? (
                    <div style={{ marginTop: "30px" }}>
                <h5>AI Bot says</h5>
                <p>{answer}</p>
                {/* <h4>Source Documents</h4>
                {sources.map((source, index) => (
                    <p key={index}>{source}</p>
                ))} */}
            </div>
                ) : (<div>&nbsp;</div>)
            }
            
        </div>
    );
}

export default ChatWindow;