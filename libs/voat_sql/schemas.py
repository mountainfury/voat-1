from voat_sql import *

# I'll have to look more into this, there may be a better way. 

class SubVoat(Base):
    __tablename__ = 'subvoat'
    
    id            = Column(Integer, primary_key=True)
    name          = Column(String(200), unique=True, nullable=False)
    owner_id      = Column(Integer)
    creation_date = Column(DateTime)
    creator_id    = relationship('User',      backref=backref('user',      lazy='noload'))
    threads       = relationship('Thread',    backref=backref('thread',    lazy='noload'))
    moderators    = relationship('Moderator', backref=backref('moderator', lazy='noload'))


class Thread(Base):
    __tablename__ = 'thread'
    
    uuid          = Column(String(200), primary_key=True)
    title         = Column(String(200))
    body          = Column(String(200))
    user_id       = Column(Integer)
    creation_date = Column(DateTime)
    subvoat_id    = Column(Integer, ForeignKey('subvoat.id'))
    votes         = Column(Integer, ForeignKey('user.id'))


class Comment(Base):
    __tablename__ = 'comment'

    uuid          = Column(String(200),  primary_key=True)
    body          = Column(String(5000))
    user_id       = Column(Integer)
    creation_date = Column(DateTime)
    thread_uuid   = Column(String, ForeignKey('thread.uuid'))
    reply_uuid    = Column(String(200))



class User(Base):
    __tablename__ = 'user'

    id            = Column(Integer, primary_key=True)
    creation_time = Column(DateTime)
    username      = Column(String(200), unique=True, nullable=False)
    email         = Column(String(200), unique=True)
    password_hash = Column(String(200))
    api_token     = Column(String(200))
    banned        = Column(Boolean)
    verified      = Column(Boolean, default=False)
    moderator     = relationship('Moderator', backref=backref('moderator', lazy='noload'))


class Moderator(Base):
    __tablename__ = 'moderator'
    id           = Column(Integer, primary_key=True)
    user_id      = Column(Integer, ForeignKey('user.id'))
    subvoat_id   = Column(Integer, ForeignKey('subvoat.id'))


class Servers(Base):
    __tablename__ = 'server'

    id         = Column(Integer, primary_key=True)
    address    = Column(String(200), unique=True)
    public_key = Column(String(200), unique=True)
