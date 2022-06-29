import datetime

import pymysql
from data.config import host, port, user, password, db_name


def connect_to_db():
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=db_name
    )

    return connection

def insert_data(connection, fullname, user_id, telephone, username, label_give, label_recieve,
                amount_give, amount_recieve, exchange_rate, way_to_give, way_to_recieve,
                status, created_time):
    with connection.cursor() as cursor:
        insert_query = "INSERT INTO `orders` (fullname, user_id, telephone," \
                       " username, label_give, label_recieve, amount_give," \
                       " amount_recieve, exchange_rate," \
                       " way_to_give, way_to_recieve, status, created_time)" \
                       f" VALUES ('{fullname}', '{user_id}', '{telephone}'," \
                       f" '{username}', '{label_give}', '{label_recieve}', {amount_give}," \
                       f" {amount_recieve}, {exchange_rate}," \
                       f" '{way_to_give}', '{way_to_recieve}', '{status}', '{created_time}');"
        cursor.execute(insert_query)
        connection.commit()
        return cursor.lastrowid


def get_data(connection, user_id):
    with connection.cursor() as cursor:
        select_all_rows = f"SELECT labels, exchange_rate, amount_1, amount_2, " \
                          f"way_to_give, way_to_recieve, created_time FROM `orders`" \
                          f" WHERE user_id = {user_id}"

        cursor.execute(select_all_rows)
        # cursor.execute("SELECT * FROM `users`")
        rows = cursor.fetchall()

    return rows

def complete_order_bd(connection, id, status, operator_id):
    with connection.cursor() as cursor:
        select_responsible_id = f"SELECT responsible_id FROM `orders` where id = {id}"
        cursor.execute(select_responsible_id)
        # cursor.execute("SELECT * FROM `users`")
        responsible_id = cursor.fetchall()[0]
        if responsible_id == operator_id:
            completion_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            update_query = f"UPDATE `orders` SET status = '{status}'," \
                           f" completion_time = '{completion_time}'  WHERE id = {id};"
            cursor.execute(update_query)
            connection.commit()


def start_work(connection, id, user, status='В обработке'):
    with connection.cursor() as cursor:
        acceptance_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        update_query = f"UPDATE `orders`" \
                       f" SET status = '{status}', responsible_name = '{user.full_name}'," \
                       f" responsible_id = '{user.id}', acceptance_time = '{acceptance_time}'" \
                       f" WHERE id = {id};"
        cursor.execute(update_query)
        connection.commit()




if __name__=='__main__':
    connection = connect_to_db()
    with connection.cursor() as cursor:
        create_table_query = "CREATE TABLE `orders`(id int AUTO_INCREMENT," \
                              " fullname varchar(64)," \
                              " user_id varchar(20)," \
                              " telephone varchar(16)," \
                             " username varchar(64)," \
                             " label_give varchar(64)," \
                             " label_recieve varchar(64)," \
                             " amount_give float,"\
                             " amount_recieve float," \
                             " exchange_rate float," \
                             " way_to_give varchar(64)," \
                             " way_to_recieve varchar(64)," \
                             " status varchar(64)," \
                             " created_time datetime," \
                             " acceptance_time datetime," \
                             " completion_time datetime," \
                             " responsible_name varchar(64)," \
                             " responsible_id varchar(64)," \
                             " PRIMARY KEY (id));"
        cursor.execute(create_table_query)
    print("Table created successfully")