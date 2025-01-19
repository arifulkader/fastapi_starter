
from database import Base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Boolean, Integer, String


class Staff(Base):
    __tablename__ = 'staffs'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(128), unique=True, index=True)
    email = Column(String(128),nullable=True)
    password = Column(String(128),)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return self.username
