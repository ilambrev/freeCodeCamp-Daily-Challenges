def generate_snowflake(crystals):

    return "\n".join([line + line[::-1] for line in crystals.split("\n")])

# print(generate_snowflake("* \n *\n* "))
# print(generate_snowflake("X=~"))
# print(generate_snowflake(" X  \n  v \nX--=\n  ^ \n X  "))
# print(generate_snowflake("*   *\n * * \n* * *\n * * \n*   *"))
# print(generate_snowflake("*  -\n * -\n*  -"))