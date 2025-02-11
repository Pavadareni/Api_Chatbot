# GUIDE FOR CHATBOT IMPLEMENTATION USING GEMINI API
## 1. Clone the Repository.
- Clone the repository using the command in Command Prompt  
   ```
  git clone https://github.com/Pavadareni/Api_Chatbot.git
   ```
   
- Move to the working directory by:  
    ```
    cd Api_Chatbot 
    ```
    
## 2. Start the backend server
- Open a terminal, and move to the backend directory using the command
  ```
   cd chatbot-backend\backend
  ```    
  
- Initialize and Install the dependencies by:   
  ```
   npm init    
   npm install
  ```
 
- Run the server file by:      
  ```
  node index.js
  ```
    
## 3. Get The Gemini API Key
- Get Your Gemini API Key at:  
   [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

- Create an environment file named ```.env``` in API_Chatbot directory.   
  Copy and paste the API Key in .env file
  ```
   GEMINI_API_KEY = "your key"
  ```
  
### 4. Start the API Server
- Open a new terminal and move to api directory by:
  ```
  cd api
  ```

- Install Requirements by :    
  ```
  pip install -r requiremnts.txt
  ```

- Start the Flask server by:    
  ```
  python api.py
  ```

### 5. Start the frontend server
- Open a new terminal, and move to the frontend directotry:
  
  ```
  cd talktome
  ```

- Initialize the node package and install dependencies by:
    
  ```
  npm init  
  npm install  
  ```

- Run the frontend by the command:
  
  ```
  npm run dev 
  ```

- Go the link provided by react vite to see the frontend :
    [http://localhost:5173/](http://localhost:5173/)
    
