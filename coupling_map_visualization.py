# Alternative visualization methods for coupling maps when Graphviz is not available

def visualize_coupling_maps_without_graphviz(A, B, cmapA, cmapB):
    """
    Visualize coupling maps using text-based methods when Graphviz is not available
    """
    print("=" * 60)
    print("COUPLING MAP VISUALIZATION (Text-based)")
    print("=" * 60)
    
    # Coupling Map A
    print(f"\n📊 {A.name} Coupling Map:")
    print(f"   Number of qubits: {A.num_qubits}")
    print(f"   Number of connections: {len(list(cmapA.get_edges()))}")
    print(f"   Connections: {list(cmapA.get_edges())}")
    
    # Coupling Map B
    print(f"\n📊 {B.name} Coupling Map:")
    print(f"   Number of qubits: {B.num_qubits}")
    print(f"   Number of connections: {len(list(cmapB.get_edges()))}")
    print(f"   Connections: {list(cmapB.get_edges())}")
    
    # Comparison
    print(f"\n🔍 COMPARISON:")
    print(f"   {A.name}: {len(list(cmapA.get_edges()))} connections for {A.num_qubits} qubits")
    print(f"   {B.name}: {len(list(cmapB.get_edges()))} connections for {B.num_qubits} qubits")
    
    # Calculate connection density
    density_A = len(list(cmapA.get_edges())) / (A.num_qubits * (A.num_qubits - 1) / 2) if A.num_qubits > 1 else 0
    density_B = len(list(cmapB.get_edges())) / (B.num_qubits * (B.num_qubits - 1) / 2) if B.num_qubits > 1 else 0
    
    print(f"\n📈 Connection Density (higher = more connected):")
    print(f"   {A.name}: {density_A:.4f}")
    print(f"   {B.name}: {density_B:.4f}")
    
    # Simple ASCII visualization for small coupling maps
    if A.num_qubits <= 20:
        print(f"\n🎨 ASCII Visualization for {A.name}:")
        visualize_ascii_coupling_map(cmapA.get_edges(), A.num_qubits, A.name)
    
    if B.num_qubits <= 20:
        print(f"\n🎨 ASCII Visualization for {B.name}:")
        visualize_ascii_coupling_map(cmapB.get_edges(), B.num_qubits, B.name)

def visualize_ascii_coupling_map(edges, num_qubits, backend_name):
    """
    Create a simple ASCII visualization of the coupling map
    """
    if num_qubits > 20:
        print("   (ASCII visualization only for ≤20 qubits)")
        return
    
    print(f"   Qubit connections for {backend_name}:")
    
    # Create adjacency matrix
    matrix = [[0] * num_qubits for _ in range(num_qubits)]
    for edge in edges:
        i, j = edge
        matrix[i][j] = 1
        matrix[j][i] = 1  # Undirected graph
    
    # Print header
    header = "   " + "".join(f"{i:2}" for i in range(num_qubits))
    print(header)
    print("   " + "-" * (2 * num_qubits))
    
    # Print matrix
    for i in range(num_qubits):
        row = f"{i:2}|"
        for j in range(num_qubits):
            if i == j:
                row += " ·"  # Diagonal
            elif matrix[i][j]:
                row += " ●"  # Connection
            else:
                row += " ○"  # No connection
        print(row)

# Usage example (replace with your actual backend objects)
if __name__ == "__main__":
    print("This script provides alternative visualization methods for coupling maps.")
    print("Import and use the functions in your notebook when Graphviz is not available.")
    
    # Example usage:
    # visualize_coupling_maps_without_graphviz(A, B, cmapA, cmapB)


