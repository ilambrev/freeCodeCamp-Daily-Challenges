def decode_qr(qr_code):

    def rotate_code(code):
        rotated_code = []

        for i in range(len(code) - 1, -1, -1):
            row = []
            for j in range(len(code)):
                row.append(code[j][i])

            rotated_code.append("".join(row))

        return rotated_code

    def isOrientationRight(code):
        return (code[0][:2] == "11" and code[0][4:] == "11"
                and code[1][:2] == "11" and code[1][4:] == "11"
                and code[4][:2] == "11" and code[5][:2] == "11")

    while not isOrientationRight(qr_code):
        qr_code = rotate_code(qr_code)

    binary_data = ""

    for i in range(len(qr_code)):
        if i == 0 or i == 1:
            binary_data += qr_code[i][2:4]
        elif i == 4 or i == 5:
            binary_data += qr_code[i][2:]
        else:
            binary_data += qr_code[i]

    return binary_data

# print(decode_qr(["110011", "110011", "000000", "000000", "110000", "110001"]))  # should return "000000000000000000000001"
# print(decode_qr(["100011", "000011", "000000", "000000", "110011", "110011"]))  # should return "000000000000000000000001"
# print(decode_qr(["110011", "111111", "010000", "110000", "110011", "110100"]))  # should return "001101000011000000110100"
# print(decode_qr(["011011", "101011", "101000", "100010", "110011", "111011"]))  # should return "010001000100010101010110"
# print(decode_qr(["111100", "110001", "100011", "001101", "110011", "110011"]))  # should return "010000100100100101001110"