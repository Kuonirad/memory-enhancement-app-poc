/** @jsx h */
import { h } from "preact";
import { useState } from "preact/hooks";
import "./App.css";
import MemoryInput from "./components/MemoryInput.js";
import MemoryDisplay from "./components/MemoryDisplay.js";
import EnhancementTools from "./components/EnhancementTools.js";

function App() {
  return (
    <div class="App">
      <header class="App-header">
        <h1>Memory Enhancement App</h1>
      </header>
      <main class="App-main">
        <section class="memory-input">
          <h2>Input Memory</h2>
          <MemoryInput />
        </section>
        <section class="memory-display">
          <h2>Memory Display</h2>
          <MemoryDisplay />
        </section>
        <section class="memory-enhancement">
          <h2>Enhancement Tools</h2>
          <EnhancementTools />
        </section>
      </main>
      <footer class="App-footer">
        <p>
          &copy; {new Date().getFullYear()} Memory Enhancement App. All rights
          reserved.
        </p>
      </footer>
    </div>
  );
}

export default App;
