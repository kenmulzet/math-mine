import React, { useRef, useEffect } from "react";
import { Chart } from "chart.js/auto";

export default function Histogram({ data }) {
  const canvasRef = useRef(null);

  useEffect(() => {
    if (!canvasRef.current || !data || Object.keys(data).length === 0) return;

    const ctx = canvasRef.current.getContext("2d");

    const chart = new Chart(ctx, {
      type: "bar",
      data: {
        labels: Object.keys(data),
        datasets: [
          {
            label: "Problem Counts",
            data: Object.values(data),
            backgroundColor: "rgba(75, 192, 192, 0.6)",
          },
        ],
      },
      options: {
        responsive: true,
        plugins: { legend: { display: false } },
      },
    });

    return () => chart.destroy();
  }, [data]);

  return (
    <div className="card mt-4 shadow-sm mx-auto" style={{ maxWidth: "800px", maxHeight: "600px" }}>
      <div className="card-body">
        <h5 className="card-title text-center mb-3">Problem Distribution</h5>
        <canvas ref={canvasRef} className="w-100" height="500" />
      </div>
    </div>
  );
}