from sqlalchemy import create_engine,Table,Column,MetaData,Integer,String,ForeignKey,Date,Float
import os

if os.path.exists("avtograf.db"):
    os.remove("avtograf.db")

engine = create_engine("sqlite:///avtograf.db")
metaData=MetaData()

Users_Table = Table('Users', metaData,
                    Column('Id_img',Integer),
                    Column('Name',String, nullable = False),
                    Column('Password',String,nullable = False),
                    Column('Mail',String,nullable = False),
                    Column('Info',String)
                    )

Timetable = Table('Timetable',metaData,
                    Column('Time',String,nullable = False),
                    Column('Data',Date,nullable = False),
                    Column('Name_event',String,nullable = False),
                    Column('About', String),
                    Column('Room',Integer,nullable = False)
                    )

Rooms_table = Table('Rooms',metaData,
                    Column('Room', Integer,nullable=False),
                    Column('Id_img',Integer,nullable=False),
                    Column('About_r',String)
                    )

Images_Table = Table('Images',metaData,
                    Column('Id_img',Integer, nullable = False),
                    Column('Adr_img', String, nullable = False)
                    )

Comments_Table = Table('Comments', metaData,
                    Column('Id_img',Integer,nullable = False),
                    Column('Name_comment', String,nullable = False),
                    Column('Text',String,nullable = False),
                    Column('Name', String),
                    Column('Data',Date ,nullable = False)
                    )

Admins_Table = Table('Admins', metaData,
                    Column('Id_img',Integer,nullable = False),
                    Column('Name_ad',String, nullable = False),
                    Column('Phone',String, nullable = False),
                    Column('Mail',String, nullable = False)
                    )
