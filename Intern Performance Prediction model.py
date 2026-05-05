import pandas as pd
data=pd.read_csv("data.csv")
print(data.head())
x=data[['time','feedback','attendance']]
y=data["performance"]
from sklearn.model_selection import train_test_split
x_train,x_test, y_train, y_test =train_test_split(x,y,test_size=0.2,random_state=42)
from sklearn.ensemble import  RandomForestRegressor
model=RandomForestRegressor()
model.fit(x_train,y_train)
predictions=model.predict(x_test)
print("Predictions:", predictions)
for p in predictions:
    if p >= 0.7:
        print(f"{p:.2f} → EXCEL ⭐")
    elif p >= 0.4:
        print(f"{p:.2f} → AVERAGE ⚠️")
    else:
        print(f"{p:.2f} → STRUGGLING ❌")odel.pkl","wb"))