select name, count(*) from students as s
join exams as e on e.s_id=s.s_id
where score>2
group by s.s_id;