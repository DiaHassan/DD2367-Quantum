from qiskit_aer.primitives import SamplerV2 as AerSampler
from qiskit import QuantumCircuit

bell = QuantumCircuit(2)
bell.h(0)
bell.cx(0, 1)
bell.measure_all()

sampler = AerSampler()
job = sampler.run([bell])
print(job.result()[0].data.meas.get_counts())