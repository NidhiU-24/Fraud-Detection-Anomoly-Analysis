import duckdb
import sys

if len(sys.argv) < 2:
    print("Usage: python run_sql.py <sql_file>")
    sys.exit(1)

sql_file = sys.argv[1]

with open(sql_file, "r", encoding="utf-8") as f:
    sql = f.read()

con = duckdb.connect("md:")

# Split SQL statements safely
statements = [s.strip() for s in sql.split(";") if s.strip()]

for i, statement in enumerate(statements, start=1):
    print(f"\n--- Running Query {i} ---")
    
    try:
        result = con.execute(statement)
        
        # Check if query returned columns (means it was SELECT)
        if result.description is not None:
            df = result.fetch_df()
            print(df)
        else:
            print("Query executed successfully.")

    except Exception as e:
        print(f"Error in Query {i}: {e}")

print(f"\nFinished executing {sql_file}")
