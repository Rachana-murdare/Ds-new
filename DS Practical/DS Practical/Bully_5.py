class BullyAlgorithm:
    def __init__(self, nodes):
        self.nodes = nodes
        self.coordinator = max(nodes)  # Assume highest node is the leader initially

    def start_election(self, initiator):
        print(f"\nNode {initiator} starts an election...")
        higher_nodes = [node for node in self.nodes if node > initiator]

        if not higher_nodes:
            print(f"Node {initiator} becomes the new coordinator (No higher nodes).")
            self.coordinator = initiator
        else:
            for node in higher_nodes:
                print(f"Node {initiator} sends election message to Node {node}")
            self.coordinator = max(higher_nodes)
            print(f"Node {self.coordinator} becomes the new coordinator.")

    def get_coordinator(self):
        return self.coordinator


# Example Usage
nodes = [1, 2, 3, 4, 5]
bully = BullyAlgorithm(nodes)
print(f"Initial Coordinator: Node {bully.get_coordinator()}")
bully.start_election(3)  # Node 3 initiates election
print(f"New Coordinator: Node {bully.get_coordinator()}")
