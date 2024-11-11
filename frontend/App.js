import React, { useState } from "react";

function App() {
  const [patentId, setPatentId] = useState("");
  const [companyName, setCompanyName] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult(null);
    setError(null);

    try {
      const res = await fetch("http://localhost:5000/check_infringement", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ patent_id: patentId, company_name: companyName }),
      });

      if (!res.ok) {
        throw new Error("Failed to fetch");
      }

      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div>
      <h1>Patent Infringement Check</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Patent ID"
          value={patentId}
          onChange={(e) => setPatentId(e.target.value)}
        />
        <input
          type="text"
          placeholder="Company Name"
          value={companyName}
          onChange={(e) => setCompanyName(e.target.value)}
        />
        <button type="submit">Check Infringement</button>
      </form>

      {error && <p>{error}</p>}

      {result && (
        <div>
          <h2>Infringement Analysis for {result.company_name}</h2>
          <ul>
            {result.top_infringing_products.map((product) => (
              <li key={product.product_name}>
                <h3>{product.product_name}</h3>
                <p>Infringement Likelihood: {product.infringement_likelihood}</p>
                <p>Explanation: {product.explanation}</p>
                <p>Relevant Claims: {product.relevant_claims.join(", ")}</p>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
