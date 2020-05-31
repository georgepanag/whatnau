create table _budget(
budget_ID bigint(16) auto_increment,
userID bigint(16) ,
day_selection enum("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"),
budget_upper_bound bigint(16) default 0,
monthly_budget bigint(16) default 0,
day_for_money_spent datetime, 
day_money_spent bigint(16) default 0,

primary key(budget_ID),

constraint BUDGET_USER foreign key (userID) references _user(userID) on delete cascade on update cascade

)engine=InnoDB;

insert into _budget(userID,day_selection, budget_upper_bound,monthly_budget,day_for_money_spent,day_money_spent)
values( '1', 14, 900,300,"2020-05-10 15:45:20",50 );
insert into _budget(userID,day_selection, budget_upper_bound,monthly_budget,day_for_money_spent,day_money_spent)
values( '2', 23, 1400, 500,"2020-06-01 10:30:40",30 );
insert into _budget(userID,day_selection)
values( '3', NULL);
insert into _budget(userID,day_selection)
values( '4', NULL);
