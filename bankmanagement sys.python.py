import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Nandan@143nayak',database='bms')

def open_account():
    name=input("Enter your name:")
    acc=input("Enter your acc no:")
    dob=input("Enter your DOB")
    add=input("Enter your address:")
    con=input("Enter your contact:")
    op_bal=int(input('Enter your opening balance:'))

    data1=(name,acc,dob,add,con,op_bal)
    data2=(name,acc,op_bal)

    sql1=('insert into account values(%s,%s,%s,%s,%s,%s)')
    sql2=('insert into account values(%s,%s,%s)')

    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)

    mydb.commit()
    print("Data entered successfully")
    main()

def deposit():
        amount=input('enter the amount to deposite:')
        acc=input("enter your acc no:")
        a="select balance from amount where acc_no=%s"
        data1=(acc,)
        x=mydb.cursor()
        x.execute(a,data1)
        result=x.fetchone()
        t=result[0]+amount
        sql=('update amount set balance where acc_no=%s')
        d=(t,acc)
        x.execute(sql,d)
        mydb.commit()
        print("_________________________________________")
        main()

def withdraw():
        amount=input('enter the amount to withdraw:')
        acc=input("enter your acc no:")
        a="select balance from amount where acc_no=%s"
        data1=(acc,)
        x=mydb.cursor()
        x.execute(a,data1)
        result=x.fetchone()
        t=result[0]-amount
        sql=('update amount set balance where acc_no=%s')
        d=(t,acc)
        x.execute(sql,d)
        mydb.commit()
        print("_________________________________________")
        main()
        
def balance():
        acc=input("enter the account number:")
        a="select*from amount where acc_no=%s"
        data=(ac,)
        x=mydb.cursor()
        x.execute(a,data)
        mydb.commit()
            
def main():
     print("""
          1.open new account
          2.deposite amount
          3.withdraw amount
          4.balance enquiry
          5.show customer details
          6.close account
           """)
     choose=int(input("choose your option:"))
     if(c==1):
        open()
        print("1.open new acc")
     elif(c==2):
        deposit()
        print("2.deposite amount")
     elif(c==3):
        withdraw()
        print("3.withdraw amount")
     elif(c==4):
        balance()
        print("4.balancy enquiry")
     elif(c==5):
        showcustomer()
        print("5.show customer details")
     elif(c==6):
        close()
        print("6.close account")
     else:
        print("enter the valid number")
        main()
main()
                

            
