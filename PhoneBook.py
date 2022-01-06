d = {'simran':'fhgfdgd', 'hfgdfhgd':'vbfhdjgdh','bvjhfghda':'hfdgdash'}

def verify_phone_number(phone_number):
    if phone_number[0]=='+':
        f = phone_number[1:]
        if f.isdigit():
            if len(f)==12:
                d[user_name]=phone_number
                print("\n User Create \n")
            else:
                print("\n*****Enter 12 digit Phone Number******\n")
        else:
            print("\n******Enter a Valid Phone Number******\n")
    else:
        if phone_number.isdigit():
            if len(phone_number)==12:
                d[user_name]=phone_number
                print("\n User Create \n")
            else:
                print("\n******Enter 12 digit Phone Number******\n")
        else:
            print("\n*****Enter a Valid Phone Number*****\n")

while True:
    
    print("Create New Account Enter : 1 \n \
Search Account Enter : 2 \n \
Update Account Enter : 3 \n \
Delete Account Enter : 4 \n \
View all Account Enter : 5 \n\
Exit : 6 ")
    chioce_user = input("\n Please Enter your choice : ")

    #1. create user
    if chioce_user == "1":
        user_name = input("\nPlease Enter Name : ")
        phone_number = input("\nPlease Enter Phone Number : ")
        verify_phone_number(phone_number)

    #2.    find phone number
    elif chioce_user=="2":
        user_name = input("\nPlease Enter Name : ")
        if user_name in d:
            print(d[user_name])
        else:
            print("\n **********Not Found*********\n")

    #3.  update phone number
    elif chioce_user=="3":
        user_name = input("\nPlease Enter Name : ")
        if user_name in d:
            phone_number = input("\nPlease Enter Phone Number : ")
            if verify_phone_number(phone_number):
                d[user_name] = phone_number
                d.update({user_name:phone_number})
        else:
            print("\n***********Not Found********\n")

    #4. Delete account
    elif chioce_user=="4":
        user_name = input("\nPlease Enter Name : ")
        if user_name in d:
            d.pop(user_name)
            print("\n",d,"\n")
        else:
            print("\n*************Not Found***********\n")

    #5. show all object
    elif chioce_user=="5":
        print("\n",d,"\n")    

    elif chioce_user=="6":
        break
    else:
        print("enter valid data")
        break