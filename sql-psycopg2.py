import psycopg2

#connect to chinook database
connection = psycopg2.connect(database ="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the Artist table
cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the Name column from the Artist table
#cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only Queen from the Artist table
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ['Queen'])

# Query 4 - select only by ArtistId #51 from the Artist table
#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - selct only the albums with ArtistId #51 on the Album table
#cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

#Query 6 - select all tracks where composer is Queen
#cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ['Queen'])


#fetch multiple rows
results = cursor.fetchall()

#fetch single row
#results = cursor.fetchone()

#close the connection
connection.close()

#print results
for result in results:
    print(result)