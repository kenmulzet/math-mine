import React, { useState, useEffect } from "react";
import axios from 'axios';

function DynamicProblemForm({ mapNames }) {
  const [problemTypes, setProblemTypes] = useState({});
  const [category, setCategory] = useState("");
  const [counts, setCounts] = useState({});
  const [includeAnswers, setIncludeAnswers] = useState(false);

  useEffect(() => {
    (async () => {
      const types = {};
      for (const { value } of mapNames) {
        try {
          const res = await fetch(`/maps/${value}`);
          types[value] = res.ok
            ? Object.entries(await res.json()).map(([key, v]) => ({
                key,
                label: v.label
              }))
            : [];
        } catch (err) {
          console.error("Failed to load", value, err);
          types[value] = [];
        }
      }
      setProblemTypes(types);
    })();
  }, [mapNames]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const payload = { include_answers: includeAnswers };
    Object.entries(counts).forEach(([k, c]) => c > 0 && (payload[k] = c));
    console.log("Payload:", payload);
    // send to backend...
  };

  return (
    <form onSubmit={handleSubmit}>
      <select
        value={category}
        onChange={(e) => {
          setCategory(e.target.value);
          setCounts({});
        }}
      >
        <option value="">-- Choose --</option>
        {mapNames.map(({ label, value }) => (
          <option key={value} value={value}>
            {label}
          </option>
        ))}
      </select>

      {category &&
        problemTypes[category]?.map((pt) => (
          <div key={pt.key}>
            <label>{pt.label}</label>
            <input
              type="number"
              min="0"
              value={counts[pt.key] || ""}
              onChange={(e) =>
                setCounts({
                  ...counts,
                  [pt.key]: parseInt(e.target.value) || 0
                })
              }
            />
          </div>
        ))}

      <label>
        <input
          type="checkbox"
          checked={includeAnswers}
          onChange={(e) => setIncludeAnswers(e.target.checked)}
        />
        Include Answers
      </label>

      <button type="submit">Generate</button>
    </form>
  );
}

export default DynamicProblemForm;