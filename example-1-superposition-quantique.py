# EXAMPLE 1: SUPERPOSITION QUANTIQUE
def superposition_demo():
    """Démontre le principe de superposition avec la porte Hadamard"""
    qc = QuantumCircuit(1)
    qc.h(0)  # Met le qubit en superposition |0> + |1>
    
    backend = Aer.get_backend('statevector_simulator')
    result = execute(qc, backend).result()
    state = result.get_statevector()
    
    print(f"État quantique: {state}")
    print("Le qubit est simultanément dans les états |0> ET |1> !")

# EXAMPLE 2: INTRICATION QUANTIQUE
def entanglement_demo():
    """Crée deux qubits intriqués (phénomène EPR)"""
    qc = QuantumCircuit(2)
    qc.h(0)  # Superposition du premier qubit
    qc.cx(0, 1)  # Porte CNOT crée l'intrication
    
    print("Qubits intriqués: si l'un mesure |0>, l'autre mesure |0> instantanément!")
    return qc

# EXAMPLE 3: ALGORITHME DE GROVER (RECHERCHE)
def grover_search_demo():
    """Implémentation simplifiée de l'algorithme de recherche quantique"""
    qc = QuantumCircuit(2)
    # Étape 1: Superposition initiale
    qc.h([0, 1])
    # Étape 2: Oracle de marquage (simplifié)
    qc.z(0)  # Marque la solution |11>
    # Étape 3: Amplification d'amplitude
    qc.h([0, 1])
    qc.z([0, 1])
    qc.h([0, 1])
    
    print("Recherche quantique: trouve une solution en √N étapes au lieu de N!")
    return qc