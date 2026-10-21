import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState(true);

  const BASE_URL = "http://localhost:8000";

  useEffect(() => {
    const currentPath = window.location.pathname;
    fetch(`${BASE_URL}${currentPath}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Gagal mengambil data");
        }
        return response.json();
      })
      .then((data) => {
        setData(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error:", error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading data...</p>;

  return (
    <>
      <div>
        <h1>Respons from backend</h1>
        <p>{data}</p>
      </div>
    </>
  );
}

export default App;
