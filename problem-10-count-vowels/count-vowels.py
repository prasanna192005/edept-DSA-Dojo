# Problem 10: Count Vowels
# Edept Dojo
s=input().strip().lower(); 
print(sum(ch in "aeiou" for ch in s))
