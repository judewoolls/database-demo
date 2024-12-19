from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing instruction form the chinook database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class based model for the artist table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key = True)
    Name = Column(String)

# create a class based model for the album table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key = True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key= True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey('Album.AlbumId'))
    MediaTypeId = Column(Integer, primary_key = False)
    GenreId = Column(Integer, primary_key = False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key = False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)

# instead of connecting to the database directly we will ask for a session
# create a new instance of session maker, then point to our engine (the db)
Session = sessionmaker(db)
#open an actual session by calling the session subclass
session = Session()

# create a database subclass using the declarative base subclass
base.metadata.create_all(db)

# Query 1 - Select all records from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")


# Query 2 - select only the artist name from artist table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)


# Query 3 - select Queen from artist table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select only by ID 51 from artist table
# artist = session.query(Artist).filter_by(ArtistId="51").first()
# print(artist.ArtistId, artist.Name, sep=" | ")


# Query 5 - Select only the albums with ArtistId #51 on the album table
# albums = session.query(Album).filter_by(ArtistId = 51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Qeury 6 - Select using composer "Queen" to select tracks

tracks = session.query(Track).filter_by(Composer = "Queen")
for track in tracks:
    print(track.TrackId, track.Name, track.AlbumId, track.MediaTypeId, track.GenreId, track.Composer, track.Milliseconds, track.Bytes, track.UnitPrice, sep=" | ")
