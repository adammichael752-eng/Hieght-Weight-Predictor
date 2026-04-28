import { useState } from "react";
import axios from "axios";

export default function App() {
  const [age, setAge] = useState(10);
  const [height, setHeight] = useState(138);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const predict = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await axios.post("/api/predict", { age, height });
      setResult(res.data);
    } catch {
      setError("Could not connect to backend. Make sure the Python server is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "40px", maxWidth: "400px", margin: "0 auto", fontFamily: "sans-serif" }}>
      <h1>Height & Weight Predictor</h1>

      <label>Age: {age}</label>
      <br />
      <input
        type="range"
        min="5"
        max="100"
        value={age}
        onChange={(e) => setAge(Number(e.target.value))}
        style={{ width: "100%", margin: "12px 0" }}
      />

      <label>Height: {height} cm</label>
      <br />
      <input
        type="range"
        min="50"
        max="220"
        value={height}
        onChange={(e) => setHeight(Number(e.target.value))}
        style={{ width: "100%", margin: "12px 0" }}
      />

      <button onClick={predict} disabled={loading} style={{ padding: "8px 20px", cursor: "pointer" }}>
        {loading ? "Predicting..." : "Predict"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h2>Weight: {result.weight} kg</h2>
        </div>
      )}
    </div>
  );
}
