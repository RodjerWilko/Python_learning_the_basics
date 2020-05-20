from pony.orm import Database, Required, Json

from settings import DB_CONFIG

db = Database()

db.bind(**DB_CONFIG)


class UserState(db.Entity):
    user_id = Required(str, unique=True)
    scenario_name = Required(str)
    step_name = Required(str)
    context = Required(Json)


class Registration(db.Entity):
    name = Required(str)
    email = Required(str)
    date_flight = Required(str)
    time_flight = Required(str)
    city_out = Required(str)
    city_in = Required(str)
    sits = Required(str)
    comment = Required(str)
    phone = Required(str)


db.generate_mapping(create_tables=True)
