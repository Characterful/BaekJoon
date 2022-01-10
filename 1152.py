wordCount = input()
count = 1

for ch in wordCount:
    if ch==" ":
        count+=1
if wordCount[0] == " ":
    count-=1
if wordCount[len(wordCount)-1] == " ":
    count-=1
print(count)
