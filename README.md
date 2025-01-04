# 🖐 Motion Cast

An interactive application that connects the **frontend** and **backend** to capture and replicate hand movements in real-time using modern technologies.

## 📖 About the Project

**Motion Cast** is an innovative project that:

- Uses the **backend** to capture the user's hand movements through the webcam.
- Synchronizes the captured movements with the **frontend**, where they are represented by a 3D-rendered hand in real-time.

The main goal is to demonstrate the interaction between computer vision and 3D graphics in a practical and engaging application.

---

## 🛠 Technologies Used

### Frontend
- React
- Three.js
- WebSocket

### Backend
- Python
- OpenCV (for hand movement detection)
- WebSocket

---

## 🚀 How to Run Motion Cast

### Prerequisites

- Node.js (for the frontend)
- Python 3.8 or higher (for the backend)
- A Python package manager (like pip)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/motion-cast.git
   cd motion-cast
   ```

2. Install the backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Install the frontend dependencies:
   ```bash
   cd ../frontend
   npm install
   # or
   yarn install
   ```

### Running Motion Cast

1. Start the backend:
   ```bash
   cd backend
   python app.py
   ```

2. In another terminal, start the frontend:
   ```bash
   cd frontend
   npm start
   # or
   yarn start
   ```

3. Access the frontend in your browser:
   ```
   http://localhost:5173
   ```

Now you can explore **Motion Cast** and see the virtual hand in your browser following your real hand movements captured by the webcam!

---

## 🧪 Features

- **Movement Detection**: The backend captures hand movements via the webcam.
- **Real-Time Synchronization**: Data is sent to the frontend via WebSocket.
- **3D Representation**: The frontend displays movements in a 3D-rendered virtual hand.

---

## 📂 Repository Structure

```
.
├── backend/           # Backend application code in Python
│   ├── app.py         # Main backend file
│   ├── requirements.txt # Backend dependencies
├── frontend/          # Frontend application code in React
│   ├── public/        # React public files
│   ├── src/           # React source code
│   ├── package.json   # Frontend dependencies
└── README.md          # Project documentation
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

--- 

Let me know if you'd like further refinements! 😊
