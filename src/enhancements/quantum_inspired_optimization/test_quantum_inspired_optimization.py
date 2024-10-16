import unittest
import numpy as np
from unittest.mock import patch, MagicMock
import warnings
from src.enhancements.quantum_inspired_optimization.quantum_inspired_optimization import QuantumInspiredOptimizer, quantum_inspired_memory_optimization
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from scipy.optimize import minimize

class TestQuantumInspiredOptimization(unittest.TestCase):
    def setUp(self):
        self.optimizer = QuantumInspiredOptimizer(num_qubits=3, p=2)

    def test_create_circuit(self):
        beta = [0.1, 0.2]
        gamma = [0.3, 0.4]
        circuit = self.optimizer.create_circuit(beta, gamma)
        self.assertEqual(circuit.num_qubits, 3)
        self.assertGreater(len(circuit.data), 7)  # Should have more gates than just Hadamard and measurement

    def test_apply_cost_hamiltonian(self):
        circuit = QuantumCircuit(3)
        self.optimizer._apply_cost_hamiltonian(circuit, 0.5)
        self.assertGreater(len(circuit.data), 0)

    def test_apply_mixing_hamiltonian(self):
        circuit = QuantumCircuit(3)
        self.optimizer._apply_mixing_hamiltonian(circuit, 0.5)
        self.assertEqual(len(circuit.data), 3)  # Should apply RX gate to each qubit

    def test_compute_expectation(self):
        counts = {'000': 500, '111': 300, '101': 200}
        expectation = self.optimizer._compute_expectation(counts)
        self.assertIsInstance(expectation, float)
        self.assertGreaterEqual(expectation, 0)

    @patch('src.enhancements.quantum_inspired_optimization.quantum_inspired_optimization.minimize')
    def test_optimize_memory_task(self, mock_minimize):
        mock_minimize.return_value = MagicMock(x=np.array([0.1, 0.2, 0.3, 0.4]))
        self.optimizer.backend = MagicMock()
        self.optimizer.backend.run.return_value.result.return_value.get_counts.return_value = {'000': 500, '111': 300, '101': 200}

        result = self.optimizer.optimize_memory_task(0.5)
        self.assertIsInstance(result, dict)
        self.assertIn('state', result)
        self.assertIn('task_complexity', result)
        self.assertIn('selected_strategy', result)
        self.assertIn(result['selected_strategy'], [
            "Chunking", "Mnemonic Devices", "Mind Mapping", "Spaced Repetition",
            "Method of Loci", "Elaborative Rehearsal", "Dual Coding", "Active Recall"
        ])

    @patch('src.enhancements.quantum_inspired_optimization.quantum_inspired_optimization.QuantumInspiredOptimizer')
    def test_quantum_inspired_memory_optimization(self, mock_optimizer):
        mock_optimizer.return_value.optimize_memory_task.return_value = {
            'state': '111',
            'task_complexity': 0.7,
            'selected_strategy': 'Chunking'
        }
        result = quantum_inspired_memory_optimization("Test task", 0.7)
        self.assertIsInstance(result, str)
        self.assertIn("Test task", result)
        self.assertIn("0.7", result)
        self.assertIn("optimized memory enhancement strategy is:", result)

    def test_optimization_process(self):
        def mock_objective_function(params):
            return np.sum(params**2)  # Simple quadratic function for testing

        result = minimize(mock_objective_function, x0=[0.5, 0.5, 0.5, 0.5], method='COBYLA', options={'maxiter': 10})

        self.assertIsInstance(result.x, np.ndarray)  # Optimized parameters
        self.assertIsInstance(result.fun, float)  # Optimized value

    def test_convert_state_to_binary_integer(self):
        state = 7  # Binary: '111'
        expected = '111'
        result = self.optimizer.convert_state_to_binary(state)
        self.assertEqual(result, expected)

    def test_convert_state_to_binary_string(self):
        state = '101'
        expected = '101'
        result = self.optimizer.convert_state_to_binary(state)
        self.assertEqual(result, expected)

    def test_convert_state_to_binary_string_with_spaces(self):
        state = '1 0 1'
        expected = '101'
        result = self.optimizer.convert_state_to_binary(state)
        self.assertEqual(result, expected)

    def test_convert_state_to_binary_list(self):
        state = [1, 0, 1]
        expected = '101'
        result = self.optimizer.convert_state_to_binary(state)
        self.assertEqual(result, expected)

    def test_convert_state_to_binary_tuple(self):
        state = (1, 0, 1)
        expected = '101'
        result = self.optimizer.convert_state_to_binary(state)
        self.assertEqual(result, expected)

    def test_convert_state_to_binary_invalid_type(self):
        state = {'state': '101'}
        with self.assertRaises(ValueError):
            self.optimizer.convert_state_to_binary(state)

    def test_validate_binary_string_valid(self):
        binary_str = '101'
        result = self.optimizer.validate_binary_string(binary_str)
        self.assertEqual(result, binary_str)

    def test_validate_binary_string_invalid(self):
        binary_str = '102'
        with self.assertRaises(ValueError):
            self.optimizer.validate_binary_string(binary_str)

    @patch('src.enhancements.quantum_inspired_optimization.quantum_inspired_optimization.logging')
    def test_map_state_to_strategy_valid(self, mock_logging):
        state = '111'
        task_complexity = 0.5
        result = self.optimizer.map_state_to_strategy(state, task_complexity)
        self.assertIsInstance(result, dict)
        self.assertIn('state', result)
        self.assertIn('task_complexity', result)
        self.assertIn('selected_strategy', result)

    @patch('src.enhancements.quantum_inspired_optimization.quantum_inspired_optimization.logging')
    def test_map_state_to_strategy_invalid_state(self, mock_logging):
        state = {'invalid': 'state'}  # Invalid state type
        task_complexity = 0.5
        with self.assertRaises(ValueError):
            self.optimizer.map_state_to_strategy(state, task_complexity)

if __name__ == '__main__':
    unittest.main()
