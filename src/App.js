import React from 'react';
import "./App.css";
import MemoryInput from "./components/MemoryInput.js";
import MemoryDisplay from "./components/MemoryDisplay.js";
import EnhancementTools from "./components/EnhancementTools.js";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Memory Enhancement App</h1>
      </header>
      <main className="App-main">
        <section className="memory-input">
          <h2>Input Memory</h2>
          <MemoryInput />
        </section>
        <section className="memory-display">
          <h2>Memory Display</h2>
          <MemoryDisplay />
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
