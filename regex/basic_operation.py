import re

text = "The quick brown fox jumps over the lazy dog."
pattern = "fox"
match = re.search(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match found.")