class RegisterAllocator:
    """
    Chaitin-Briggs Graph Coloring Register Allocator.
    Assigns physical registers to virtual variables using K-coloring heuristics.
    """
    def __init__(self, k_registers=3):
        self.k = k_registers

    def allocate(self, nodes, edges):
        adj = {n: set() for n in nodes}
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        stack = []
        remaining = set(nodes)
        while remaining:
            found = False
            for n in list(remaining):
                deg = len(adj[n] & remaining)
                if deg < self.k:
                    stack.append(n)
                    remaining.remove(n)
                    found = True
                    break
            if not found:
                victim = remaining.pop()
                stack.append(victim)

        colors = {}
        while stack:
            n = stack.pop()
            neighbor_colors = {colors[nb] for nb in adj[n] if nb in colors}
            assigned = None
            for reg in range(self.k):
                if reg not in neighbor_colors:
                    assigned = reg
                    break
            colors[n] = assigned

        return colors
