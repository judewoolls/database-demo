from sqlalchemy import (
    create_engine, Table, Column, Float, Integer, MetaData, String, ForeignKey
)

db = create_engine('postgresql:///chinook')

meta = MetaData(db)

#create variable for artist table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

#create variable for album table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

#create track table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer),
    Column("GenreId", Integer),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making a connection
with db.connect() as connection:
    # Query 1 - select all records from the Artist table
    #select_query = artist_table.select()

    # Query 2 - select only the Name column from the Artist table
    # select_query =  artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - select only Queen from the Artist table
    #select_query = artist_table.select().where(artist_table.c.Name == 'Queen')

    # Query 4 - select only by ArtistId #51 from the Artist table
    #select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - selct only the albums with ArtistId #51 on the Album table
    #select_query = album_table.select().where(album_table.c.ArtistId == 51)

    #Query 6 - Select all tracks where the composer is queen from the track table
    select_query = track_table.select().where(track_table.c.Composer == 'Queen')

    results = connection.execute(select_query)
    for result in results:
        print(result)