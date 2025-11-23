# QUANTUM STATE VISUALIZATION ALGORITHM
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_vector

def quantum_state_modeler(qubits=1, gates=['h']):
    """
    Modélise l'évolution d'un état quantique through les portes logiques
    Visualise sur la sphère de Bloch - parfaite pour ton dépôt
    """
    qc = QuantumCircuit(qubits)
    
    # Application des portes quantiques
    for gate in gates:
        if gate == 'h':
            qc.h(0)  # Superposition
        elif gate == 'x':
            qc.x(0)  # Porte X (NOT quantique)
        elif gate == 'y':
            qc.y(0)  # Porte Y
        elif gate == 'z':
            qc.z(0)  # Porte Z
    
    # Simulation
    backend = Aer.get_backend('statevector_simulator')
    result = execute(qc, backend).result()
    statevector = result.get_statevector()
    
    # Conversion pour visualisation Bloch
    bloch_vector = [
        2 * statevector[0].real * statevector[1].real,
        2 * statevector[0].imag * statevector[1].imag,
        abs(statevector[0])*2 - abs(statevector[1])*2
    ]
    
    return bloch_vector, qc

# Exemple d'utilisation
bloch_vec, circuit = quantum_state_modeler(gates=['h', 'x'])
plot_bloch_vector(bloch_vec)  # Visualisation élégante