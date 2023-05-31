letter ='''Dear <|NAME|>
Your are selected
Date: <|DATE|>

'''
name=input("Enter the name ")
date=input("Enter the date")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)