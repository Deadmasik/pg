select c.c_no, title, round(avg(e.score),3) as s from courses as c
join exams as e on c.c_no = e.c_no
group by c.c_no;
