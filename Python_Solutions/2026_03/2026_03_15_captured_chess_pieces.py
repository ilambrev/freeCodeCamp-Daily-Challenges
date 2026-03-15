def get_captured_value(pieces):
    initial_pieces = {
        "P": {"quantity": 8, "value": 1}, 	 	
        "R": {"quantity": 2, "value": 5}, 	
        "N": {"quantity": 2, "value": 3}, 	
        "B": {"quantity": 2, "value": 3}, 	
        "Q": {"quantity": 1, "value": 9}, 	
        "K": {"quantity": 1, "value": 0} 	
    }

    if "K" not in pieces:
        return "Checkmate"
    
    for piece in pieces:
        initial_pieces[piece]["quantity"] -= 1

    return sum(v["quantity"] * v["value"] for v in initial_pieces.values())

# print(get_captured_value(["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"]))
# print(get_captured_value(["P", "P", "P", "P", "P", "R", "B", "K"]))
# print(get_captured_value(["K", "P", "P", "N", "P", "P", "R", "P", "B", "P", "N", "B"]))
# print(get_captured_value(["P", "Q", "N", "P", "P", "B", "K", "P", "R", "R", "P", "P", "B", "P"]))
# print(get_captured_value(["P", "K"]))
# print(get_captured_value(["N", "P", "P", "B", "K", "P", "Q", "N", "P", "P", "R", "R", "P", "P", "P", "B"]))
# print(get_captured_value(["N", "P", "P", "B", "P", "R", "Q", "P", "P", "P", "B"]))