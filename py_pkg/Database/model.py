from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Define DB model

Base = declarative_base()
class User_Default_Table(Base):
    __tablename__ = 'User_Default_Table'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(64), index=True)
    default_file_path = Column(String(500))
    default_id_column = Column(String(500))
    default_data_column = Column(String(500))
    default_target_column = Column(String(500))
    default_mode = Column(String(500))
    default_model_name = Column(String(500))


class User_Sponsor_Table(Base):
    __tablename__ = 'User_Sponsor_Table'
    id = Column(Integer, primary_key=True)
    task_name = Column(String(500))
    task_description = Column(String(500))
    user_id = Column(String(64), index=True)
    test_indicator = Column(String(500))
    task_id = Column(String(500))
    test_id = Column(String(500))
    train_file_path = Column(String(500))
    train_id_column = Column(String(500))
    train_data_column = Column(String(500))
    train_target_column = Column(String(500))
    test_file_path = Column(String(500))
    test_id_column = Column(String(500))
    test_data_column = Column(String(500))
    test_target_column = Column(String(500))
    task_mode = Column(String(500))
    model_name = Column(String(500))
    metric_name = Column(String(500))


class User_Assistor_Table(Base):
    __tablename__ = 'User_Assistor_Table'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(64), index=True)
    task_id = Column(String(500))
    test_id = Column(String(500))
    task_name = Column(String(500))
    task_description = Column(String(500))
    test_name = Column(String(500)) 
    test_description = Column(String(500))
    train_file_path = Column(String(500))
    train_id_column = Column(String(500))
    train_data_column = Column(String(500))
    train_target_column = Column(String(500))
    test_file_path = Column(String(500))
    test_id_column = Column(String(500))
    test_data_column = Column(String(500))
    test_target_column = Column(String(500))
    mode = Column(String(500)) 
    test_indicator = Column(String(500)) 
    model_name = Column(String(500)) 