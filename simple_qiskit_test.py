import qiskit_aer
from qiskit import QuantumCircuit

def main():
    print("Running simple Qiskit test...")

    # Create a Quantum Circuit
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    print("Quantum circuit created.")

    # Use AerSimulator directly from qiskit_aer
    simulator = qiskit_aer.AerSimulator()
    print("AerSimulator instantiated.")

    # Execute the circuit on the simulator
    job = simulator.run(qc, shots=1000)
    result = job.result()
    counts = result.get_counts(qc)
    print(f"Execution results: {counts}")

if __name__ == "__main__":
    main()
