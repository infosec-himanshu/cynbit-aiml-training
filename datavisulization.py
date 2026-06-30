import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

plt.figure(figsize=(6, 4))
plt.bar(df["Name"], df["Age"], color="skyblue")
plt.title("Student Ages")
plt.xlabel("Names")
plt.ylabel("Age")
plt.savefig("student_ages_bar.png")
plt.close()

city_counts = df["City"].value_counts()
plt.figure(figsize=(5, 5))
plt.pie(city_counts, labels=city_counts.index, autopct="%1.1f%%", startangle=140, colors=["gold", "lightgreen", "lightcoral", "lightskyblue"])
plt.title("Student City Distribution")
plt.savefig("student_city_pie.png")
plt.close()

print("Charts generated and saved successfully as images.")