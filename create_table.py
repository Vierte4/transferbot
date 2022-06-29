if __name__=='__main__':
    from utils.manage_db import connect_to_db

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