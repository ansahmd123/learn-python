import pandas as pd
import re

mydict = {'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[18]': 137.599, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[19]': 131.41, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[14]': 39.286, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[17]': 39.008, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[16]': 38.662, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[13]': 38.117, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[15]': 36.921, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[21]': 35.901, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[6]': 35.422, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[8]': 35.387, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[1]': 35.353, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[12]': 35.293,
          'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[4]': 35.207, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[20]': 35.037, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[0]': 34.437, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[5]': 34.351, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[7]': 34.229, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[10]': 33.659, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[9]': 32.567, 'com.calypso.tk.product.TestCDSIndexForNPV#testPricerCDSIndexTrade[0]': 31.979, 'com.calypso.tk.product.TestPricerCDSNthDefault#testCDSNthDefault[11]': 30.563, 'com.calypso.tk.product.TestCorrelationSurfGeneration#testCorrelationSurfaceGeneration[4]': 27.55, 'com.calypso.tk.product.TestPricerCDSIndexOption#testCDSIndexOption[7]': 27.194}

mylist = [(k, v) for k, v in mydict.items()]

mylist = mylist[:1]
# print((mylist[0]))

single_tuple = mylist[0]

# print(single_tuple)
single_list = list(single_tuple)
# print(single_list)

single_str = single_list[0]
print(single_str)

parts = single_str.split('#')
result = parts[0].split('.') + parts[1]

print(result)


# print(single_str.rsplit('.', 1))

# print(re.split('[.]', single_str, -1))
# single_str_list = single_str.split('#')
# single_str_list = single_str.rsplit('.', 1)
# single_str_list = single_str_list[1].split('#')
# print(single_str_list)


# print(type(mylist[0]))

# with pd.ExcelWriter('student_result.xlsx') as writer:
#     df.to_excel(writer, sheet_name='percentage')

# df = pd.DataFrame(mylist, columns=["test name", "time(secs)"])
# # print(df)
# df.to_excel("long_running_test_cases.xlsx")
