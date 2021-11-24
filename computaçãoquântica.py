# -*- coding: utf-8 -*-
"""ComputaçãoQuântica.ipynb"""


!pip install qiskit

pip install qiskit[visualization]



!pip install pylatexenc

!pip install qiskit --upgrade



from qiskit import *
from qiskit.visualization import plot_histogram

num_qubits=2
num_bits=2
qc=QuantumCircuit(num_qubits,num_bits)

qc

qc.x(0)
qc.h(1)
qc.measure(0,0)
qc.measure(1,1)



qc.draw(output='text')

backend = Aer.get_backend('qasm_simulator')

execute(qc,backend,shots=1000).result().get_counts()

