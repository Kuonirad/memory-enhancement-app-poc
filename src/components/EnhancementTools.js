/** @jsx h */
import { h } from "https://esm.sh/preact@10.5.15";
import { useState } from "https://esm.sh/preact@10.5.15/hooks";

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
    <div class="enhancement-tools-component">
      <button
        onClick={() => toggleTool("Categorize")}
        class={activeTools.includes("Categorize") ? "active" : ""}
      >
        Categorize
      </button>
      <button
        onClick={() => toggleTool("Visualize")}
        class={activeTools.includes("Visualize") ? "active" : ""}
      >
        Visualize
      </button>
      <button
        onClick={() => toggleTool("Associate")}
        class={activeTools.includes("Associate") ? "active" : ""}
      >
        Associate
      </button>
    </div>
  );
}

export default EnhancementTools;
