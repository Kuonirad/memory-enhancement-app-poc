import unittest
from quantum_inspired_optimization import QuantumInspiredOptimizer, quantum_inspired_memory_optimization

class TestQuantumInspiredOptimization(unittest.TestCase):
    def setUp(self):
        self.optimizer = QuantumInspiredOptimizer(num_qubits=3)

    def test_create_circuit(self):
        circuit = self.optimizer.create_circuit()
        self.assertEqual(circuit.num_qubits, 3)
        self.assertEqual(len(circuit.data), 7)  # 3 Hadamard gates + 4 measurement operations

    def test_run_circuit(self):
        circuit = self.optimizer.create_circuit()
        counts = self.optimizer.run_circuit(circuit)
        self.assertEqual(sum(counts.values()), self.optimizer.num_shots)

    def test_interpret_results(self):
        counts = {'000': 500, '111': 300, '101': 200}
        results = self.optimizer.interpret_results(counts)
        self.assertEqual(len(results), 3)
        self.assertAlmostEqual(results[0][1], 0.5)
        self.assertAlmostEqual(results[1][1], 0.3)
        self.assertAlmostEqual(results[2][1], 0.2)

    def test_optimize_memory_task(self):
        strategy = self.optimizer.optimize_memory_task(0.5)
        self.assertIn(strategy, [
            "Chunking", "Mnemonic Devices", "Mind Mapping", "Spaced Repetition",
            "Method of Loci", "Elaborative Rehearsal", "Dual Coding", "Active Recall"
        ])

    def test_quantum_inspired_memory_optimization(self):
        result = quantum_inspired_memory_optimization("Test task", 0.7)
        self.assertIsInstance(result, str)
        self.assertIn("Test task", result)
        self.assertIn("0.7", result)
        self.assertIn("optimized memory enhancement strategy is:", result)

if __name__ == '__main__':
    unittest.main()
