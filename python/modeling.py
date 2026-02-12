import duckdb
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Connect to MotherDuck cloud
con = duckdb.connect("md:")

# Load feature-engineered data
df = con.execute("SELECT * FROM model_features").fetch_df()

# Prepare features and target
X = df.drop(columns=["Class", "amount_category"])
y = df["Class"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions and evaluation
preds = model.predict(X_test)
print(classification_report(y_test, preds))
