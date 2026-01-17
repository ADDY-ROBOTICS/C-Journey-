email = input("Enter your email here ")
index = email.index("@")

username = email[:index]
domain = email[index + 1:]

print(f"The username of the email is {username}")
print (f"the email is hosted by {domain}")