import React, { useState } from 'react';
import PropTypes from 'prop-types';

function MemoryInput({ addMemory }) {
  const [memory, setMemory] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (memory.trim() !== "") {
      addMemory(memory);
      console.log("Memory saved:", memory);
      setMemory("");
    }
  };

  return (
    <div className="memory-input-component">
      <form onSubmit={handleSubmit}>
        <textarea
          placeholder="Enter your memory here..."
          value={memory}
          onChange={(e) => setMemory(e.target.value)}
        ></textarea>
        <button type="submit">Save Memory</button>
      </form>
    </div>
  );
}

MemoryInput.propTypes = {
  addMemory: PropTypes.func.isRequired,
};

export default MemoryInput;
