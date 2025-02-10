const API_URL = "http://localhost:5050/api/chat"; // Express backend URL

export const sendMessageToChatbot = async (message) => {
  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    return data.reply;
  } catch (error) {
    console.error("Chatbot API Error:", error);
    return "Error connecting to chatbot. Please try again.";
  }
};
