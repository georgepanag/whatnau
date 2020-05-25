drop database whatnau;
create database whatnau;
use whatnau;

create table _user(

userID bigint(16)  auto_increment,
email varchar(128),
usrname varchar(128),
pass varchar(128),
cr_cardID bigint(20) ,
interests set("sports","music","theater","cinema","politics","underground","festivals","fashion","undefined") default "undefined",
gender enum("M","F"),/*M=male , F=female*/
_type enum("O","SU"),/*O=organiser , SU=simple_user*/
job tinytext default NULL, 
corporation varchar(25) default NULL,
reg_date datetime default now(),
space int(3) default 5/*shared event space*/,
primary key(userID)


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
descr text,
_type set("sports",'social','arts','business','study','food','workout',"travelling","undefined") default "undefined",
importance enum("LOW","MED","HIGH") default "HIGH",
start_date datetime,
_end_date datetime,
shared enum("YES","NO") default "NO",

primary key(eventID),
constraint EVENT_USER foreign key (userID) references _user(userID) on delete cascade on update cascade


)engine=InnoDB;



create table promoted_event(

promotedID bigint(16) not null auto_increment,
userID bigint(16) not null,
descr text,
category set("sports","music","theater","cinema","politics","underground","festivals","fashion","undefined") default "undefined",
entrance_value bigint(16),
target_aud enum("to all","only fans") default "to all",
start_date datetime,
end_date datetime,

primary key(promotedID),
constraint PROMOTED_USER foreign key (userID) references _user(userID) on delete cascade on update cascade



)engine=InnoDB;


create table participants(
userID bigint(16) not null,
promotedID bigint(16) not null,
comments text,
primary key(userID,promotedID),
constraint PARTICIPANTS_USER foreign key (userID) references _user(userID) on delete cascade on update cascade,
constraint PARTICIPANTS_PROMOTED foreign key (promotedID) references promoted_event(promotedID) on delete cascade on update cascade


)engine=InnoDB;



/*use whatnau;*/
insert into _user(email,usrname,pass,cr_cardID,gender,_type,job,corporation) values
("jason@gmail.com","jason","JJason","54546546","M","SU",null,null),
("mxins@freemail.gr","Marinero","you_shall_not_pass",null,"M","SU",null,null),
("lil@hotmail.gr","Lily23","234523",null,"F","O","sales","SalesUK CO"),
("bob@yahoo.gr","Bobos","whatever","088879889686986","M","O","Bar owner",null);


insert into buddies(userID,buddy) values (1,2),(2,3),(1,3),(3,2);


insert into _event(userID,descr,_type,importance,start_date,_end_date,shared) values
(1,"Software Engineering Project","social,study","MED","2018-02-13 12:23:34","2018-02-13 15:23:34","NO"),
(2,"Hanging out","social","LOW","2018-02-13 17:23:34","2018-02-13 20:23:34","YES"),
(3,"undefined","undefined","MED","2018-02-13 20:23:34","2018-03-13 20:23:34","NO"),
(2,"basketball","sports","HIGH","2018-02-13 18:23:34","2018-02-13 21:23:34","NO"),
(4,"concert","arts,social","LOW","2020-02-13 20:23:34","2020-02-13 23:00:00","YES");




