user_pass=[{"user name":"yuva","password":"yuva@123"},{"user name":"ajay","password":"ajay@123"},{"user name":"vishnu","password":"vishnu@123"}]

while True:
    ent=input("Enter your user name :").strip().lower()
    pas=input("enter the password:").strip()
    if ent == user_pass[0]["user name"] and pas==user_pass[0]["password"] :
            print("welcome!!")      
            
    elif ent == user_pass[1]["user name"] and pas==user_pass[1]["password"] :
            print("welcome!!")

    elif ent == user_pass[2]["user name"] and pas==user_pass[2]["password"] :
            print("welcome!!")
    
    else:
        print("invalid enteries")
        
    break
