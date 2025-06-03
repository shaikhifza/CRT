create database practice;
use practice;
create table student(
roll_no int primary key,
name varchar(150) not null,
course_name varchar(100) not null
);
create table details(
roll_no int,
address text,
phone_no varchar(20) not null,
foreign key(roll_no) references student(roll_no)
);
insert into details(roll_no,name,course_name)values
(101,"AA","aids"),
(102,"BB","cse"),
(103,"CC","ece"),
(104,"DD","mec"),
(105,"EE","aids");
select*from student;
insert into details(roll_no,address,phone_no)values
(101,"builtup",37677687),
(102,"almaspet",8777656),
(103,"ravindra nagar",87767668),
(104,"hgfvb ",86676777),
(105,"circle",7779088);
create table details(
roll_no int,
address text,
phone_no varchar(20) not null,
foreign key(roll_no) references student(roll_no)
);
insert into details(roll_no,address,phone_no)values
(101,null,"37677687"),
(102,null,"8777656"),
(103,null,"87767668"),
(104,"hgfvb ","86676777"),
(105,"circle","7779088");
select*from details;

select*from student
join details
on student.roll_no=details.roll_no;
select s.roll_no,s.name,s.course_name,d.phone_no
from student s
left join details d
on s.roll_no=d.roll_no
insert into student value(10,"hello","ece");
select *from student;
select s.roll_no,s.name,s.course_name,d.phone_no
from student s
left join details d
on s.roll_no=d.roll_no;
select*
from details 
right join student 
on student.roll_no=details.roll_no;