import sys
import importlib
import os

def test_import(module_name):
    try:
        module = importlib.import_module(module_name)
        print(f"Successfully imported {module_name}")
        if hasattr(module, '__file__'):
            print(f"Module location: {module.__file__}")
        if hasattr(module, '__version__'):
            print(f"Module version: {module.__version__}")
        return module
    except ImportError as e:
        print(f"Failed to import {module_name}: {str(e)}")
        return None

def main():
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print("Python path:")
    for path in sys.path:
        print(f"  {path}")

    modules_to_test = [
        'qiskit',
        'qiskit_aer',
        'numpy',
        'scipy',
        'matplotlib',
        'pandas',
        'sympy',
        'enhancements.quantum_inspired_optimization.quantum_inspired_optimization'
    ]

    for module_name in modules_to_test:
        print(f"\nTesting import of {module_name}")
        module = test_import(module_name)

    # Test basic Qiskit functionality
    qiskit = test_import('qiskit')
    if qiskit:
        try:
            qc = qiskit.QuantumCircuit(2)
            qc.h(0)
            qc.cx(0, 1)
            qc.measure_all()
            print("Quantum circuit created successfully.")
        except Exception as e:
            print(f"Error creating quantum circuit: {str(e)}")

if __name__ == "__main__":
    main()
