import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(data):
    # Count frequencies
    freq = {}
    for char in data:
        freq[char] = freq.get(char, 0) + 1

    # Build the priority queue
    heap = [HuffmanNode(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    # Build the Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    # Generate codes
    root = heap[0]
    codes = {}

    def generate_codes(node, current_code):
        if not node:
            return
        if node.char is not None:
            codes[node.char] = current_code
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root, "")
    return codes

# Example
data = "huffmanencoding"
codes = huffman_encoding(data)
print("Huffman Codes:", codes)
