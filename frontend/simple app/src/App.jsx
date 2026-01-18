import { useState } from "react";
import "./App.css";

function App() {
  const [num, setNum] = useState("");
  const [sum, setSum] = useState(null);

  const handleOnChange = (e) => {
    setNum(e.target.value);
    //setNum("");
  };
  const handleSubmit = async () => {
    if (num === "" || num === null) {
      alert("Please enter a number");
      return;
    }
    const response = await fetch("http://127.0.0.1:8000/submit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        num: Number(num),
      }),
    });

    const data = await response.json();
    console.log(data);
    setSum(data.sum);
    setNum("");
  };
  return (
    <div className="main">
      <div className="box">
        <h2 className="heading">WELCOME TO SIMPLE APP</h2>
        <label className="label">Enter a number:</label>
        <input
          type="number"
          value={num}
          placeholder="Enter a number"
          onChange={handleOnChange}
        />
        <br />
        <button className="btn" onClick={handleSubmit}>
          SUBMIT
        </button>
        <h3 style={{ visibility: sum === null ? "hidden" : "visible" }}>
          Total sum : {sum}
        </h3>
      </div>
    </div>
  );
}

export default App;
