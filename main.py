import csv
from data.user import Users
from data import db_session

db_session.global_init("db/startup_data.db")
db_sess = db_session.create_session()


def csv_to_list(f_name):
    with open(f_name, mode='r') as f:
        reader = csv.reader(f, delimiter=',')
        return list(reader)


for el in csv_to_list("userdata-b66177fb-1f96-4dfd-9b28-15b118ef4551.csv")[1:]:
    user = Users()
    user.user_id, user.join_datetime, user.age, user.income, user.kids, user.teenagers, user.marital, user.education = el
    db_sess.add(user)
db_sess.commit()
db_sess.close()
