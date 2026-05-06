class RingAlgorithm:
    def __init__(self, processes):
        self.processes = sorted(processes)
        self.ring = self.processes[:]   # copy of processes
        self.coordinator = None

    def is_alive(self, process_id):
        return process_id in self.ring

    def hold_election(self, initiator):
        print(f"Process {initiator} starts election.")

        election_list = [initiator]
        current_index = self.ring.index(initiator)

        while True:
            current_index = (current_index + 1) % len(self.ring)
            next_process = self.ring[current_index]

            if next_process == initiator:
                break

            print(f"Election message from {election_list[-1]} to {next_process}")
            election_list.append(next_process)

        # Select highest ID as coordinator
        winner = max(election_list)
        self.coordinator = winner

        print(f"Process {winner} is elected as the new coordinator.")


# Example usage
if __name__ == "__main__":
    processes = [1, 2, 4, 6]
    ring = RingAlgorithm(processes)
    ring.hold_election(initiator=2)