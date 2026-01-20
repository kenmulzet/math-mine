import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import OutputLinks from "./OutputLinks";
import Histogram from "./Histogram";

function DynamicProblemForm({ mapNames }) {
  const [problemTypes, setProblemTypes] = useState({});
  const [category, setCategory] = useState("");
  const [counts, setCounts] = useState({});
  const [includeAnswers, setIncludeAnswers] = useState(false);
  const [outputFiles, setOutputFiles] = useState([]);
  const [answerFiles, setAnswerFiles] = useState([]);
  const [answerKeyFiles, setAnswerKeyFiles] = useState([]);
  const [includeNameDate, setIncludeNameDate] = useState(false);
  const [changeTitle, setChangeTitle] = useState(false);
  const [newTitle, setNewTitle] = useState("");
  const [problemCounts, setProblemCounts] = useState({});
  const [showHistogram, setShowHistogram] = useState(false);

  useEffect(() => {
    (async () => {
      const types = {};
      for (const { value } of mapNames) {
        try {
          const res = await fetch(`/maps/${value}?t=${Date.now()}`);
          console.log("value = ", value)
          if (res.ok) {
            const json = await res.json();
            console.log("json = ", json)
            types[value] = Object.entries(json).map(([key, v]) => ({
              key,
              label: typeof v === "string" ? v : v.label
            }));
          } else {
            types[value] = [];
          }
        } catch (err) {
          console.error("Failed to load", value, err);
          types[value] = [];
        }
      }
      setProblemTypes(types);
    })();
  }, [mapNames]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Case 1: No problem type selected
    if (!category) {
      alert("Please select a problem type before excavating.");
      return;
    }

    // Case 2: Zero problems selected
    const totalProblems = Object.values(counts).reduce((sum, val) => sum + val, 0);
    if (totalProblems === 0) {
      alert("Please select at least one problem before excavating.");
      return;
    }

    // Determine categoryName for default title
    const selectedMap = mapNames.find(m => m.value === category);
    const categoryName = selectedMap ? selectedMap.label : category;

    if (categoryName === "Calculus") {
      categoryName = "Calculus I"
    }

    // Build payload using snake_case
    const payload = {
      include_name_date: includeNameDate,
      change_title: changeTitle,
      title: changeTitle ? newTitle : `${categoryName} Worksheet`,
    };

    // Flatten counts into payload (only non‑zero)
    Object.entries(counts).forEach(([k, c]) => {
      if (c > 0) payload[k] = c;
    });

    console.log("category:", category)
    console.log("counts:", counts)
    console.log("Submitting payload:", payload);

    // ✅ Update React state with the flattened counts object
    setProblemCounts(counts);

    try {
      const res = await axios.post("http://localhost:8000/generate", payload)
      setOutputFiles(
        res.data.HTML_filename ? [res.data.HTML_filename] : []
      );

      setAnswerFiles(
        res.data.PDF_filename ? [res.data.PDF_filename] : []
      );

      setAnswerKeyFiles(
        res.data.Answer_key_filename ? [res.data.Answer_key_filename] : []
      );

    } catch (err) {
      console.error("Excavate failed", err);
    }
  };

  return (
    <div className="card p-4 shadow-sm">
      <form onSubmit={handleSubmit} className="mb-4">
        <div className="row mb-3">
          {/* Problem Type Column */}
          <div className="col-md-6 d-flex flex-column align-items-center">
            {/* Label above dropdown */}
            <label className="form-label fw-bold mb-2">Select Problem Type</label>
            <select
              value={category}
              onChange={(e) => {
                setCategory(e.target.value);
                setCounts({});

                // ✅ Clear old files when problem type changes
                setOutputFiles([]);
                setAnswerFiles([]);
                setAnswerKeyFiles([]);

                // ✅ Reset flags
                setIncludeAnswers(false);
                setIncludeNameDate(false);
                setChangeTitle(false);
                setShowHistogram(false);
                setNewTitle("");   // if you allow custom titles
              }}


              className="form-select w-auto mb-4"
            >
              <option value="">-- Choose --</option>
              {mapNames.map(({ label, value }) => (
                <option key={value} value={value}>
                  {label}
                </option>
              ))}
            </select>

            {/* Name/Date Boolean Selector */}
            <div className="form-check mb-4">
              <input
                type="checkbox"
                className="form-check-input"
                id="include_name_date"
                checked={includeNameDate}
                onChange={(e) => setIncludeNameDate(e.target.checked)}
              />
              <label className="form-check-label" htmlFor="include_name_date">
                Include Name/Date Line
              </label>
            </div>

            {/* Include Answers Checkbox */}
            <div className="form-check mb-4">
              <input
                type="checkbox"
                className="form-check-input"
                id="include_answers"
                checked={includeAnswers}
                onChange={(e) => setIncludeAnswers(e.target.checked)}
              />
              <label className="form-check-label" htmlFor="include_answers">
                Include Answers
              </label>
            </div>

            {/* Change Title Checkbox */}
            <div className="form-check mb-4">
              <input
                type="checkbox"
                className="form-check-input"
                id="change_title"
                checked={changeTitle}
                onChange={(e) => setChangeTitle(e.target.checked)}
              />
              <label className="form-check-label" htmlFor="change_title">
                Change Title (Leave blank for no title)
              </label>
            </div>

            {/* Conditionally render the input field */}
            {changeTitle && (
              <div className="text-center mb-4 w-100">
                <input
                  type="text"
                  className="form-control w-75 mx-auto"
                  placeholder="Enter new worksheet title"
                  value={newTitle}
                  onChange={(e) => setNewTitle(e.target.value)}
                />
              </div>
            )}
          </div>

          {/* Count Column */}
          <div className="col-md-6">
            {category && (
              <>
                {/* Centered Count heading */}
                <div className="text-center mb-3">
                  <label className="form-label fw-bold">Number of Problems</label>
                </div>

                {/* Inputs: label left, box right, vertically aligned */}
                {problemTypes[category]?.map((pt) => (
                  <div
                    key={pt.key}
                    className="d-flex justify-content-between align-items-center mb-3"
                  >
                    <label className="mb-0">{pt.label}</label>
                    <input
                      type="number"
                      min="0"
                      className="form-control w-25 text-end"
                      value={counts[pt.key] || ""}
                      onChange={(e) =>
                        setCounts({
                          ...counts,
                          [pt.key]: parseInt(e.target.value) || 0,
                        })
                      }
                    />
                  </div>
                ))}
              </>
            )}
          </div>
        </div>

        {/* Centered Excavate + Reset Buttons */}
        <div className="d-flex justify-content-center mt-4">
          <button type="submit" className="btn btn-primary px-4 me-3">
            Excavate
          </button>
          <button
            type="button"
            className="btn btn-secondary px-4"
            disabled={
              !category &&
              Object.keys(counts).length === 0 &&
              !includeNameDate &&
              !includeAnswers &&
              !changeTitle &&
              newTitle === "" &&
              outputFiles.length === 0 &&
              answerFiles.length === 0

            }
            onClick={() => {
              setCategory("");
              setCounts({});
              setIncludeNameDate(false);
              setIncludeAnswers(false);
              setChangeTitle(false);
              setNewTitle("");
              setOutputFiles([]);    // ✅ clears Your Files block
              setAnswerFiles([]);    // ✅ clears Your Files block
              setAnswerKeyFiles([]); // ✅ clears Your Files block
            }}
          >
            Reset
          </button>
        </div>

        {/* Show Histogram Checkbox */}
        <div className="d-flex justify-content-center mt-3">
          <button
            type="button"
            className="btn btn-info px-4"
            onClick={() => setShowHistogram(!showHistogram)}
            disabled={Object.keys(problemCounts).length === 0}
          >
            {showHistogram ? "Hide Histogram" : "Show Histogram"}
          </button>
        </div>
      </form>

      {/* Render output links below the form */}
      <OutputLinks files={outputFiles} answers={answerFiles} />

      {includeAnswers && answerKeyFiles.length > 0 && (
        <>
          <div className="mt-3">
            <h5>Answer Key</h5>
            {answerKeyFiles.map((file, idx) => (
              <a
                key={idx}
                href={`http://localhost:8000/static/${file}`}
                target="_blank"
                rel="noopener noreferrer"
              >
                Answer Key
              </a>
            ))}
          </div>
        </>
      )}

      {(outputFiles.length > 0 || answerFiles.length > 0 || answerKeyFiles.length > 0) && (
        <div className="mt-3">
          <button
            onClick={() =>
              window.open(
                `http://localhost:8000/download_all?pdf_filename=${answerFiles}&answer_filename=${answerKeyFiles}`
              )
            }
            className="btn btn-primary"
          >
            Download All
          </button>
        </div>
      )}

      {showHistogram && <Histogram data={problemCounts} />}

    </div>
  );
}

export default DynamicProblemForm;