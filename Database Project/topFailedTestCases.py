import pandas as pd
from openpyxl import load_workbook
# existing_file = "top failed tests.xlsx"
target_week = 12


def myfunction(branches, target_week):
    for branch in branches: 
        existing_data = pd.read_excel("top failed tests.xlsx")
        df_week_branch = df[(df['week'] == target_week) & (df['Branch'] == branch)].head(10)
        test_failures_per_branch = df_week_branch.groupby('FailedTests').size().reset_index(name='Failures')
        test_failures_per_branch = test_failures_per_branch.sort_values(by='Failures', ascending=False)
        
        # append data into existing sheet
        # Append new data to existing DataFrame
        # appended_data = existing_data.append(test_failures_per_branch, ignore_index=True)
        appended_data = pd.concat([existing_data, test_failures_per_branch], ignore_index=True)
        # Set index=False to avoid writing row numbers to Excel
        appended_data.to_excel("top failed tests.xlsx", index=False)
        # convert to list to append
        # test_list = test_failures_per_branch.values.tolist()
        # test_list = sorted(test_list, key=lambda x: round(x[1], 0), reverse=True)
        # test_list = test_list[:10]
        # wb = load_workbook(existing_file)
        # ws = wb.active
        # for row in test_list:
        #     ws.append(row)
        # wb.save(existing_file)   
             
        # logic to convert data into excel sheet (branch,test case,failure count)
        # test_failures_per_branch
    
        # new workbook
        # with pd.ExcelWriter("top failed tests.xlsx") as writer:
        #     test_failures_per_branch.to_excel(writer, sheet_name="test cases")
        
        # # existing workbook
        # with pd.ExcelWriter(existing_file, mode="a", engine="openpyxl") as writer:
        #     test_failures_per_branch.to_excel(writer, sheet_name="calib")
            
       

if __name__ == "__main__":
    df = pd.read_excel('tests-analysis-report.xlsx',sheet_name=2)
    branches = ['FEATURE-TEST-HSQLDBUPG', 'mr17-bugs', 'CORE-FRONTOFFICE_18', 'FEATURE-V17-RUNTIME-JAVA17', 'CORE-BACKOFFICE_18']
    # df_week = df[df['week'] == target_week]
    # branches = 'CORE-MIDDLEOFFICE_18'
    # myfunction(branches,12)
    df_week = df[df['week'] == 13]
    for branch in branches:
        existing_data = pd.read_excel("top failed tests.xlsx")
        test_failures_per_branch = df_week.groupby(['Branch', 'FailedTests']).size()
        test_failures_per_branch = test_failures_per_branch.reset_index(name='Failures')
        test_failures_per_branch = test_failures_per_branch.sort_values(by=['Branch', 'Failures'], ascending=[True, False])
        top_failed_tests_for_branch = test_failures_per_branch[test_failures_per_branch['Branch'] == branch].head(10)

        appended_data = pd.concat([existing_data, test_failures_per_branch], ignore_index=True)
        # Set index=False to avoid writing row numbers to Excel
        appended_data.to_excel("top failed tests.xlsx", index=False)
        