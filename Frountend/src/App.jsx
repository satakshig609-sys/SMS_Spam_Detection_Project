import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState("");

  const checkMessage = async () => {
    if (!message.trim()) {
      setResult("Please enter a message");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: message,
        }),
      });

      const data = await response.json();
      setResult(data.prediction);
    } catch (error) {
      setResult("Unable to connect to backend");
    }
  };

  const clearMessage = () => {
    setMessage("");
    setResult("");
  };

  return (
    <div className="app">

      {/* Decorative background */}
      <div className="circle circle-one"></div>
      <div className="circle circle-two"></div>

      <div className="main-container">

        {/* Left Features */}
        <div className="features">

          <div className="feature">
            <div className="feature-icon">✓</div>
            <div>
              <h3>Detect Spam<br />Messages</h3>
              <p>
                Keep your inbox safe<br />
                from unwanted messages.
              </p>
            </div>
          </div>

          <div className="feature">
            <div className="feature-icon">ϟ</div>
            <div>
              <h3>Fast & Accurate<br />Prediction</h3>
              <p>
                Get reliable results<br />
                in seconds.
              </p>
            </div>
          </div>

          <div className="feature">
            <div className="feature-icon">♙</div>
            <div>
              <h3>Your Privacy<br />Matters</h3>
              <p>
                Your data stays safe<br />
                and secure.
              </p>
            </div>
          </div>

        </div>

        {/* Main Card */}
        <div className="card">

          <div className="mail-icon">✉</div>

          <h1>SMS Spam Detector</h1>

          <p className="subtitle">
            Quickly. Simple. Secure.
          </p>

          <textarea
            placeholder="Enter your SMS here..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />

          <div className="buttons">

            <button
              className="check-btn"
              onClick={checkMessage}
            >
              <span>⌕</span>
              Check Message
            </button>

            <button
              className="clear-btn"
              onClick={clearMessage}
            >
              <span>♜</span>
              Clear
            </button>

          </div>

          <div className="result">

            {result ? (
              <h2
                className={
                  result === "SPAM" ? "spam" : "ham"
                }
              >
                {result}
              </h2>
            ) : (
              <>
                <div className="info-icon">i</div>
                <p>Result will appear here...</p>
              </>
            )}

          </div>

        </div>

      </div>
    </div>
  );
}

export default App;