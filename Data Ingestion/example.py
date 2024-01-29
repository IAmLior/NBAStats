from cassandra.cluster import Cluster

# Connect to the Cassandra cluster
cassandra_cluster = Cluster()
cassandra_session = cassandra_cluster.connect()
cassandra_keyspace_name = 'nbatests'
cassandra_session.set_keyspace(cassandra_keyspace_name),

query = "SELECT * FROM Ranking"
prepared_query = cassandra_session.prepare(query)
results = cassandra_session.execute(prepared_query)
pass

# # Define your insert query
# insert_query = "INSERT INTO graetstudents (student_id, name, email, enrollment_year) VALUES (%s, %s, %s, %s)"

# # Data to insert
# data_to_insert = ('12345', 'lior abuhav', 'lala@lala.com', 2020)

# # Execute the prepared query with the data
# 

# # Close the connection
# cassandra_cluster.shutdown()



#creating keyspace - not working
# create_keyspace_query = f"CREATE KEYSPACE IF NOT EXISTS {cassandra_keyspace_name} WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': 3}}"
# Execute the query to create the keyspace
# a = session.execute(create_keyspace_query)

#creating table -  not working
# Define creation query
# create_query = 'CREATE TABLE students (student_id UUID PRIMARY KEY, name TEXT, email TEXT, enrollment_year INT);'
# students_table = cassandra_session.execute(create_query)