from qiskit_ibm_runtime import QiskitRuntimeService

# >>> Edit these two lines:
TOKEN = "aGegbVMfJFB9qNARDnC_W8W825UrINsanjfnIKrelefn"   # REQUIRED
INSTANCE = None  # OPTIONAL: e.g., "crn:v1:bluemix:public:quantum-computing:us-east:...:..."

# Safety check to avoid empty tokens
# if not TOKEN or TOKEN.strip() in {"", "aGegbVMfJFB9qNARDnC_W8W825UrINsanjfnIKrelefn"}:
#     raise ValueError("Please paste your IBM Quantum API key into TOKEN (between quotes) and run again.")

# Create the service directly (no saved account needed)
service = QiskitRuntimeService(
    channel="ibm_quantum_platform",
    token=TOKEN.strip(),
    instance=(INSTANCE.strip() if isinstance(INSTANCE, str) and INSTANCE.strip() else None),
)

# Quick sanity check
backends = service.backends(operational=True, simulator=False)
print("OK. Found", len(backends), "real backends. Example:", [b.name for b in backends[:3]])

QiskitRuntimeService.save_account(
    channel="ibm_quantum_platform",
    token=TOKEN.strip(),
    instance=(INSTANCE.strip() if isinstance(INSTANCE, str) and INSTANCE.strip() else None),
    set_as_default=True,
    overwrite=True,
)
print("Saved default account for this runtime.")
