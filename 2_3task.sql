drop table if exists exams;
drop table if exists courses;
drop table if exists students;
create table if not exists students
(
    s_id varchar(16) primary key,
    name text not null,
	start_year smallint not null 
);
alter table students
add constraint start_year
check(start_year > 0);

create table if not exists courses
(
    c_no varchar(16) primary key,
    title text not null,
	hours smallint not null check(hours > 0)
);
alter table courses
add constraint hours
check(hours > 0);

create table if not exists exams(
	s_id varchar(16) not null,
	foreign key (s_id) references students(s_id),
	c_no varchar(16) not null,
	foreign key (c_no) references courses(c_no),
	score smallint not null check(score > 1 and score < 6),
	constraint test_pkey primary key (s_id, c_no)
);
