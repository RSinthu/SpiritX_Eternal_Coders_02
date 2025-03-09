
import React, { useState } from "react";
import axios from "axios";
import "./ChatBot.css"; 

const CustomChatBot = () => {
  interface Message {
    text: string;
    sender: "user" | "bot";
  }

  const [messages, setMessages] = useState<Message[]>([]);
  const [inputMessage, setInputMessage] = useState<string>("");

  const handleSendMessage = async () => {
    if (!inputMessage.trim()) return; 

  
    setMessages([...messages, { text: inputMessage, sender: "user" }]);
    setInputMessage(""); 
    
    try {
      const apiUrl:string = import.meta.env.VITE_API_URL;

      const response = await axios.post(`${apiUrl}/chats`, {
        question: inputMessage,
      });

      setMessages((prevMessages) => [
        ...prevMessages,
        { text: response.data.response, sender: "bot" },
      ]);
    } catch (error) {
      console.error("Error sending message:", error);
      setMessages((prevMessages) => [
        ...prevMessages,
        { text: "Sorry, there was an error. Please try again.", sender: "bot" },
      ]);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter") {
      handleSendMessage();
    }
  };

  return (
    <div className="chatbot-container">
      <div className="chatbox">
        <div className="messages">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`${message.sender === "user" ? "user" : "bot"}`}
            >
              {message.text}
            </div>
          ))}
        </div>
        <div className="input-container">
          <input
            type="text"
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Type your message..."
          />
          <button onClick={handleSendMessage}>Send</button>
        </div>
      </div>
    </div>
  );
};

export default CustomChatBot;