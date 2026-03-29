import { useState } from 'react'
import './App.css'

function App() {
  const [form, setForm] = useState({
    sqft_living: "",
    bedrooms: "",
    bathrooms: "",
    floors: "",
    condition: "",
    yr_built: ""
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const res = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(form)
    });

    const data = await res.json();

    if (data.error) {
      alert(data.error);
    } else {
      setResult(data.predicted_price);
    }
  };

  return (
    <div>
      <h2>🏠 Prediksi Harga Rumah</h2>

      <form onSubmit={handleSubmit}>
        <input name="sqft_living" placeholder="Luas" onChange={handleChange} /><br/>
        <input name="bedrooms" placeholder="Kamar" onChange={handleChange} /><br/>
        <input name="bathrooms" placeholder="Bathroom" onChange={handleChange} /><br/>
        <input name="floors" placeholder="Floors" onChange={handleChange} /><br/>
        <input name="condition" placeholder="Condition" onChange={handleChange} /><br/>
        <input name="yr_built" placeholder="Tahun" onChange={handleChange} /><br/>

        <button type="submit">Prediksi</button>
      </form>

      {result && (
        <h3>💰 Harga: ${Number(result).toLocaleString()}</h3>
      )}
    </div>
  );
}

export default App
