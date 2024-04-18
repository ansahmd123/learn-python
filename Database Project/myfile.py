# from iteration_utilities import flatten
import jenkins


# def download_test_report(jenkins_url, name, buildNumer, pwd):
#     jenkins_server = jenkins.Jenkins(
#         jenkins_url, username='vishal.wasekar@adenza.com', password=pwd)
#     return jenkins_server.get_build_test_report(name, buildNumer)

# def compare_test_reports(report1, report2):
#     # Get test cases count for each job
#     testsForJob1 = generateTestsDetailsDict(report1)
#     # testsForJob2 = generateTestsDetailsDict(report2)

#     # print(f"Test Cases Count for MO: {len(testsForJob1)}")
#     # print(f"Test Cases Count for MR17: {len(testsForJob2)}")

#     #aisa tha
#     # differences, extaTests = find_difference(testsForJob1, testsForJob2)
#     # extaTests = find_difference(testsForJob1, testsForJob2)

#     #aisa kiya
#     # extaTests = find_difference(testsForJob1)

#     # print("Differences in tests:")
#     # for key, val in differences.items():
#     #     print(f"{key} : {val}")

#     print("**********************************")
#     print("**********************************")

#     print("Extra tests available:")

#     for key, val in extaTests.items():
#         print(f"{key} : {val}")

# def find_difference(dict1, dict2):
#     # differences = {}
#     extaTests = {}
#     all_keys = set(dict1.keys()) | set(dict2.keys())  # Get all keys

#     for key in all_keys:
#         # if key in dict1 and key in dict2:  # If key is common in both dictionaries
#         #     difference = dict1[key] - dict2[key]
#         #     differences[key] = difference
#         # elif key in dict1:  # If key is present only in dict1
#         #     extaTests[key] = dict1[key]     # only mo18
#         # elif key in dict2:  # If key is present only in dict2
#         #     extaTests[key] = dict2[key] + " : Only available in MR17"

#         if key in dict1:
#             extaTests[key] = dict1[key]

#     # Sort the differences dictionary by absolute value of the difference in descending order
#     # differences = dict(sorted(differences.items(), key=lambda x: round(x[1], 2), reverse=True))
#     extaTests = dict(sorted(extaTests.items(), key=lambda x: round(x[1], 2), reverse=True))
#     # extaTests = dict(sorted(extaTests.items(),reverse=True))
#     # extaTests = sorted(extaTests.items(), key=lambda kv: (kv[1], kv[0]))


#     # return differences,extaTests
#     return extaTests



# def generateTestsDetailsDict(report):
#     mydict = []
#     for suits in report['suites']:
#         for cases in suits['cases']:
#             # mydict[cases['className']+"#"+cases['name']] = cases['duration']
#             mydict.append([cases['className'].rsplit('.', 1),
#                           cases['name'], cases['duration']])
#     # mydict = dict(sorted(mydict.items(), key=lambda x: round(x[1], 2), reverse=True))
#     return (mydict)


if __name__ == "__main__":
    # Download test reports for two different jobs
    # report1 = download_test_report("https://jenkins.calypso.com/jenkins",
    #                                "CORE-MIDDLEOFFICE_18-fi-crd-e2eCommitStage", 159, "1138aadabeffeb1d8c16a5ce1ecf03b97b")
    # report2 = download_test_report("https://hfserver.calypso.com/jenkins", "mr17-bugs-secfinance-CommitStage", 576,"11db7a8cd94d23bc310418bda9d6afadf4")

    # Compare test reports
    # compare_test_reports(report1, report2)
    # dict = generateTestsDetailsDict(report1)
    
    # print(dict)
    # sorted_dict = dict.sort(key=lambda x:x[2])
    # sorted_dict = sorted(dict, key=lambda x: round(x[2], 2), reverse=True)
    # print(sorted_dict)

    # new_list = []
    # for nlist in sorted_dict:
    #     new_list.append((nlist[0]))
    # new_list.append(list(flatten(sorted_dict[0][0])))
    
    

    

    # print(type(suites_list[0]))
    all_tests = []
    for mydict in suites_list:
        for x in mydict['cases']:
            test = [x['className'].rsplit('.',1),x['name'],x['duration']]
            flat_test = [item for sublist in test for item in (sublist if isinstance(sublist, list) else [sublist])]
            all_tests.append(flat_test)
    all_tests = sorted(all_tests, key=lambda x: round(x[3], 2), reverse=True)
        # print(mydict.keys())
    print(len(all_tests))
    
    import pandas as pd
    df = pd.DataFrame(all_tests[:20],columns=['package','class','test name','time'])
    df.to_excel('top20_test_report.xlsx')
    # suites_list = report1['suites']

    # print(type(suites_list[0]))

    # import pandas as pd
    # df = pd.DataFrame(sorted_dict[:10],columns=["package","class name","test name","time"])
    # df.to_excel("testcasesexcel.xlsx")