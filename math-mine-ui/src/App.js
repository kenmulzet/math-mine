import React, { useState } from 'react';
import DynamicProblemForm from './components/DynamicProblemForm';
import OutputLinks from './components/OutputLinks';

function App() {
  const [outputFiles, setOutputFiles] = useState([]);
  const [answerFiles, setAnswerFiles] = useState([]);

  const mapNames = [
    { label: "Algebra", value: "algebra_map.json" },
    { label: "Geometry", value: "geometry_map.json" },
    { label: "Calculus I", value: "calculus_map.json" },
    { label: "Differential Equations", value: "diffeq_map.json" }
  ];


  return (
    <div className="container py-5">

      <h1 className="text-center mb-5">⛏️ Math Mine 💎</h1>

      <div className="container mt-5">
        <h2 className="mb-4 text-center">Practice Worksheet Generator</h2>
        <DynamicProblemForm mapNames={mapNames} setOutputFiles={setOutputFiles} setAnswerFiles={setAnswerFiles} />
        <OutputLinks files={outputFiles} answers={answerFiles} />
      </div>
    </div>
  );
}

export default App;