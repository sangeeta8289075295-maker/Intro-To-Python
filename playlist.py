class Playlist:

    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"Playlist '{self.name}' of genre '{self.genre}' is ready.")

    def add_song(self, song):
        self.songs.append(song)
        print(f"'{song}' added to playlist '{self.name}'.")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}' removed from playlist '{self.name}'.")
        else:
            print(f"'{song}' not found in playlist '{self.name}'.")

    def display(self):
        print(f"Songs in playlist '{self.name}':")
        if self.songs:
            for i, song in enumerate(self.songs, 1):
                print(f" {i}. {song}")
        else:
            print(" No songs in the playlist.")

    def __del__(self):
        print(f"Playlist '{self.name}' is deleted. Goodbye!")


# Driver code
my_playlist = Playlist("Road Trip Vibes", "Pop")

while True:
    print("\n1. Add song  2. Remove song  3. View playlist  4. Delete and quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        song = input("Enter the song name to add: ")
        my_playlist.add_song(song)
    elif choice == '2':
        song = input("Enter the song name to remove: ")
        my_playlist.remove_song(song)
    elif choice == '3':
        my_playlist.display()
    elif choice == '4':
        del my_playlist
        break
    else:
        print("Invalid choice. Enter 1, 2, 3 or 4.")
