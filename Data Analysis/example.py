from cassandra.cluster import Cluster

cassandra_cluster = Cluster()
cassandra_session = cassandra_cluster.connect()
cassandra_keyspace_name = 'nbatests22'
cassandra_session.set_keyspace(cassandra_keyspace_name),

query = "SELECT team_id, season, HOME_RECORD, ROAD_RECORD FROM Ranking WHERE games = 82 ALLOW FILTERING;"
prepared_query = cassandra_session.prepare(query)
results = cassandra_session.execute(prepared_query)
pass



cassandra_cluster.shutdown()



#creating keyspace - not working
# create_keyspace_query = f"CREATE KEYSPACE IF NOT EXISTS {cassandra_keyspace_name} WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': 3}}"
# Execute the query to create the keyspace
# a = session.execute(create_keyspace_query)

#creating table -  not working
# Define creation query
# create_query = 'CREATE TABLE students (student_id UUID PRIMARY KEY, name TEXT, email TEXT, enrollment_year INT);'
# students_table = cassandra_session.execute(create_query)