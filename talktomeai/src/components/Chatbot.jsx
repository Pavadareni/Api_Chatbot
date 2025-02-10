import React, { useState } from "react";
import { Send } from "lucide-react";
import "./Chatbot.css";
import { sendMessageToChatbot } from "../apiService"; // Import the API service

const ChatBot = () => {
  const [messages, setMessages] = useState([
    { text: "Hello! How can I help you today?", sender: "bot" },
  ]);
  const [input, setInput] = useState("");

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = { text: input, sender: "user" };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");

    try {
      const botReply = await sendMessageToChatbot(input);
      setMessages((prev) => [...prev, { text: botReply, sender: "bot" }]);
    } catch (error) {
      setMessages((prev) => [...prev, { text: "Error: Unable to reach chatbot.", sender: "bot" }]);
    }
  };

  return (
    <div>
      <h1 className="heading">Talk to me AI</h1>
      <div className="chat-container">
        <div className="chat-header">ChatBot</div>
        <div className="chat-messages">
          {messages.map((msg, index) => (
            <div key={index} className={`chat-bubble ${msg.sender}`}>
              {msg.text}
            </div>
          ))}
        </div>
        <div className="chat-input-container">
          <input
            type="text"
            className="chat-input"
            placeholder="Type a message..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
          />
          <button className="chat-send-button" onClick={handleSend}>
            <Send size={20} />
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatBot;
