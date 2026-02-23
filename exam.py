import mysql.connector
def entry():
    print('WELCOME TO SHHSS ONLINE EXAMINATION PLATFORM')
    ID=int(input('YOUR ID:'))
    conn_object=mysql.connector.connect(host="localhost",username="root",password="password",database="MANAGEMENT")
    cur_object=conn_object.cursor()
    e,f,g='select* from students','select* from teachers','select* from management'
    cur_object.execute(e)
    STUDENTS=cur_object.fetchall()
    cur_object.execute(f)
    TEACHERS=cur_object.fetchall()
    cur_object.execute(g)
    MANAGEMENT=cur_object.fetchall()
    for i in STUDENTS:
        if i[0]==ID:
           studs(ID)
    for i in TEACHERS:
        if i[0]==ID:
           staff()
    for i in MANAGEMENT:
        if i[0]==ID:
           ADD_new()
    else:
        print('SORRY,YOU DO NOT BELONG TO OUR SCHOOL ASK THE MANAGEMENT TO ADD YOU IF YOU ARE NEW')
        exit()

def ADD_new():
    print("HERE, WE MANAGE THE RECORDS OF STAFF AND THE STUDENTS")
    new_member=input('Enter your name:')
    age=input('Enter your age:')
    choose=input("TEACHER OR STUDENT?")
    #cur_object.execute('use management;')
    conn_object=mysql.connector.connect(host="localhost",username="root",password="password",database="MANAGEMENT")
    cur_object=conn_object.cursor()
    val=()
    if choose.upper()=='TEACHER':
        subject=input('Enter your subject:')
        C=cur_object.rowcount()
        ID=C+1
        sql="INSERT INTO teachers(ID,NAME,SUBJECT,AGE) values(%s,%s,%s)"
        val=(new_member,subject,age)
        cur_object.execute(sql,val)
    elif choose.upper()=='STUDENT':
        cl=int(input("your class:"))
        sec=input('Enter your SECTION:')
        adm_no=cur_object.rowcount() +1
        sql="INSERT INTO students(ADM_NO,NAME,CLASS,SECTION,AGE) values(%s,%s,%s,%s,%s)"
        val=(adm_no,new_member,cl,sec,age)
        cur_object.execute(sql,val)
    conn_object.commit()
    cur_object.close()
    conn_object.close()
    entry()

def studs(I):
    l,stud_ans=[],[]
    cl=input("Class:")
    sub=input("Subject:")
    c=sub+cl
    file=open(c,'r')
    l=file.readlines()
    name=input('Enter your name:')
    f=name+c
    fi=open(f,'a')
    for i in range (0,len(l)-1,2):
        print('QUES.1',l[i])
        print(l[i+1])
        a=input("ANS.")
        stud_ans.append(a)
        fi.write('\n')
        fi.write(a)
    print("THANKYOU")
    c=0
    a=l[-1]
    for i in range (0,len(a)):
        if a[i]==stud_ans[i]:
            c+=1
    print(len(a))
    print('SCORES=',c,'/',len(a))
    for i in range(0,20):
     print()
    fi.close()
    file.close()
    print("THANKS FOR USING OUR PLATFORM.")
    exit()
def staff():
    ans=""
    sub=input("ENTER YOUR SUBJECT:")
    print("Let's create!")
    cl=input("Please enter your class:")
    #create a class text file
    c=sub+cl
    file=open(c,'a')
    max_que=int(input("Enter maximum number of questions:"))
    for i in range(0,max_que):
         que=str(input("Que"))
         file.write(que)
         file.write('\n')
         options=[]
         op=['a','b','c','d']
         for i in range(4):
            e=input(op[i])
            f=op[i]+e+"  "
            file.write(f)
         file.write('\n')
    ans=input('write answers sequence:')
    file.write(ans)
    file.close()
    print("THANKS FOR USING OUR PLATFORM.")
    exit()
global ans
Q=[]
global STUDENTS
global TEACHERS
global MANAGEMENT

entry()

