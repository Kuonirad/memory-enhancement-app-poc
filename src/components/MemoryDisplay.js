import React from 'react';
import PropTypes from 'prop-types';

function MemoryDisplay({ memories }) {
  return (
    <div className="memory-display-component">
      <ul>
        {memories.map((memory, index) => (
          <li key={index}>{memory}</li>
        ))}
      </ul>
    </div>
  );
}

MemoryDisplay.propTypes = {
  memories: PropTypes.arrayOf(PropTypes.string).isRequired,
};

export default MemoryDisplay;
