class Song: 
    all = 0
    genres = []
    artists = []
    genre_count = {}    
    artist_count = {}

    def __init__(self,name,artist,genre) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)
        self.add_to_genre_count(self.genre)
        self.add_to_artist_count(self.artist)
    @classmethod
    def add_song_to_count(cls):
        cls.all += 1
    @classmethod
    def add_to_genres(cls,genre):
        cls.genres.append(genre) if genre not in cls.genres else False
    @classmethod
    def add_to_artists(cls,artist):
        cls.artists.append(artist) if artist not in cls.artists else False
    def add_to_genre_count(cls,genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    def add_to_artist_count(cls,artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1