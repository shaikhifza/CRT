create database practice;
use practice;
create table student(
Rollno int primary key,
Sname varchar(150) not null,
Cname varchar(100) not null
);
create table details(
Rollno int,
Address text,
Pno varchar(20) not null,
foreign key (Rollno) references student(Rollno)
);
insert into student(Rollno,Sname,Cname) values
(101,"Hifza","AI"),
(102,"Sai","CSE"),
(103,"Bhavya","AI"),
(104,"Sowmya","ECE"),
(105,"Ramya","EEE");
select*from student;

insert into details(Rollno,Address,Pno) values
(101,"HYD",1234),
(102,"",5678),
(103,"CHN",2790),
(104,"HYD",0987),
(105,"",8765);
select*from details;
truncate table details;
select*from details;

insert into details(Rollno,Address,Pno) values(101,NULL,5648);
insert into details(Rollno,Address,Pno) values(104,"HYD",5641);
insert into details(Rollno,Address,Pno) values(105,"BLR",9648);
insert into details(Rollno,Address,Pno) values(102,NULL,5758);
insert into details(Rollno,Address,Pno) values(103,"CHN",5648);
select*from details;
select*
from student 
join details
on student.Rollno=details.Rollno;
select s.Rollno,s.Sname,s.Cname,d.Pno
from student s
right join details d
on s.Rollno=d.Rollno
insert into student values(107,"Hello","ECE");
select*from student;Pno
select s.Rollno,s.Sname,s.Cname,d.
from student s
left join details d
on s.Rollno=d.Rollno
select *
from details d
right join student s
on d.Rollno=s.Rollno

