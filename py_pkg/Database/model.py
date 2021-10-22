from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Define DB model
Base = declarative_base()
class User_Default_Path(Base):
    __tablename__ = 'User_Default_Path'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(64), index=True)
    default_train_file_path = Column(String(500))
    default_train_id_colomn = Column(String(500))
    default_train_data_colomn = Column(String(500))
    default_train_target_colomn = Column(String(500))
    default_train_data_path = Column(String(500))
    default_train_id_path = Column(String(500))
    default_test_data_path = Column(String(500))
    default_test_id_path = Column(String(500))

class User_Chosen_Path(Base):
    __tablename__ = 'User_Chosen_Path'
    id = Column(Integer, primary_key=True)
    task_name = Column(String(500))
    task_description = Column(String(500))
    user_id = Column(String(64), index=True)
    test_indicator = Column(String(500))
    task_id = Column(String(500))
    test_id = Column(String(500))
    train_file_path = Column(String(500))
    train_id_colomn = Column(String(500))
    train_data_colomn = Column(String(500))
    train_target_colomn = Column(String(500))
    test_file_path = Column(String(500))
    test_id_colomn = Column(String(500))
    test_data_colomn = Column(String(500))
    test_target_colomn = Column(String(500))

class User_Pending_Page(Base):
    __tablename__ = 'User_Pending_Page'
    id = Column(Integer, primary_key=True)
    task_name = Column(String(500))
    task_description = Column(String(500))
    user_id = Column(String(64), index=True)
    task_id = Column(String(500))
    test_id = Column(String(500))
    default_train_data_path = Column(String(500))
    default_train_id_path = Column(String(500))
    default_test_data_path = Column(String(500))
    default_test_id_path = Column(String(500))





