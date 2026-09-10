from client import RegisterAllocator

def main():
    print("=== Testing Chaitin-Briggs Graph Coloring Register Allocator ===")
    alloc = RegisterAllocator(k_registers=2)
    nodes = ["v0", "v1", "v2"]
    edges = [("v0", "v1")]
    colors = alloc.allocate(nodes, edges)
    print("Register assignment:", colors)

    assert colors["v0"] != colors["v1"]
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
