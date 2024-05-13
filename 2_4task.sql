insert into students(s_id, name, start_year) values ('68eb3f26eb871d51', 'Корочков Николай', 2023);
insert into students(s_id, name, start_year) values ('68eb3f26eb871d52', 'Козлов Николай', 2023);
insert into courses(c_no, title, hours) values ('1c8090e663a40d41', 'Теория Вероятности', 144);
insert into courses(c_no, title, hours) values ('1c8090e663a40d42', 'Статистика', 144);
insert into exams(s_id, c_no, score) values ('68eb3f26eb871d51', '1c8090e663a40d41', 3);
insert into exams(s_id, c_no, score) values ('68eb3f26eb871d52', '1c8090e663a40d41', 5);
insert into exams(s_id, c_no, score) values ('68eb3f26eb871d51', '1c8090e663a40d42', 2);
insert into exams(s_id, c_no, score) values ('68eb3f26eb871d52', '1c8090e663a40d42', 3);

--Можно еще множественно копировать из файла csv, где каждое значение будет записано через :,
-- а отдельная строчка это запись в таблице
--copy students(s_id, name, start_year) from 'students.csv' delimiter ':' encodinG 'UTF8' csv;
--copy courses(c_no, title, hours) from 'courses.csv' delimiter ':' encodinG 'UTF8' csv;
--copy exams(s_id, c_no, score) from 'exams.csv' delimiter ':' encodinG 'UTF8' csv;