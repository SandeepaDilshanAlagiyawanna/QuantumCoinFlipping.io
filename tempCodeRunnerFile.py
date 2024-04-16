import qiskit
from qiskit import QuantumCircuit, execute
from qiskit_aer import AerSimulator

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1)

# Apply a Hadamard gate to put the qubit into a superposition
qc.h(0)

# Measure the qubit to get the result
qc.measure_all()

# Simulate the circuit
simulator = AerSimulator()
job = execute(qc, simulator, shots=1)
result = job.result()
counts = result.get_counts(qc)

# Extract the result
if '0' in counts:
    print("Heads")
else:
    print("Tails")
