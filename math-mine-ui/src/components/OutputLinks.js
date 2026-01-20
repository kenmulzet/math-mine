import React from 'react';

function OutputLinks({ files = [], answers = [] }) {
  if (files.length === 0 && answers.length === 0) return null;

  return (
    <div className="mt-4">
      <h4>Your Files</h4>
      <ul className="list-group">
        {files.length > 0 && (
          <li className="list-group-item">
            <a
              href={`http://localhost:8000/static/${files[0]}`}
              target="_blank"
              rel="noopener noreferrer"
            >
              📄 Worksheet (HTML)
            </a>
          </li>
        )}
        {answers.length > 0 && (
          <li className="list-group-item">
            <a
              href={`http://localhost:8000/static/${answers[0]}`}
              target="_blank"
              rel="noopener noreferrer"
            >
              📝 Worksheet (PDF)
            </a>
          </li>
        )}
      </ul>
    </div>
  );
}

export default OutputLinks;