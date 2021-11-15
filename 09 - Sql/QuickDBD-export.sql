-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE `department` (
    `dept_no` varchar(10)  NOT NULL ,
    `dept_name` varchar(25)  NOT NULL ,
    `last_updated` datetime  NOT NULL ,
    PRIMARY KEY (
        `dept_no`
    )
);

CREATE TABLE `employees` (
    `emp_no` int  NOT NULL ,
    `emp_title` varchar(10)  NOT NULL ,
    `birth_date` datetime  NOT NULL ,
    `first_name` varchar(25)  NOT NULL ,
    `last_name` varchar(25)  NOT NULL ,
    `sex` varchar(1)  NOT NULL ,
    `hire_date` datetime  NOT NULL ,
    `last_updated` datetime  NOT NULL ,
    PRIMARY KEY (
        `emp_no`
    )
);

CREATE TABLE `dept_emp` (
    `id` serial  NOT NULL ,
    `emp_no` int  NOT NULL ,
    `dept_no` varchar(10)  NOT NULL ,
    `last_updated` datetime  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `dept_manager` (
    `id` serial  NOT NULL ,
    `dept_no` varchar(10)  NOT NULL ,
    `emp_no` int  NOT NULL ,
    `last_updated` datetime  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `salaries` (
    `id` serial  NOT NULL ,
    `emp_no` int  NOT NULL ,
    `salary` int  NOT NULL ,
    `last_update` datetime  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `titles` (
    `title_id` varchar(10)  NOT NULL ,
    `title` varchar(25)  NOT NULL ,
    `last_updated` datetime  NOT NULL ,
    PRIMARY KEY (
        `title_id`
    )
);

ALTER TABLE `employees` ADD CONSTRAINT `fk_employees_emp_title` FOREIGN KEY(`emp_title`)
REFERENCES `titles` (`title_id`);

ALTER TABLE `dept_emp` ADD CONSTRAINT `fk_dept_emp_emp_no` FOREIGN KEY(`emp_no`)
REFERENCES `employees` (`emp_no`);

ALTER TABLE `dept_emp` ADD CONSTRAINT `fk_dept_emp_dept_no` FOREIGN KEY(`dept_no`)
REFERENCES `department` (`dept_no`);

ALTER TABLE `dept_manager` ADD CONSTRAINT `fk_dept_manager_dept_no` FOREIGN KEY(`dept_no`)
REFERENCES `department` (`dept_no`);

ALTER TABLE `dept_manager` ADD CONSTRAINT `fk_dept_manager_emp_no` FOREIGN KEY(`emp_no`)
REFERENCES `employees` (`emp_no`);

ALTER TABLE `salaries` ADD CONSTRAINT `fk_salaries_emp_no` FOREIGN KEY(`emp_no`)
REFERENCES `employees` (`emp_no`);

