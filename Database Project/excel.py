
# for row in rows:
#     print(row)

import pandas as pd


# mylist = [[1, "Anas", 67], [2, "Ammar", 95],
#           [3, "Jawwad", 96], [4, "Zimad", 99]]

# working
# df = pd.DataFrame(mylist)
# # writer = pd.ExcelWriter('student_results.xlsx', engine='xlsxwriter')
# # df.to_excel(writer, sheet_name="percentage", index=False)

# with pd.ExcelWriter('student_result.xlsx') as writer:
#     df.to_excel(writer, sheet_name='percentage')

# working
# df1 = pd.DataFrame(mylist, columns=['ID', 'Name', 'Percentage'])
# df1.to_excel("output.xlsx")


# trying for calypso test case analysis
mydict = {"tes1": 69, "test2": 70, "test3": 34}

mylist = [(k, v) for k, v in mydict.items()]

print(mylist)
df = pd.DataFrame(mylist, columns=["name", "time(secs)"])
print(df)
