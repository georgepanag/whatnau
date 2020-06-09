drop database whatnau;

create database whatnau;
grant all privileges on whatnau.* to 'whatnau'@'localhost';
use whatnau;

create table _user(

userID bigint(16)  auto_increment,
email varchar(128),
usrname varchar(128),
pass varchar(128),
cr_cardID bigint(20)  ,
interests set("sports","music","arts","theater","cinema","politics","underground","festivals","fashion","undefined") default "undefined",
gender enum("M","F"),/*M=male , F=female*/
_type enum("O","SU"),/*O=organiser , SU=simple_user*/
job tinytext default NULL, 
corporation varchar(25) default NULL,
reg_date datetime default now(),
shared_space int(3) default 5/*shared event space*/,
primary key(userID)


)engine=InnoDB;

create table buddy_req(
reqID bigint(16)  auto_increment, 
from_user bigint(16), 
to_user bigint(16), 
is_accepted int(3) default 0,/* 0=under processing , 1=request accepted , 2=request rejected*/
primary key(reqID),

constraint FRIENDSHIP_REQ foreign key (from_user) references _user(userID) on delete cascade on update cascade
)engine=InnoDB;


create table buddies(
friendshipID bigint(16) not null auto_increment, 
userID bigint(16), 
buddy bigint(16),
dateEstablished datetime default now(),
primary key(friendshipID),
constraint FRIENDSHIP foreign key (userID) references _user(userID) on delete cascade on update cascade
)engine=InnoDB;



create table _event(

eventID bigint(16) auto_increment,
userID bigint(16) not null,
descr text ,
_type set("sports",'social','arts','business','study','food','workout',"travelling","undefined") default "undefined",
importance enum("LOW","MED","HIGH") default "HIGH",
start_date datetime default null,
_end_date datetime default null,
shared enum("YES","NO") default "NO",

primary key(eventID),
constraint EVENT_USER foreign key (userID) references _user(userID) on delete cascade on update cascade


)engine=InnoDB;



create table promoted_event( /*from organiser*/

promotedID bigint(16) not null auto_increment,
userID bigint(16) not null,
descr text,
category set("sports","music","arts","cinema","politics","underground","festivals","fashion","undefined") default "undefined",
entrance_value bigint(16),
target_aud enum("to all","only fans") default "to all",
start_date datetime,
end_date datetime,
location text,

primary key(promotedID),
constraint PROMOTED_USER foreign key (userID) references _user(userID) on delete cascade on update cascade



)engine=InnoDB;


create table participants(
userID bigint(16) not null,
promotedID bigint(16) not null,
review_score enum("no review","1","2","3","4","5","6","7","8","9","10") default "no review",
primary key(userID,promotedID),
constraint PARTICIPANTS_USER foreign key (userID) references _user(userID) on delete cascade on update cascade,
constraint PARTICIPANTS_PROMOTED foreign key (promotedID) references promoted_event(promotedID) on delete cascade on update cascade
	



)engine=InnoDB;

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



insert into promoted_event(userID,descr,category,entrance_value,target_aud,start_date,end_date,location) values (2,"test","arts,underground",10,"only fans","2020-02-13 21:00:00","2020-02-13 22:00:00","Patra"),
(2,"test2","musical",10,"to all","2020-02-14 11:00:00","2020-02-14 12:00:00","Athens"),
(3,"test3","sports",0,"to all","2020-03-13 15:00:00","2020-03-13 16:00:00","Thessaloniki"),
(4,"test4","arts",10,"only fans","2020-02-13 21:00:00","2020-02-13 22:00:00","Crete");



insert into _user(email,usrname,pass,cr_cardID,gender,_type,job,corporation,shared_space) values
("jason@gmail.com","jason","JJason","54546546","M","SU",null,null,0),
("mxins@freemail.gr","Marinero","you_shall_not_pass",null,"M","O",null,null,3),
("lil@hotmail.gr","Lily23","234523",null,"F","O","sales","SalesUK CO",5),
("bob@yahoo.gr","Bobos","whatever","088879889686986","M","O","Bar owner",null,2);


insert into buddies(userID,buddy) values (1,2),(2,3),(1,3),(3,2),(2,4),(1,4),(3,4);



/*for testing*/
insert into _event(userID,descr,_type,importance,start_date,_end_date,shared) values
(1,"Software Engineering Project","social,study","MED","2018-02-13 12:00:00","2018-02-13 13:00:00","NO"),
(1,"Hanging out","social","LOW","2018-02-13 14:00:00","2018-02-13 15:00:00","YES"),
(1,"undefined","undefined","MED","2018-02-13 16:00:00","2018-02-13 17:00:00","YES"),
(4,"basketball","sports","HIGH","2018-02-13 18:00:00","2018-02-13 19:00:00","NO"),
(2,"concert","arts,social","LOW","2020-02-13 20:23:34","2020-02-13 21:00:00","NO");

insert into buddy_req(from_user,to_user,is_accepted) values 
(1,4,0),
(2,4,0),
(1,3,0),
(3,4,0);


/*"update_shared_space_1" trigger updates <_user.shared_space> every time a shared event is going to be deleted when condition<_event.userID=_user.userID> is satisfied*/
delimiter $$
create trigger update_shared_space_1 before delete on _event
for each row
begin
	set @a:=(select shared from _event where userID=old.userID);
    if(@a="YES") then
		update _user set shared_space=shared_space+1 where _user.userID=old.userID;
	else
		update _user set shared_space=shared_space where _user.userID=old.userID;
	end if;
end $$
delimiter ;


delimiter $$
create trigger update_shared_space_2 before update on _event
for each row
begin
	set @t:=(select _type from _user where _user.userID=old.userID);
    
	set @sp:=(select shared_space from _user where _user.userID=old.userID);
    
    if (@t="SU") then
		if  ((old.shared="YES") and (new.shared="NO")) then
			if ((@sp>=0) and (@sp<5)) then
				update _user set shared_space=shared_space+1 where _user.userID=old.userID;
            else
				update _user set shared_space=shared_space+0 where _user.userID=old.userID;
			end if;            
		elseif ((old.shared="NO") and (new.shared="YES")) then
			if((@sp>0) and (@sp<=5)) then
				update _user set shared_space=shared_space-1 where _user.userID=old.userID;
			else
				signal sqlstate '45000' set message_text = "Limited_Priviledges:Please free some of your shared space";
            end if;
        else
			#signal sqlstate '45000' set message_text = "<else> 1";
			set @dummy= "same";
			#update _event set userID=new.userID,descr=new.descr,_type=new._type,importance=new.importance,start_date=new.start_date,_end_date=new._end_date where old.eventID=new.eventID;
		end if;
	else
		set @dummy="else";
		#update _event set userID=new.userID,descr=new.descr,_type=new._type,importance=new.importance,start_date=new.start_date,_end_date=new._end_date where old.eventID=new.eventID;
    end if;    
end $$    
    
delimiter ;
