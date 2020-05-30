/* Enas tropos:Na pairneis to cr_cardID mesw toy _user.userID ("select cr_cardID from _budget where _budget.userID=_user.userID")*/
create table _budget(
budget_ID bigint(16) auto_increment,
userID bigint(16) ,
day_selection enum("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"),

#cr_cardID bigint(20) ,
budget_upper_bound bigint(16) default 0,
monthly_budget bigint(16) default 0,

primary key(budget_ID),

constraint BUDGET_USER foreign key (userID) references _user(userID) on delete cascade on update cascade
#constraint CREDIT_CARD_USER foreign key (cr_cardID) references _user(cr_cardID) on delete cascade on update cascade
)engine=InnoDB;


insert into _budget(userID,day_selection, budget_upper_bound,monthly_budget)
values( '1', 14, 900,300 );
insert into _budget(userID,day_selection, budget_upper_bound,monthly_budget)
values( '2', 23, 1400, 500 );
insert into _budget(userID,day_selection)
values( '3', NULL);
insert into _budget(userID,day_selection)
values( '4', NULL);
