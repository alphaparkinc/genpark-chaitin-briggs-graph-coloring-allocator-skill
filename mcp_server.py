import sys
import json
from client import RegisterAllocator

def main():
    alloc = RegisterAllocator()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "allocate":
            colors = alloc.allocate(params.get("nodes", []), params.get("edges", []))
            res = {"colors": colors}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
