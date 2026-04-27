#Question 6: String Replace + Count
# Input sentence
# Replace "a" with "@"
# Count how many "a" were there

text = input("Enter your sentense: ")
count_a = text.count("a")
new_text = text.replace("a", "@")
print("the count of a is",count_a)
print("Modified:", new_text)