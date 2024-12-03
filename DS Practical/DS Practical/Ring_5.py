class RingAlgorithm:
    def __init__(self, nodes):
        self.nodes = sorted(nodes)
        self.coordinator = max(nodes)

    def start_election(self, initiator):
        print(f"\nNode {initiator} starts an election...")
        ring = self.nodes[self.nodes.index(initiator):] + self.nodes[:self.nodes.index(initiator)]
        print("Election message is sent around the ring:", ring)

        new_coordinator = max(ring)
        self.coordinator = new_coordinator
        print(f"Node {self.coordinator} becomes the new coordinator.")

    def get_coordinator(self):
        return self.coordinator


# Example Usage
nodes = [1, 2, 3, 4, 5]
ring = RingAlgorithm(nodes)
print(f"Initial Coordinator: Node {ring.get_coordinator()}")
ring.start_election(2)  # Node 2 initiates election
print(f"New Coordinator: Node {ring.get_coordinator()}")
