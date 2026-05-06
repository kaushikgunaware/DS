class BullyAlgorithm:
    def __init__(self, processes, coordinator=None):
        self.processes = processes  # list of process IDs
        self.coordinator = coordinator or max(processes)

    def is_alive(self, process_id):
        # Simulate which processes are alive
        return process_id in self.processes

    def hold_election(self, initiator):
        print(f"Process {initiator} starts election.")

        higher_processes = [p for p in self.processes if p > initiator]

        if not higher_processes:
            self.coordinator = initiator
            print(f"Process {initiator} becomes the new coordinator.")
        else:
            for p in higher_processes:
                print(f"Process {initiator} sends election message to {p}.")

            responses = [p for p in higher_processes if self.is_alive(p)]

            if responses:
                print(f"Process {initiator} gets responses from: {responses}")

                # Highest alive process takes over
                highest = max(responses)
                self.hold_election(highest)
            else:
                self.coordinator = initiator
                print(f"No higher processes responded. {initiator} becomes coordinator.")


# Example usage
if __name__ == "__main__":
    processes = [1, 2, 3, 5, 6]
    bully = BullyAlgorithm(processes)
    bully.hold_election(initiator=3)