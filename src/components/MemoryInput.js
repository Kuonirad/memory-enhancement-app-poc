import { h } from "preact";
import { useState } from "preact/hooks";

function MemoryInput() {
  const [memory, setMemory] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    // TODO: Implement memory saving logic
    console.log("Memory saved:", memory);
    setMemory("");
  };

  return (
    <div class="memory-input-component">
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

export default MemoryInput;
