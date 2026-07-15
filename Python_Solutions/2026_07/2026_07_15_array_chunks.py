def chunk_array(arr, size):
    array_chunks = []
    chunks = int(len(arr) / size) if len(arr) % size == 0 else int(len(arr) / size) + 1

    for i in range(chunks):
        begin = i * size
        end = (i + 1) * size if (len(arr) - begin) >= size else len(arr)
        array_chunks.append(arr[begin:end])

    return array_chunks

# print(chunk_array([1, 2, 3, 4, 5, 6], 3))
# print(chunk_array([1, "two", 3, "four", 5, "six", 7, "eight"], 2))
# print(chunk_array([1, 2, 3, 4, 5], 3))
# print(chunk_array(["a", "b", "c", "d", "e"], 1))
# print(chunk_array([1, 2, 3], 5))