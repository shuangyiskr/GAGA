from queue import PriorityQueue


class HuffmanNode:
    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(freq_dict):
    pq = PriorityQueue()
    for char, freq in freq_dict.items():
        pq.put(HuffmanNode(freq, char))

    while pq.qsize() > 1:
        node1 = pq.get()
        node2 = pq.get()
        parent = HuffmanNode(node1.freq + node2.freq)
        parent.left = node1
        parent.right = node2
        pq.put(parent)

    return pq.get()


def encode_string(root, string):
    huffman_code = {}
    build_huffman_code(huffman_code, "", root)
    encoded_string = ""
    for char in string:
        encoded_string += huffman_code[char]
    return encoded_string


def build_huffman_code(huffman_code, current_code, node):
    if node is None:
        return
    if node.char is not None:
        huffman_code[node.char] = current_code
    build_huffman_code(huffman_code, current_code + "0", node.left)
    build_huffman_code(huffman_code, current_code + "1", node.right)


# 测试代码
if __name__ == "__main__":
    freq_dict = {'a': 45, 'b': 13, 'c': 12, 'd': 16, 'e': 9, 'f': 5}
    root = build_huffman_tree(freq_dict)
    huffman_code = {}
    build_huffman_code(huffman_code, "", root)
    print(huffman_code)
    encoded_string = encode_string(root, "abcda")
    print(encoded_string)
