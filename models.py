from app import db
from sqlalchemy.dialects.postgresql import JSON

##Notes - this program is utilziing postgresql as the db (see the config file)
##before launching, will need to ensure the postgresql db is open and running, with
##the appropriate user roles, permissions, etc...that matcht the config file appropiately 


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    # result_all = db.Column(db.String())
    # result_no_stop_words = db.Column(db.String())

    def __init__(self, url):
        self.url = url
        # self.result_all = result_all
        # self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)


##this below is a very simple task that will be placed into the 'task cue'
##still need to perform more research on how to prioritize, creating a dashboard 
##to look at the existing tasks, completed tasks, failed tasks, etc...


def boomer(x):
    resp = x
    result = Result(url=resp)
    db.session.add(result)
    db.session.commit()
    return result.id