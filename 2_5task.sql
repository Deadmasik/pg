select name from students 
where s_id not in (select s_id from exams where score>2);