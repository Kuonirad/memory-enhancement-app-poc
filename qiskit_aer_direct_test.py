import qiskit_aer
from qiskit import QuantumCircuit

def main():
    print(f"Qiskit-Aer version: {qiskit_aer.__version__}")

    # Create a simple quantum circuit
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()

    # Use AerSimulator directly from qiskit_aer
    simulator = qiskit_aer.AerSimulator()
    print(f"Created AerSimulator: {simulator}")

    # Run the circuit
    job = simulator.run(qc, shots=1000)
    result = job.result()
    counts = result.get_counts(qc)
    print(f"Simulation results: {counts}")

if __name__ == "__main__":
    main()
