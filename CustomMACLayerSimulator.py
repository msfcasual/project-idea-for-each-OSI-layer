import random
import time

class Channel:
    def __init__(self):
        self.busy = False

    def sense(self):
        return self.busy

    def occupy(self):
        self.busy = True

    def release(self):
        self.busy = False

class Node:
    def __init__(self, node_id, channel):
        self.node_id = node_id
        self.channel = channel

    def send(self, data):
        if not self.channel.sense():
            print(f"Node {self.node_id}: Channel is free. Sending data: {data}")
            self.channel.occupy()
            time.sleep(0.1)  # Simulate transmission time
            self.channel.release()
            print(f"Node {self.node_id}: Transmission complete.")
        else:
            print(f"Node {self.node_id}: Channel busy. Collision detected!")

def simulate_mac(nodes, rounds=5):
    for i in range(rounds):
        print(f"\n--- Round {i+1} ---")
        sender = random.choice(nodes)
        data = f"Message {i+1} from Node {sender.node_id}"
        sender.send(data)
        time.sleep(0.05)

if __name__ == "__main__":
    channel = Channel()
    nodes = [Node(i, channel) for i in range(3)]
    simulate_mac(nodes)