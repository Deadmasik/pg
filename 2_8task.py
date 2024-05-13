import hashlib
import random

def students(N):
    global cursor, conn
    #s_id, name,start_year
    last_name = ['Иванов','Смирнов','Кузнецов','Попов','Васильев','Петров','Соколов','Михайлов','Новиков','Фёдоров']
    first_name = ['Марк','Лев','Максим','Михаил','Александр','Виктория','Алиса','Анна','Мария','Софья']

    b = N
    while b>0:
        t1 = random.randint(0,9)
        t2 = random.randint(0,9)
        name = ''
        if t2 >=5:
            name += last_name[t1] + 'а '+ first_name[t2]
        else:
            name += last_name[t1] + ' '+ first_name[t2]
        t3 = random.randint(2015, 2025)
        
        hash_t = hashlib.new('sha256')
        hash_t.update(name.encode('cp1251'))
        hex_t = hash_t.hexdigest()
        
        cursor.execute(f"select name from students where s_id= '{hex_t[0:16]}'; ")
        record = cursor.fetchone()
        if record!=None:
            continue
        
        cursor.execute("insert into Students(s_id, name, start_year) values ('{}','{}',{});".format(\
            hex_t[0:16], name, t3))
        conn.commit()
        b-=1
def courses(N):
    global cursor, conn
    #c_no, title, hours
    title = ['Русский язык','История','Иностранный язык','Экономическая теория','Социология','Философия',\
                 'Экология','Психология','ОБЖД','Физическая культура']
    hours = [i*12 for i in range(1,12)]
    b = N
    while b>0:
        t1 = random.randint(0,9)
        t2 = random.randint(0,9)
        name = title[t1] +str(hours[t2])
        hash_t = hashlib.new('sha256')
        hash_t.update(name.encode('cp1251'))
        hex_t = hash_t.hexdigest()
        
        cursor.execute("select title from courses where c_no='{}';".format(hex_t[0:16])) 
        record = cursor.fetchone()
        if record!=None:
            continue
        cursor.execute("insert into Courses(c_no, title, hours) values ('{}','{}',{});".format(\
            hex_t[0:16], title[t1], hours[t2]))
        conn.commit()
        b-=1
def exams(N):
    global cursor, conn
    cursor.execute("select c_no  from courses;")
    t1 = cursor.fetchall()
    cursor.execute("select s_id from students;")
    t2 = cursor.fetchall()
    b = N
    while b>0:
        t3 = t1[random.randint(0, len(t1)-1)][0]
        t4 = t2[random.randint(0, len(t2)-1)][0]
        t5 = random.randint(2,5)
        cursor.execute("select * from exams where s_id='{}' and c_no='{}';".format(t4, t3)) 
        record = cursor.fetchone()
        if record!=None:
            continue
        cursor.execute("insert into Exams(s_id, c_no, score) values ('{}', '{}', {});".format(t4,t3,t5))
        conn.commit()
        b-=1
import psycopg2
conn = psycopg2.connect(dbname='academy', user='postgres', 
                        password='docker', host='127.0.0.1',port="5400")
cursor = conn.cursor()
m = int(input("Введите количество новых студентов:(не больше 100)\n"))
n = int(input("Введите количество новых курсов(не больше 100):\n"))
l = input("Введите количество новых оценок(пропустить, если для каждого студента нужен экзамен)")
if l == '':
    l = m*n
students(m)
courses(n)
exams(int(l))

cursor.close()
conn.close()
