import React, { useState, useEffect } from 'react';
import "./App.css";
import MemoryInput from "./components/MemoryInput.js";
import MemoryDisplay from "./components/MemoryDisplay.js";
import EnhancementTools from "./components/EnhancementTools.js";

function App() {
  const [memories, setMemories] = useState([]);

  useEffect(() => {
    const storedMemories = JSON.parse(localStorage.getItem('memories') || '[]');
    setMemories(storedMemories);
  }, []);

  const addMemory = (memory) => {
    const updatedMemories = [...memories, memory];
    setMemories(updatedMemories);
    localStorage.setItem('memories', JSON.stringify(updatedMemories));
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Memory Enhancement App</h1>
      </header>
      <main className="App-main">
        <section className="memory-input">
          <h2>Input Memory</h2>
          <MemoryInput addMemory={addMemory} />
        </section>
        <section className="memory-display">
          <h2>Memory Display</h2>
          <MemoryDisplay memories={memories} />
        </section>
        <section className="memory-enhancement">
          <h2>Enhancement Tools</h2>
          <EnhancementTools />
        </section>
      </main>
      <footer className="App-footer">
        <p>
          &copy; {new Date().getFullYear()} Memory Enhancement App. All rights
          reserved.
        </p>
      </footer>
    </div>
  );
}

export default App;
