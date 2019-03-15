text="""Hello python , how are you today.
today is Monday and There are 2 on the table"""
find="on"
counter=0

for Index in range(len(text)):
    if(text[Index]==find[0]):
        fLen=len(find)
        sub=text[Index:Index+fLen]
        if(sub==find):
            counter+=1;
print("Word",find,"in text",counter)