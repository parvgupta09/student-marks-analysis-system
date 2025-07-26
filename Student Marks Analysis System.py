# Student Marks Analysis System

import numpy as np
import pandas as pd
import contextlib



np.random.seed(42)



def grade(marks):
    if marks >= 90:
        return "AA"
    elif marks >= 80:
        return "AB"
    elif marks >= 70:
        return "BB"
    elif marks >= 60:
        return "BC"
    elif marks >= 50:
        return "CC"
    elif marks >= 40:
        return "CD"
    else:
        return "FF"



def plots():
    import matplotlib.pyplot as plt
    import pandas as pd

    # Read data
    df = pd.read_csv('Marks of Students_Cleaned.csv')
    df.columns = df.columns.str.strip()
    
    english = df['English']
    maths = df['Maths']
    science = df['Science']

    # 🔹 Histogram for each subject
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.hist(english, bins=10, color='red', edgecolor='black', label='Marks in English')
    plt.xlabel('Marks in English')
    plt.ylabel('No. of Students')
    plt.yticks(range(0, 18, 2))
    plt.title('Distribution of Marks in English')
    plt.legend(fontsize=6)

    plt.subplot(2, 2, 2)
    plt.hist(maths, bins=10, color='purple', edgecolor='black', label='Marks in Maths')
    plt.xlabel('Marks in Maths')
    plt.ylabel('No. of Students')
    plt.yticks(range(0, 18, 2))
    plt.title('Distribution of Marks in Maths')
    plt.legend(fontsize=6)

    plt.subplot(2, 2, 3)
    plt.hist(science, bins=10, color='lightgreen', edgecolor='black', label='Marks in Science')
    plt.xlabel('Marks in Science')
    plt.ylabel('No. of Students')
    plt.yticks(range(0, 18, 2))
    plt.title('Distribution of Marks in Science')
    plt.legend(fontsize=6)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.suptitle('Distribution of Marks in Each Subject')
    plt.savefig('Distribution of Marks in Each Subject.pdf', dpi=600, bbox_inches='tight')
    plt.show()
    plt.close()

    # 🔹 Pie chart for one student
    roll = int(input('Enter the roll no. of the student for pie chart: '))
    marks = [english[roll - 1], maths[roll - 1], science[roll - 1]]
    plt.pie(marks, labels=['English', 'Maths', 'Science'],
            colors=['lightgreen', 'blue', 'coral'], autopct='%1.2f%%')
    plt.title(f'Subject-wise Contribution for Roll No. {roll}')
    plt.show()
    plt.close()

    # 🔹 Bar chart for top 10 students
    top10 = df.sort_values(by='Total', ascending=False).head(10)
    marks = top10['Total']
    roll = top10['Roll No.']
    plt.bar(roll, marks, color='lightgreen', width=2, label='Marks of Top 10 Students', edgecolor='green')
    plt.xlabel('Roll No.')
    plt.ylabel('Marks')
    plt.title('Marks of Top 10 Students')
    plt.legend()
    for i in range(len(roll)):
        plt.text(roll.iloc[i], marks.iloc[i] + 1, str(marks.iloc[i]),
                 ha='center', va='bottom', fontsize=8, color='black')
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig('Bar Graph of Marks of Top 10 Students.pdf', dpi=600, bbox_inches='tight')
    plt.show()
    plt.close()

    # 🔹 Scatter plots (correlation)
    plt.scatter(english, maths, color='blue', marker='o')
    plt.xlabel('Marks in English')
    plt.ylabel('Marks in Maths')
    plt.grid(color='grey', linewidth=1, linestyle=':')
    plt.title('Correlation between English and Maths')
    plt.xticks(range(0, 101, 10))
    plt.yticks(range(0, 101, 10))
    plt.savefig('Correlation between English and Maths.pdf', dpi=600, bbox_inches='tight')
    plt.show()
    plt.close()

    plt.scatter(english, science, color='blue', marker='o')
    plt.xlabel('Marks in English')
    plt.ylabel('Marks in Science')
    plt.grid(color='grey', linewidth=1, linestyle=':')
    plt.title('Correlation between English and Science')
    plt.xticks(range(0, 101, 10))
    plt.yticks(range(0, 101, 10))
    plt.savefig('Correlation between English and Science.pdf', dpi=600, bbox_inches='tight')
    plt.show()
    plt.close()

    plt.scatter(science, maths, color='blue', marker='o')
    plt.xlabel('Marks in Science')
    plt.ylabel('Marks in Maths')
    plt.grid(color='grey', linewidth=1, linestyle=':')
    plt.title('Correlation between Science and Maths')
    plt.xticks(range(0, 101, 10))
    plt.yticks(range(0, 101, 10))
    plt.savefig('Correlation between Science and Maths.pdf', dpi=600, bbox_inches='tight')
    plt.show()
    plt.close()

    # 🔹 Trend line for a single student
    roll = int(input('Enter the roll no. of the student for line chart: '))
    plt.plot(['English', 'Maths', 'Science'],
             [english[roll - 1], maths[roll - 1], science[roll - 1]],
             color='orange', linewidth=1, marker='o', label='Marks in Subjects')
    plt.xlabel('Subjects')
    plt.ylabel('Marks')
    plt.title(f'Trend of Marks Across Subjects for Roll No. {roll}')
    plt.grid(color='grey', linewidth=1, linestyle=':')
    plt.legend()
    plt.show()
    plt.close()

    # 🔹 Box Plot
    plt.boxplot([english, maths, science], labels=['English', 'Maths', 'Science'])
    plt.title('Marks Spread Across Subjects')
    plt.ylabel('Marks')
    plt.grid(color='grey', linestyle=':', linewidth=1)
    plt.savefig('Subjects Box Plot.pdf', dpi=600, bbox_inches='tight')
    plt.show()
    plt.close()



