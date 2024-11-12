text = "Please email us at mentor@rahulshettyacademy.com with below template to receive response"
test = text.split("at ")[1].split()[0].strip()
print(test)