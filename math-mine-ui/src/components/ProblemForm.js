import React, { useState } from 'react';
import axios from 'axios';

function ProblemForm({ setOutputFiles, setAnswerFiles }) {
  const [topic, setTopic] = useState('');
  const [count, setCount] = useState(5);
  const [include_answers, setIncludeAnswers] = useState(false);


  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/generate', {
        topic: topic,
        count: count,
        include_answers: include_answers, 
      });

      // Backend returns { files: [...], answers: [...] }
      setOutputFiles(response.data.files || []);
      setAnswerFiles(response.data.answers || []);
    } catch (error) {
      console.error("Error generating problems:", error);
    }
  };

  return (
    <div className="card p-4 shadow-sm">
      <form onSubmit={handleSubmit} className="mb-4">
        <div className="row mb-3 text-center">
          {/* Problem Type Column */}
          <div className="col-md-6 d-flex flex-column align-items-center">
            <label className="form-label">Select Problem Type</label>
            <select
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
              className="form-select w-75"
            >
              <option value="" disabled>-- Choose --</option>
              <option value="algebra">Algebra</option>
              <option value="geometry">Geometry</option>
              <option value="calculus">Calculus I</option>
              <option value="diffeq">Differential Equations</option>
            </select>
          </div>

          {/* Count Column */}
          <div className="col-md-6 d-flex flex-column align-items-center">
            <label className="form-label">Count</label>
            <input
              type="number"
              value={count}
              onChange={(e) => setCount(e.target.value)}
              className="form-control w-50 text-center"
            />
          </div>
        </div>

        {/* Include Answers Checkbox */}
        <div className="text-center mb-4">
          <div className="form-check d-inline-block">
            <input
              type="checkbox"
              className="form-check-input"
              id="include_answers"
              checked={include_answers}
              onChange={(e) => setIncludeAnswers(e.target.checked)}
            />
            <label className="form-check-label" htmlFor="include_answers">
              Include Answers
            </label>
          </div>
        </div>

        {/* Centered Excavate Button */}
        <div className="text-center mt-4">
          <button type="submit" className="btn btn-primary px-4">
            Excavate
          </button>
        </div>
      </form>
    </div>
  );
  
}

export default ProblemForm;