
import string


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)
    count = len(h)

    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)

        heapq.heappush(h,(freq1 + freq2, count , Node(left,right)))

        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h

        root.walk(code, "")
    return code



def huffman_decoding(encoding_dict, encoded_str):
    decoded_str = ''
    encoding_dict = {value:key for key, value in encoding_dict.items()}
    sequence = ''

    for char in encoded_str:
        sequence += char
        if sequence in encoding_dict:
                decoded_str += encoding_dict[sequence]
                sequence = ''
    return decoded_str




k, length = (int(i) for i in input().split())

encoding_dict ={}

for _ in range(k):
    key,value = (i.strip() for i in input().split(":"))
    encoding_dict[key] = value

encoded_str = input()
print(huffman_decoding(encoding_dict,encoded_str))
