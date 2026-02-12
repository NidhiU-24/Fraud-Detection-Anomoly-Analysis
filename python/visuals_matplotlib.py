import duckdb
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# Connect to MotherDuck
# ------------------------------
con = duckdb.connect("md:")

# Load final fraud risk table
df = con.execute("SELECT * FROM fraud_risk_final").fetch_df()

# ------------------------------
# Prepare data for plots
# ------------------------------
# Fraud counts
fraud_counts = df['Class'].value_counts()

# Fraud rate by total risk score
risk_summary = df.groupby('total_risk_score').agg(
    total=('Class', 'count'),
    fraud=('Class', 'sum')
).reset_index()
risk_summary['fraud_rate'] = 100 * risk_summary['fraud'] / risk_summary['total']

# Fraud rate by amount category
amount_summary = df.groupby('amount_category').agg(
    total=('Class', 'count'),
    fraud=('Class', 'sum')
).reset_index()
amount_summary['fraud_rate'] = 100 * amount_summary['fraud'] / amount_summary['total']

# Z-scores for anomaly detection
z_scores = (df['Amount'] - df['Amount'].mean()) / df['Amount'].std()

# ------------------------------
# Create figure 3x2
# ------------------------------
fig, axes = plt.subplots(3, 2, figsize=(18, 18), constrained_layout=True)
fig.suptitle("Fraud Detection & Anomaly Analysis", fontsize=22, weight='bold')

# ------------------------------
# 1️⃣ Fraud vs Non-Fraud Pie
# ------------------------------
axes[0, 0].pie(
    fraud_counts,
    labels=['Legit (0)', 'Fraud (1)'],
    autopct='%1.2f%%',
    startangle=90,
    colors=['#4CAF50', '#F44336']
)
axes[0, 0].set_title("Fraud vs Non-Fraud Distribution", fontsize=14)

# ------------------------------
# 2️⃣ Fraud Rate by Risk Score
# ------------------------------
axes[0, 1].bar(risk_summary['total_risk_score'], risk_summary['fraud_rate'], color='orange')
axes[0, 1].set_xlabel('Total Risk Score')
axes[0, 1].set_ylabel('Fraud Rate (%)')
axes[0, 1].set_title('Fraud Rate by Risk Score', fontsize=14)
for i, v in enumerate(risk_summary['fraud_rate']):
    axes[0, 1].text(risk_summary['total_risk_score'][i]-0.15, v+0.5, f"{v:.2f}%", fontsize=10)

# ------------------------------
# 3️⃣ Transaction Amount Distribution (Log Scale)
# ------------------------------
axes[1, 0].hist(df['Amount'], bins=50, color='skyblue', edgecolor='black')
axes[1, 0].set_xlabel('Transaction Amount')
axes[1, 0].set_ylabel('Number of Transactions')
axes[1, 0].set_yscale('log')
axes[1, 0].set_title('Transaction Amount Distribution (Log Scale)', fontsize=14)

# ------------------------------
# 4️⃣ Fraud Rate by Amount Category
# ------------------------------
axes[1, 1].bar(amount_summary['amount_category'], amount_summary['fraud_rate'], color=['green', 'yellow', 'red'])
axes[1, 1].set_xlabel('Amount Category')
axes[1, 1].set_ylabel('Fraud Rate (%)')
axes[1, 1].set_title('Fraud Rate by Amount Category', fontsize=14)
for i, v in enumerate(amount_summary['fraud_rate']):
    axes[1, 1].text(i-0.15, v+0.5, f"{v:.2f}%", fontsize=10)

# ------------------------------
# 5️⃣ Z-Score Distribution (Anomaly Detection)
# ------------------------------
axes[2, 0].hist(z_scores, bins=50, color='purple', edgecolor='black')
axes[2, 0].set_xlabel('Z-Score')
axes[2, 0].set_ylabel('Number of Transactions')
axes[2, 0].set_title('Z-Score Distribution (Anomaly Detection)', fontsize=14)
axes[2, 0].axvline(3, color='red', linestyle='--', label='Z=3 Threshold')
axes[2, 0].axvline(-3, color='red', linestyle='--')
axes[2, 0].legend()

# ------------------------------
# 6️⃣ Scatter Plot: Amount vs Total Risk Score (Fraud Highlighted)
# ------------------------------
colors = df['Class'].map({0: '#4CAF50', 1: '#F44336'})
axes[2, 1].scatter(df['total_risk_score'], df['Amount'], c=colors, alpha=0.6, edgecolor='k')
axes[2, 1].set_xlabel('Total Risk Score')
axes[2, 1].set_ylabel('Transaction Amount')
axes[2, 1].set_title('Transaction Amount vs Total Risk Score (Fraud Highlighted)', fontsize=14)
axes[2, 1].set_yscale('log')
axes[2, 1].legend(
    handles=[
        plt.Line2D([0], [0], marker='o', color='w', label='Legit', markerfacecolor='#4CAF50', markersize=10),
        plt.Line2D([0], [0], marker='o', color='w', label='Fraud', markerfacecolor='#F44336', markersize=10)
    ],
    loc='upper left'
)

# ------------------------------
# Save and show figure
# ------------------------------
plt.savefig("fraud_analysis_portfolio.png", dpi=300)
plt.show()
