import pymysql
import os
os.system("cls")
db=input("Enter database name :-")
database=pymysql.connect(host="localhost",port=3306,user="root",password="",database=f"{db}")
cur=database.cursor()
print(f"Current Database={db}")
cur.execute("show tables")
tables=cur.fetchall()
tl=[]
for var in tables:
    t=var[0]
    tl.append(t)
while True:
    print()
    print()
    t_choice=(input(f"write name of your table :-\n-->  {tl[0]}\n-->  {tl[1]}\n-->  {tl[2]}\n-->  {tl[3]}\n-->  Exit  \n:- ")).lower().strip()
    #print(f"You have choosen {t_choice}")
    def o_ch():
        global o_choice
        o_choice=int(input("1. Insert \n2. Update\n3. Delete\n4. Show\n5. Exit\n Enter Your choice :-"))
    def stu():
        if t_choice =="student":
            o_ch()
            if o_choice == 1:
                #s_id=int(input("Enter s_id :- "))
                s_name=input("Enter s_name :- ")
                ph_no=input("enter ph_no :- ")
                course=input("Enter course name :- ")
                cur.execute(f"insert into {t_choice} values ('','{s_name}','{ph_no}','{course}');")
                print(" **** --- A new Row is inserted --- ****")
                database.commit()
            elif o_choice == 2:
                column_name=input("Enter column name to update :-")
                s_id=int(input("enter s_id to set the value (as a condition) :- ")) # we have used only s_id because this is primary key
                if column_name == "s_id":
                    new_value=int(input("Enter new value "))
                    cur.execute(f"update {t_choice} set {column_name}={new_value} where s_id={s_id};")
                else:
                    new_value=input("enter new value :-")
                    cur.execute(f"update {t_choice} set {column_name}='{new_value}' where s_id={s_id};")
                database.commit()
                print(" **** --- updated successfully --- ****")
            elif o_choice==3:
                print("NOTE :- you should know s_id to delete a row ")
                s_id=int(input("Enter s_id :-"))
                cur.execute(f"delete from {t_choice} where s_id ={s_id};")
                database.commit()
                print(" **** --- deleted successfully --- ****")
            elif o_choice==4:
                cur.execute(f"select * from {t_choice}")
                rows=cur.fetchall()
                cur.execute(f"desc {t_choice}")
                rows2=cur.fetchall()
                l=[]
                for var in rows2:
                    l1=var[0]
                    l.append(l1)
                print(*l,sep="     ")
                print()
                for var in rows:
                    if len(var) == 3:
                        print(var[0],var[1],var[2],sep="     ")
                    elif len(var) == 4:
                        print(var[0],var[1],var[2],var[3],sep="     ")
                    elif len(var) == 5:
                        print(var[0],var[1],var[2],var[3],var[4],sep="     ")
                    elif len(var) == 6:
                        print(var[0],var[1],var[2],var[3],var[4],var[5],sep="     ")
                    else:
                        print("plz go to code and increase limit ")

            elif o_choice==5:
                print("------ GOOD BYE -----")
                continue
        o_ch()
        stu()

    ########################################################################################################
    def fees():
        if t_choice =="fees":
            o_ch()
            if o_choice == 1:
                f_id=(input("Enter f_id :- "))
                fees=int(input("Enter fees amount :- "))
                discount=int(input("enter discount :- "))
                f_s_id=int(input("Enter f_s_id (f_k value) :- "))
                cur.execute(f"insert into {t_choice} values ('{f_id}',{fees},{discount},{f_s_id});")
                print(" **** --- A new Row is inserted --- ****")
                database.commit()
            elif o_choice == 2:
                column_name=input("Enter column name to update :-")
                f_id=(input("enter f_id to set the value (as a condition) :- ")) # we have used only f_id because this is primary key
                if column_name == "f_id":
                    new_value=(input("Enter new value "))
                    cur.execute(f"update {t_choice} set {column_name}='{new_value}' where f_id='{f_id}';")
                else:
                    new_value=int(input("enter new value :-"))
                    cur.execute(f"update {t_choice} set {column_name}={new_value} where f_id='{f_id}';")
                database.commit()
                print(" **** --- updated successfully --- ****")
            elif o_choice==3:
                print("NOTE :- you should know f_id to delete a row ")
                f_id=int(input("Enter f_id :-"))
                cur.execute(f"delete from {t_choice} where f_id ={f_id};")
                database.commit()
                print(" **** --- deleted successfully --- ****")
            elif o_choice == 4:
                cur.execute(f"select * from {t_choice}")
                rows=cur.fetchall()
                cur.execute(f"desc {t_choice}")
                rows2=cur.fetchall()
                l=[]
                for var in rows2:
                    l1=var[0]
                    l.append(l1)
                print(*l,sep="     ")
                print()
                for var in rows:
                    if len(var) == 3:
                        print(var[0],var[1],var[2],sep="     ")
                    elif len(var) == 4:
                        print(var[0],var[1],var[2],var[3],sep="     ")
                    elif len(var) == 5:
                        print(var[0],var[1],var[2],var[3],var[4],sep="     ")
                    elif len(var) == 6:
                        print(var[0],var[1],var[2],var[3],var[4],var[5],sep="     ")
                    else:
                        print("plz go to code and increase limit ")

            elif o_choice==5:
                print("------ GOOD BYE -----")
                continue
            o_ch()
            fees()

        ###############################################################################################################
        def addr():
            if t_choice =="address":
                o_ch()
                if o_choice == 1:
                    a_id=(input("Enter a_id :- "))
                    plotno=(input("Enter plotno :- "))
                    street=(input("Enter street :- "))
                    city=input("Enter city :-")
                    zip=input("Enter zip code")
                    a_s_id=int(input("Enter a_s_id (f_k value) :- "))
                    cur.execute(f"insert into {t_choice} values ('{a_id}','{plotno}','{street}','{city}','{zip}',{a_s_id});" )
                    print(" **** --- A new Row is inserted --- ****")
                    database.commit()
                elif o_choice == 2:
                    column_name=input("Enter column name to update :-")
                    a_id=(input("enter a_id to set the value (as a condition) :- ")) # we have used only s_id because this is primary key
                    if column_name == "a_s_id":
                        new_value=int(input("Enter new value "))
                        cur.execute(f"update {t_choice} set {column_name}={new_value} where a_id='{a_id}';")
                    else:
                        new_value=(input("enter new value :-"))
                        cur.execute(f"update {t_choice} set {column_name}='{new_value}' where a_id='{a_id}';")
                    database.commit()
                    print(" **** --- updated successfully --- ****")

                elif o_choice==3:
                    print("NOTE :- you should know a_id to delete a row ")
                    a_id=int(input("Enter a_id :-"))
                    cur.execute(f"delete from {t_choice} where a_id ={a_id};")
                    database.commit()
                    print(" **** --- deleted successfully --- ****")
                elif o_choice == 4:
                    cur.execute(f"select * from {t_choice}")
                    rows=cur.fetchall()
                    cur.execute(f"desc {t_choice}")
                    rows2=cur.fetchall()
                    l=[]
                    for var in rows2:
                        l1=var[0]
                        l.append(l1)
                    print(*l,sep="     ")
                    print()
                    for var in rows:
                        if len(var) == 3:
                            print(var[0],var[1],var[2],sep="     ")
                        elif len(var) == 4:
                            print(var[0],var[1],var[2],var[3],sep="     ")
                        elif len(var) == 5:
                            print(var[0],var[1],var[2],var[3],var[4],sep="     ")
                        elif len(var) == 6:
                            print(var[0],var[1],var[2],var[3],var[4],var[5],sep="     ")
                        else:
                            print("plz go to code and increase limit ")
                elif o_choice==5:
                    print("------ GOOD BYE -----")
                    continue
            o_ch()
            addr()
        def exit():
            if t_choice=="exit":
                database.close()
                print("------ GOOD BYE -----")
                break
            exit()
