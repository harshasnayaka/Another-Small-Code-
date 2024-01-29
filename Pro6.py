print("A Small Code About Login Interface")
username = input("Enter Your Username : ")
password = input("Enter Your Password : ")
print("Accept Guidelines")
#captcha = int(input("Enter Captcha : "))
captcha = int(input("Enter Your Captcha :"))
if captcha == 123456:
    print("Login To Your Account ! ")
else:
    print("Invalid Captcha")