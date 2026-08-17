import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Marksheet = {
    'Name': ["Roshan", "Sohail", "Sameer", "Kiran", "Anita", "Madhu"],
    'Attendance': [90, 80, 70, 60, 75, 50],
    'English': [77, 85, 91, 54, 70, 66],
    'Hindi': [76, 84, 90, 44, 70, 56],
    'Maths': [79, 89, 69, 59, 80, 50],
    'Science': [81, 73, 78, 63, 85, 50]
}

df = pd.DataFrame(Marksheet)
#print(df)

Avg_attendance = [(df["Attendance"].sum())/len(df["Name"])]
Avg_att =np.float64(Avg_attendance)
#print(Avg_att)

Avg_Science = [(df["Science"].sum())/len(df["Name"])]
Avg_SCI =np.float64(Avg_Science)
#print(Avg_SCI)

subjects = ["English", "Hindi", "Maths", "Science"]

df["Total_Marks"]= df[subjects].sum(axis=1)
df["Avg_Score"] = (df["Total_Marks"]/len(subjects))
#print(df)

#print(df.loc[df["Name"]=="Madhu", ("Name", "Attendance", "Total_Marks", "Avg_Score")])

df.loc[df["Name"]=="Sameer", "Attendance"]=78

#print(df.loc[(df["Avg_Score"]>80) & (df["Attendance"]>75) ,("Name", "Attendance", "Total_Marks", "Avg_Score")])
print(df)
y_axis = df["Total_Marks"].to_numpy()
x_axis = df["Name"].to_numpy()

plt.plot(x_axis, y_axis)
plt.show()
