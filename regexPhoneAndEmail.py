#! python3
import re, pyperclip

# regex for phone number
phoneRegex = re.compile(r'''
# 123-123-1230, 222-1234, (123) 444-1234, 555-0987 ext 12345, ext. 12345, x2345

((\d\d\d)|(\(\d\d\d\)))?			# area code optional
(\s|-)								# first separator
\d\d\d								# first 3 digits
-									# separator
\d\d\d\d 							# last 4 digits
(((ext(\.)?\s)|x) 					# extension word-part optional
(\d{2,5}))?							# extension number-part optional


''', re.VERBOSE)

# regex for email
emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+						# name part
@									# @ symbol
[a-zA-Z0-9_.+]+						# domain part
	''', re.VERBOSE)

# get the text off the clipboard
text = pyperclip.paste()

# extract phone and email from the text
phoneExtracted = phoneRegex.findall(text)
emailExtracted = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in phoneExtracted:
	allPhoneNumbers.append(phoneNumber[0])

# print(phoneExtracted)
print(allPhoneNumbers)
print(emailExtracted)

# copy the extracted phone and email to clipboard
result = '\n'.join(allPhoneNumbers) + "\n" + '\n'.join(emailExtracted)
pyperclip.copy(result)