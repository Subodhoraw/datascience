import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def feature_engineering(input_file="data/diabetes_clean.csv"):
    # Load cleaned dataset
    df = pd.read_csv(input_file)

    # Split features (X) and target (y)
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    # Train-test split (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Feature scaling (standardization)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Save processed data
    pd.DataFrame(X_train_scaled, columns=X.columns).to_csv("data/X_train_scaled.csv", index=False)
    pd.DataFrame(X_test_scaled, columns=X.columns).to_csv("data/X_test_scaled.csv", index=False)
    y_train.to_csv("data/y_train.csv", index=False)
    y_test.to_csv("data/y_test.csv", index=False)

    print("✅ Feature engineering done. Train/test datasets saved in 'data/'.")

if __name__ == "__main__":
    feature_engineering()
