import { h } from "preact";
import { useState, useEffect } from "preact/hooks";

function MemoryDisplay() {
  const [memories, setMemories] = useState([]);

  useEffect(() => {
    // TODO: Implement fetching memories from storage
    setMemories(["Sample memory 1", "Sample memory 2"]);
  }, []);

  return (
    <div class="memory-display-component">
      <ul>
        {memories.map((memory, index) => (
          <li key={index}>{memory}</li>
        ))}
      </ul>
    </div>
  );
}

export default MemoryDisplay;
