def get_streaming_bill(cart, subscription):
    formats = { 	
        "HD": {"rent": 3.99, "buy": 12.99},
        "4K": {"rent": 5.99, "buy": 19.99}
    }

    discounts = {
        "none": 0,
        "basic": 0.10,
        "premium": 0.25
    }

    total_price = 0

    for movie in cart:
        discount = discounts[subscription]
        format = movie["format"]
        type = movie["type"]

        total_price += formats[format][type] * (1 - discount) 

    return f"${total_price:.2f}"

# print(get_streaming_bill([{ "format": "HD", "type": "rent" }], "none"))
# print(get_streaming_bill([{ "format": "HD", "type": "rent" }, { "format": "HD", "type": "buy" }], "premium"))
# print(get_streaming_bill([{ "format": "HD", "type": "rent" }, { "format": "HD", "type": "rent" }, { "format": "HD", "type": "buy" }], "basic"))
# print(get_streaming_bill([{ "format": "4K", "type": "buy" }, { "format": "4K", "type": "buy" }], "premium"))
# print(get_streaming_bill([{ "format": "HD", "type": "rent" }, { "format": "4K", "type": "rent" }, { "format": "HD", "type": "buy" }, { "format": "4K", "type": "buy" }], "none"))
# print(get_streaming_bill([{ "format": "HD", "type": "rent" }, { "format": "4K", "type": "rent" }, { "format": "HD", "type": "buy" }, { "format": "4K", "type": "buy" }, { "format": "HD", "type": "buy" }], "basic"))