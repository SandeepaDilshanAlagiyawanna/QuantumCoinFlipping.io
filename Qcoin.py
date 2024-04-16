from flask import Flask, jsonify
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

app = Flask(__name__)

@app.route('/api/coin-flip', methods=['GET'])
def coin_flip():
    try:
        # Create a quantum circuit with one qubit
        qc = QuantumCircuit(1)

        # Apply a Hadamard gate to put the qubit into a superposition
        qc.h(0)

        # Measure the qubit to get the result
        qc.measure_all()

        # Simulate the circuit
        simulator = AerSimulator()
        circ = transpile(qc, simulator)
        result = simulator.run(circ).result()
        counts = result.get_counts(qc)

        # Extract the result
        if '0' in counts:
            result_str = "Heads"
        else:
            result_str = "Tails"

        # Return JSON response
        return jsonify({"result": result_str})

    except Exception as e:
        # Handle any exceptions and return an error response
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)

@app.route('/api/coin-flip', methods=['GET'])
def coin_flip():
    # Create a quantum circuit with one qubit
    qc = QuantumCircuit(1)

    # Apply a Hadamard gate to put the qubit into a superposition
    qc.h(0)

    # Measure the qubit to get the result
    qc.measure_all()

    # Simulate the circuit
    simulator = AerSimulator()
    circ = transpile(qc, simulator)
    result = simulator.run(circ).result()
    counts = result.get_counts(qc)

    # Extract the result
    if '0' in counts:
        result_str = "Heads"
    else:
        result_str = "Tails"

    return jsonify({"result": result_str})

if __name__ == '__main__':
    app.run(debug=True)
