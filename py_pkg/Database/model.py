from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Define DB model
Base = declarative_base()
class User_Default_Path(Base):
    __tablename__ = 'Default_Path'
    id = Column(Integer, primary_key=True)
    uder_id = Column(String(64), index=True, unique=True)
    default_train_file_path = Column(String(500))
    default_train_id_colomn = Column(String(500))
    default_train_data_colomn = Column(String(500))
    default_train_target_colomn = Column(String(500))
    default_train_data_path = Column(String(500))
    default_train_id_path = Column(String(500))
    default_test_data_path = Column(String(500))
    default_test_id_path = Column(String(500))