students = np.arange(1,101,1)
english = np.random.randint(20, 101, size=100)
maths = np.random.randint(20, 101, size=100)
science = np.random.randint(20, 101, size=100)
total = english + maths + science



# Creating a csv file out of the random marks of students generated
dict = {'Roll No.':students,'English':english, 'Maths':maths, 'Science':science , 'Total':total}
marks = pd.DataFrame(dict)
marks.sort_values(by='Total',ascending=False,inplace=True)
marks.to_csv('Marks Of Students_Cleaned.csv',index=False)



# Working with creating a report out of the marks generated
with open("Report Card.txt", 'w') as f:
    with contextlib.redirect_stdout(f):

        print("-" * 40)
        print("The result of the Students are : ")
        print("-" * 40)

        for count, item in enumerate(total):
            print("\n" + "-" * 11)
            print(f"Student {count+1} : ")
            print("-" * 11)
            print(f"English - {english[count]} , Grade - {grade(english[count])}")
            print(f"Maths - {maths[count]} , Grade - {grade(maths[count])}")
            print(f"Science - {science[count]} , Grade - {grade(science[count])}")
            print(f"Total = {item}")
            print(f"Avg : {round(item/3, 3)}")

        rank = np.argsort(total)

        print("\n" + "-" * 40)
        print("Top Performers")
        print("-" * 40)
        for i in range(1, 6):
            r = 100 - i
            print(f"\nRank {i} : Student {rank[r]+1} (Total Marks - {total[rank[r]]})")

        print("\n" + "-" * 40)
        print("Top Performers in respective Subjects")
        print("-" * 40)
        print(f"\nRank 1 in English : Student {np.argmax(english)+1} (Marks - {english[np.argmax(english)]})")
        print(f"\nRank 1 in Maths : Student {np.argmax(maths)+1} (Marks - {maths[np.argmax(maths)]})")
        print(f"\nRank 1 in Science : Student {np.argmax(science)+1} (Marks - {science[np.argmax(science)]})")

        print("\n" + "-" * 40)
        print("Subject Wise Stats")
        print("-" * 40)

        print("-" * 20)
        print("English")
        print("-" * 20)
        print(f"Avg marks in English : {np.mean(english):.2f}")
        print(f"Median marks in English : {np.median(english):.2f}")
        print(f"Students failed in English : {english[english < 40].shape[0]}")

        print("\n" + "-" * 20)
        print("Maths")
        print("-" * 20)
        print(f"Avg marks in Maths : {np.mean(maths):.2f}")
        print(f"Median marks in Maths : {np.median(maths):.2f}")
        print(f"Students failed in Maths : {maths[maths < 40].shape[0]}")

        print("\n" + "-" * 20)
        print("Science")
        print("-" * 20)
        print(f"Avg marks in Science : {np.mean(science):.2f}")
        print(f"Median marks in Science : {np.median(science):.2f}")
        print(f"Students failed in Science : {science[science < 40].shape[0]}")

        count1 = 0
        count2 = 0
        count3 = 0
        for i in range(100):
            if english[i] >= 40 and maths[i] >= 40 and science[i] >= 40:
                count3 += 1
            elif (english[i] >= 40 and maths[i] >= 40) or (science[i] >= 40 and maths[i] >= 40) or (english[i] >= 40 and science[i] >= 40):
                count2 += 1
            else:
                count1 += 1
                
        print("\n" + "-" * 40)
        print("Class Result Summary")
        print("-" * 40)
        print(f"\nAvg marks of the Class : {np.mean(total):.2f}")
        print(f"\nStudents scored avg marks >= 75 : {total[total >= (75 * 3)].shape[0]}")
        print(f"\nStudents passed in only one subject : {count1}")
        print(f"\nStudents passed in two subjects : {count2}")
        print(f"\nStudents passed in all the three subjects : {count3}")



# Calling the plots() function to run all the required plots
plots()



print("✅ Report saved successfully to 'Report Card.txt'")