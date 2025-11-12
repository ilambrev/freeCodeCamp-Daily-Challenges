def generate_signature(name, title, company):
    first_prefix_range = "ABCDEFGHI"
    second_prefix_range = "JKLMNOPQR"
    third_prefix_range = "STUVWXYZ"
    signature = ""

    if name[0].upper() in first_prefix_range:
        signature += ">>"
    elif name[0].upper() in second_prefix_range:
        signature += "--"
    elif name[0].upper() in third_prefix_range:
        signature += "::"
    
    signature += name + ", " + title + " at " + company

    return signature

# print(generate_signature("Quinn Waverly", "Founder and CEO", "TechCo"))
# print(generate_signature("Alice Reed", "Engineer", "TechCo"))
# print(generate_signature("Tina Vaughn", "Developer", "example.com"))
# print(generate_signature("B. B.", "Product Tester", "AcmeCorp"))
# print(generate_signature("windstorm", "Cloud Architect", "Atmospheronics"))