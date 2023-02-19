# import re
# mylist = ["hello", "wassup"]
# # string = "h*"
# # temp = re.escape(string)
# # newlist = list(filter(temp.match, mylist))
# # print(newlist)
# # print(list(newlist))

# filtered_values = list(filter(lambda v: re.match('h*', v), mylist))

# print(filtered_values)
import re



     
# initializing string
# test_str = 'geeksforgeeks is best for geeks'
 
# # printing original string
# print("The original string is : " + str(test_str))
 
# initializing Substring
sub_str = 'k*'
 
# Wildcard Substring search
# Using re.search()
temp = re.compile(sub_str)
print(re.search(temp, "kevin1").groups())
# res = temp.search(test_str)
 
# # printing result
# print("The substring match is : " + str(res.group(0)))