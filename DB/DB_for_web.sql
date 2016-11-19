BEGIN TRANSACTION;
CREATE TABLE "Users" (
	`Name`	TEXT NOT NULL,
	`Password`	TEXT NOT NULL,
	`Id_img`	INTEGER,
	`Info`	TEXT,
	`Mail`	TEXT
);
INSERT INTO `Users` VALUES ('User1','wefsf343',8,'Я хороший человек','fsdffd@mail.ru');
INSERT INTO `Users` VALUES ('User2','tgdfgd23232',9,'Я не очень','gfgd@mail.ru');
CREATE TABLE "Timetable" (
	`Name_event`	TEXT NOT NULL,
	`Time`	INTEGER NOT NULL,
	`Data`	DATE NOT NULL,
	`About`	TEXT,
	`Room`	INTEGER
);
INSERT INTO `Timetable` VALUES ('День рождения Антикафе!','19:00','21.11.2016','Приглашаем все на наш праздник!',1);
INSERT INTO `Timetable` VALUES ('Оригами','15:00','16.12.2015','Курсы оригами',3);
CREATE TABLE "Rooms" (
	`Room`	INTEGER NOT NULL,
	`About_r`	TEXT NOT NULL,
	`Id_img`	INTEGER
);
INSERT INTO `Rooms` VALUES (1,'Самое большое помещение,светлое и тд.',7);
INSERT INTO `Rooms` VALUES (2,'Самое маленькое помещение',6);
INSERT INTO `Rooms` VALUES (3,'Просторное помещение,несколько столов',5);
CREATE TABLE "Images" (
	`Id_img`	INTEGER NOT NULL,
	`Adr_im`	TEXT NOT NULL
);
INSERT INTO `Images` VALUES (1,'/images/1.img');
INSERT INTO `Images` VALUES (2,'/images/2.img');
INSERT INTO `Images` VALUES (3,'/images/3.img');
INSERT INTO `Images` VALUES (4,'/images/4.img');
INSERT INTO `Images` VALUES (5,'/images/5.img');
INSERT INTO `Images` VALUES (6,'/images/6.img');
INSERT INTO `Images` VALUES (7,'/images/7.img');
INSERT INTO `Images` VALUES (8,'/images/8.img');
INSERT INTO `Images` VALUES (9,'/images/9.img');
CREATE TABLE "Comments" (
	`Text`	TEXT NOT NULL,
	`Name`	TEXT NOT NULL,
	`Name_comment`	TEXT,
	`Data`	DATE NOT NULL,
	`Id_img`	INTEGER
);
INSERT INTO `Comments` VALUES ('Чудесное место!','User1','Понравилось!','27.14.16',4);
INSERT INTO `Comments` VALUES ('Все прошло хорошо!','User2','Понравилось!','1.11.2016',5);
CREATE TABLE "Admins" (
	`Name_ad`	TEXT NOT NULL,
	`Id_img`	INTEGER,
	`Phone`	TEXT NOT NULL,
	`Mail`	TEXT
);
INSERT INTO `Admins` VALUES ('Name1',1,'89654343478','fdf@mail.ru');
INSERT INTO `Admins` VALUES ('Name2',2,'87690000434','ghh@gmail.com');
INSERT INTO `Admins` VALUES ('Name3',3,'93436578900','nanan@mail.ru');
COMMIT;
