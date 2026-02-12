import duckdb

# Connect to MotherDuck
con = duckdb.connect("md:")

# Print your token
token = con.execute("PRAGMA PRINT_MD_TOKEN;").fetchall()[0][0]
print("Your MotherDuck token is:\n", token)
