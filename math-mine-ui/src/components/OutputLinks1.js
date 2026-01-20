import React from 'react';

function OutputLinks({ files, answers }) {
  return (
    <div>
      {/* Worksheets Section */}
      <h4>Worksheets</h4>
      <ul className="list-group mb-3">
        {files.map((file, idx) => (
          <li key={idx} className="list-group-item">
            <a href={file} target="_blank" rel="noopener noreferrer">
              {file}
            </a>
          </li>
        ))}
      </ul>

      {/* Conditionally Render Answer Keys */}
      {answers && answers.length > 0 && (
        <>
          <h4>Answer Key PDFs</h4>
          <ul className="list-group">
            {answers.map((file, idx) => (
              <li key={idx} className="list-group-item">
                <a href={file} target="_blank" rel="noopener noreferrer">
                  {file}
                </a>
              </li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
}

export default OutputLinks;