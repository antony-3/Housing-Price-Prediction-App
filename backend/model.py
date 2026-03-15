# importing the required libraries
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Loading the data
df = pd.read_csv("/Users/user/Documents/housing_project/dataset/housing.csv")

# Removing ocean proximity feature
df.drop(columns=["ocean_proximity"], inplace=True)

# Removing rows with Nan
df.dropna(inplace=True)

# Separating features from the target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Instantiating scaling modules
scaler_X = StandardScaler()
scaler_y = StandardScaler()

# Splitting data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling both the features and targets
X_train_scaled = scaler_X.fit_transform(X_train)
X_test_scaled = scaler_X.transform(X_test)
y_train_scaled = scaler_y.fit_transform(y_train.values.reshape(-1, 1))
y_test_scaled = scaler_y.transform(y_test.values.reshape(-1, 1))

# Instantiating linear regression module
model = LinearRegression()

#Training the model
model.fit(X_train_scaled, y_train_scaled)

# Saving the model
joblib.dump(model, "model.pkl")
joblib.dump(scaler_X, "scaler_X.pkl")
joblib.dump(scaler_y, "scaler_y.pkl")

