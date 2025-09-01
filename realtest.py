# --- Imports ---
from qiskit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

# --- Connect (assumes Step 5 is done) ---
service = QiskitRuntimeService()

# Pick an available real backend (not a simulator)
backend = service.least_busy(operational=True, simulator=False)
print("Using backend:", backend.name)

# --- Build Bell circuit ---
bell = QuantumCircuit(2)
bell.h(0)
bell.cx(0, 1)
bell.measure_all()

# --- Transpile to the device's ISA ---
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_bell = pm.run(bell)

# --- Run with the Sampler V2 primitive ---
sampler = Sampler(mode=backend)
sampler.options.default_shots = 1024
job = sampler.run([isa_bell])
print("Job ID:", job.job_id())

# --- Get results ---
result = job.result()
pub_result = result[0]
print("Counts (meas register):", pub_result.data.meas.get_counts())
