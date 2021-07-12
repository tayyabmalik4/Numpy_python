# ***************for string operations,comparisond and informations*****************


import numpy as np
dream="I want to bulild Sultan Robort  "
future="This is my future and I Will "

# /////to joing two stings use add function
# print(np.char.add(dream,future))

# .....if we want to all the string in going to upper case
# print(np.char.upper(dream))
# /////if we want to all the lower case of string 
# print(np.char.lower(future))


# //////center function is use to center the string
# ------style-----np.char.center(string_name,lenght,fillchar="*")
# print(np.char.center(future,60,fillchar="*"))


# /////if we want to split the string then we use
# print(np.char.split(dream))


# /////if we want to split the line than we use this function
# print(np.char.splitlines("hello\nAI\nI am coming soon"))


# ////////////if we want to join the two strings than we use join function
str1="this is my dream"
str2="Artificial Intalligasnce"
# /////to joing the arrays
# print(np.char.join(["/",":"],[str1,str2]))


# //////if we want to replace any word or words then we use this function
# ---format------np.char.replace(variable_name,word or words,replacing_word or words)
# print(np.char.replace(str1,"this","who"))
# print(np.char.replace(str1,"this","who is that and that"))



# /////if the want to check equal or not than we use np.char.equal function
# /////if the strings are equal than it returns the true otherwise false
print(np.char.equal(str1,str2)) 


# ////if we count any word or charactor then we use the np.char.count(vasriable_name,"word or charactor")
print(np.char.count(str1,"a"))

# ////if we want to find the word or charactor then we use this function
# /////it returns the placing number
print(np.char.find(str1,"a"))

 