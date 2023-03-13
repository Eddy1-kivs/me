import React from 'react';
import { CircularProgressbar } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';

const ProgressBar = ({ percentage, text }) => {
  return (
    <div style={{ width: "130px" }}>
      <CircularProgressbar
        value={percentage}
        text={`${percentage}%`}
        strokeWidth={12}
        styles={{
          path: {
            stroke: `url(#gradient)`,
          },
        }}
      />
      <p>{text}</p>
      <svg width="0" height="0">
        <defs>
          <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stopColor="#AA367C" />
            <stop offset="100%" stopColor="#4A2FBD" />
          </linearGradient>
        </defs>
      </svg>
    </div>
  );
};

export default ProgressBar; 