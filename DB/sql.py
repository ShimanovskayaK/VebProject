from sqlalchemy import create_engine,Table,Column,MetaData,Integer,String,ForeignKey,Date,Float
import os

if os.path.exists("avtograf.db"):
    os.remove("avtograf.db")

engine = create_engine("sqlite:///avtograf.db")
metaData=MetaData()

Users_Table = Table('Users', metaData,
                    Column('Id_img',Integer,ForeignKey('Images.Id_img')),
                    Column('Name',String, nullable = False,primary_key = True),
                    Column('Password',String,nullable = False),
                    Column('Mail',String,nullable = False),
                    Column('Info',String)
                    )

Timetable = Table('Timetable',metaData,
                    Column('Time',String,nullable = False),
                    Column('Data',Date,nullable = False),
                    Column('Name_event',String,nullable = False),
                    Column('About', String),
                    Column('Room',Integer,nullable = False,ForeignKey('Rooms.Room'))
                    )

Rooms_table = Table('Rooms',metaData,                 
                    Column('Room', Integer,nullable=False,primary_key = True),                     
                    Column('Id_img',Integer,nullable=False,ForeignKey('Images.Id_img')),
                    Column('About_r',String)
                    )

Images_Table = Table('Images',metaData,
                    Column('Id_img',Integer, nullable = False,primary_key = True)
                    Column('Adr_img', String, nullable = False)
                    )

Comments_Table = Table('Comments', metaData,
                    Column('Id_img',Integer,nullable = False,ForeignKey('Images.Id_img')),
                    Column('Name_comment', String,nullable = False),
                    Column('Text',String,nullable = False))                    
                    Column('Name', String, ForeignKey('Users.Name'),ForeignKey('Admins.Name_ad')),
                    Column('Data',Date ,nullable = False)
                    )

Admins_Table = Table('Admins', metaData,
                    Column('Id_img',Integer,nullable = False,ForeignKey('Images.Id_img')),
                    Column('Name_ad',String, nullable = False,primary_key = True),
                    Column('Phone',String, nullable = False),
                    Column('Mail',String, nullable = False)
                    )
