require("dotenv").config();
const express = require("express");
const cors = require("cors");
const axios = require("axios");

const app = express();
app.use(cors());
app.use(express.json());

const FLASK_API_URL = "http://127.0.0.1:8080/chat"; 

app.post("/api/chat", async (req, res) => {
  try {
    const { message } = req.body;
    const response = await axios.post(FLASK_API_URL, { message });
    
    if (response.data.error) {
      throw new Error(response.data.error);
    }

    res.json({ reply: response.data.reply });
  } catch (error) {
    console.error("Error:", error.message);
    res.status(500).json({ error: "Error processing request" });
  }
});

const PORT = process.env.PORT || 5050;
app.listen(PORT, () => console.log(`Backend running on port ${PORT}`));
