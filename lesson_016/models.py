import peewee

dbp = peewee.Proxy()


class BaseModel(peewee.Model):
    class Meta:
        database = dbp


class UserTable(BaseModel):
    date = peewee.CharField()
    t_day = peewee.CharField()
    t_night = peewee.CharField()
    desc = peewee.CharField()
