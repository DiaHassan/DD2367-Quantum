# Fix for Graphviz MissingOptionalLibraryError in Qiskit
# Replace your Cell 4 with this code:

# Option 1: Try to fix Graphviz PATH issue
import os
import sys

# Common Graphviz installation paths on Windows
graphviz_paths = [
    r"C:\Program Files\Graphviz\bin",
    r"C:\Program Files (x86)\Graphviz\bin",
    r"C:\Users\{}\AppData\Local\Programs\Graphviz\bin".format(os.getenv('USERNAME')),
]

# Add Graphviz to PATH if found
for path in graphviz_paths:
    if os.path.exists(path) and path not in os.environ['PATH']:
        os.environ['PATH'] = path + os.pathsep + os.environ['PATH']
        print(f"Added Graphviz to PATH: {path}")
        break

# Option 2: Try the original visualization
try:
    from qiskit.visualization import plot_coupling_map
    print("Graphviz found! Using original visualization...")
    plot_coupling_map(A.num_qubits, None, cmapA.get_edges())
    plot_coupling_map(B.num_qubits, None, cmapB.get_edges())
    
except Exception as e:
    print(f"Graphviz visualization failed: {e}")
    print("\n" + "="*60)
    print("USING ALTERNATIVE VISUALIZATION METHODS")
    print("="*60)
    
    # Alternative visualization
    print(f"\n📊 {A.name} Coupling Map:")
    print(f"   Qubits: {A.num_qubits}")
    print(f"   Connections: {len(list(cmapA.get_edges()))}")
    print(f"   Edges: {list(cmapA.get_edges())}")
    
    print(f"\n📊 {B.name} Coupling Map:")
    print(f"   Qubits: {B.num_qubits}")
    print(f"   Connections: {len(list(cmapB.get_edges()))}")
    print(f"   Edges: {list(cmapB.get_edges())}")
    
    # Simple matrix visualization for small coupling maps
    if A.num_qubits <= 20:
        print(f"\n🎨 {A.name} Connection Matrix:")
        edges_A = set(cmapA.get_edges())
        for i in range(min(10, A.num_qubits)):  # Show first 10 qubits
            row = f"Q{i:2}: "
            for j in range(min(10, A.num_qubits)):
                if i == j:
                    row += "· "
                elif (i, j) in edges_A or (j, i) in edges_A:
                    row += "● "
                else:
                    row += "○ "
            print(row)
        if A.num_qubits > 10:
            print(f"   ... (showing first 10 of {A.num_qubits} qubits)")

print("\n✅ Visualization complete!")
