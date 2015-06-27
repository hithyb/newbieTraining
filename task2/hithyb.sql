use employees;



select * from employees where hire_date=(select min(hire_date)from employees);







update salaries set salary=salary+1 where emp_no in(select emp_no from employees where gender='M');






delete employees,dept_emp,dept_manager,salaries,titles from employees
left join dept_emp     ON employees.emp_no=dept_emp.emp_no 
left join dept_manager ON employees.emp_no=dept_manager.emp_no 
left join salaries     ON employees.emp_no=salaries.emp_no 
left join titles       ON employees.emp_no=titles.emp_no 
where employees.last_name='Acton';



insert into departments values
("d010","doubi");
insert into employees values
(846849587,"1995-10-21","BG2","CYR",'M',"2015-6-20");
insert into titles values
(846849587,"doubi","2015-6-20","2020-12-1");
insert into salaries values
(846849587,23333,"2015-6-20","2020-12-1");
insert into dept_emp values
(846849587,"d010","2015-6-20","2020-12-1");
insert into dept_manager values
("d010",846849587,"2015-6-20","2020-12-1");
