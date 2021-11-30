# -*- coding: utf-8 -*-
"""ComputaçãoQuântica.ipynb """


!pip install qiskit

!pip install qiskit[visualization]

"""# Simulação dos estados quânticos de Hilbert"""

from qiskit import *
from qiskit.visualization import plot_histogram

#num_qubits=3
#num_bits=3
#qc=QuantumCircuit(num_qubits,num_bits) # sintaxe

# Cria um circuito  com 3 qubits e 3 bits clássico 
qc = QuantumCircuit(3,3)
# qc.x([0,2])  # Faz porta X sobre os qubits 0,2
# Faz porta H sobre os qubits 0,1 e 2
qc.h(1)
qc.h(2)
qc.h(0)
qc.measure([0,1,2], [0,1,2])
qc.measure([1], [1])

display(qc.draw())   # Mostra o circuito quântico

backend = Aer.get_backend('qasm_simulator')

prob = execute(qc,backend,shots=1000).result().get_counts()

plot_histogram(prob)
