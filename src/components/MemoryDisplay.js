import React, { useState, useEffect } from 'react';

function MemoryDisplay() {
  const [memories, setMemories] = useState([]);

  useEffect(() => {
    // TODO: Implement fetching memories from storage
    setMemories(["Sample memory 1", "Sample memory 2"]);
  }, []);

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

export default MemoryDisplay;
