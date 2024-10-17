import React, { useState } from 'react';

function EnhancementTools() {
  const [activeTools, setActiveTools] = useState([]);

  const toggleTool = (tool) => {
    setActiveTools((prevTools) =>
      prevTools.includes(tool)
        ? prevTools.filter((t) => t !== tool)
        : [...prevTools, tool]
    );
  };

  return (
    <div className="enhancement-tools-component">
      <button
        onClick={() => toggleTool("Categorize")}
        className={activeTools.includes("Categorize") ? "active" : ""}
      >
        Categorize
      </button>
      <button
        onClick={() => toggleTool("Visualize")}
        className={activeTools.includes("Visualize") ? "active" : ""}
      >
        Visualize
      </button>
      <button
        onClick={() => toggleTool("Associate")}
        className={activeTools.includes("Associate") ? "active" : ""}
      >
        Associate
      </button>
    </div>
  );
}

export default EnhancementTools;
