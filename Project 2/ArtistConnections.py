import random
from SongLibrary import *
from Graph import *


class ArtistConnections:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.graph = Graph()

    """
    Load the artist connections graph based on a given song database
    Add the edges based on the last column of the collaborative artists 

    """

    def load_graph(self, songLibrary):
        for n in range(songLibrary.size):  # for each song in array
            if songLibrary.songArray[n].artist in self.vertList: # if the artist is in the vertex list
                for m in range(len(songLibrary.songArray[n].coartist)): # for each coartist...
                    if songLibrary.songArray[n].coartist[m] not in self.vertList:
                        self.graph.addVertex(songLibrary.songArray[n].coartist[m])  # adds node for artist
                        self.numVertices += 1  # count for number of vertices increases by 1
                        self.vertList = self.graph.vertList
                    if songLibrary.songArray[n].artist not in self.graph.getVertex(songLibrary.songArray[n].coartist[m]).coArtists:
                        self.graph.getVertex(songLibrary.songArray[n].coartist[m]).addNeighbor(songLibrary.songArray[n].artist, 1)
                    if songLibrary.songArray[n].coartist[m] not in self.graph.getVertex(songLibrary.songArray[n].artist).coArtists:
                        self.graph.getVertex(songLibrary.songArray[n].artist).addNeighbor(songLibrary.songArray[n].coartist[m], 1) # adds neighbor, sets weight to 1
                    else:
                        self.graph.getVertex(songLibrary.songArray[n].artist).addNeighbor(songLibrary.songArray[n].coartist[m], self.graph.getVertex(songLibrary.songArray[n].artist).coArtists[songLibrary.songArray[n].coartist[m]]+1) # linking artist to coartist, adds one to weight
                        self.graph.getVertex(songLibrary.songArray[n].coartist[m]).addNeighbor(songLibrary.songArray[n].artist,self.graph.getVertex(songLibrary.songArray[n].coartist[m]).coArtists[songLibrary.songArray[n].artist] + 1)
            else:
                self.graph.addVertex(songLibrary.songArray[n].artist)  # adds node for artist
                for m in range(len(songLibrary.songArray[n].coartist)):
                    if songLibrary.songArray[n].coartist[m] not in self.vertList:
                        self.graph.addVertex(songLibrary.songArray[n].coartist[m])  # adds node for artist
                        self.numVertices += 1  # count for number of vertices increases by 1
                        self.vertList = self.graph.vertList
                    if songLibrary.songArray[n].coartist[m] not in self.graph.getVertex(songLibrary.songArray[n].artist).coArtists:
                        self.graph.getVertex(songLibrary.songArray[n].artist).addNeighbor(songLibrary.songArray[n].coartist[m], 1)  # linking artist to coartist, sets weight to 1
                    else:
                        self.graph.getVertex(songLibrary.songArray[n].artist).addNeighbor(songLibrary.songArray[n].coartist[m],self.graph.getVertex(songLibrary.songArray[n].artist).coArtists[songLibrary.songArray[n].coartist[m]] + 1)  # linking artist to coartist, adds on to weight
                    if songLibrary.songArray[n].artist not in self.graph.getVertex(songLibrary.songArray[n].coartist[m]).coArtists:
                        self.graph.getVertex(songLibrary.songArray[n].coartist[m]).addNeighbor(songLibrary.songArray[n].artist, 1)  # linking artist to coartist, sets weight to 1
                    else:
                        self.graph.getVertex(songLibrary.songArray[n].coartist[m]).addNeighbor(songLibrary.songArray[n].artist,self.graph.getVertex(songLibrary.songArray[n].coartist[m]).coArtists[songLibrary.songArray[n].artist] + 1)  # linking artist to coartist, adds on to weight
                self.numVertices += 1 # count for number of vertices increases by 1
                self.vertList = self.graph.vertList
            self.graph.getVertex(songLibrary.songArray[n].artist).songs.append(songLibrary.songArray[n].title) # adds song to vertex

        return self.numVertices

    """
    Return song libary information
    """

    def graph_info(self):
        return "Vertex Size: " + str(self.numVertices)

    """
    Search the information of an artist based on the artist name
    Return a tuple (the number of songs he/she wrote, the collaborative artist list)

    """

    def search_artist(self, artist_name):

        numSongs = len(self.graph.getVertex(artist_name).songs) # len of song list in vertex
        artistLst = list(self.graph.getVertex(artist_name).coArtists.keys()) # sets the artistLst

        return numSongs, artistLst

    """
    Return a list of two-hop neighbors of a given artist
    """

    def find_new_friends(self, artist_name):

        #self.graph.getVertex(songLibrary.songArray[n].artist).songs.append(songLibrary.songArray[n].title)
        hop1 = []
        hop2_copy = set() # allows for proper number of iterations
        hop2 = set() # removes duplicate elements

        for artist in self.graph.getVertex(artist_name).coArtists.keys():
            hop1.append(artist) # add artists to hop 1
        for artist in hop1:
            m = self.graph.getVertex(artist).coArtists.keys()
            for artist in m:
                hop2.add(artist) # add artists to hop 2
                hop2_copy.add(artist) # replicate hop 2
        for n in hop2_copy:
            if n in hop1:
                hop2.remove(n) # makes second hop collaborator list

        hop2.remove(artist_name) # removes inputted artist
        two_hop_friends = list(hop2) # changes set to list
        two_hop_friends.sort()

        return two_hop_friends

    """
    Search the information of an artist based on the artist name

    """

    def recommend_new_collaborator(self, artist_name):

        numSongs = 0
        count = 0
        options = artistGraph.find_new_friends(artist_name)

        for friend2 in options:
            for artist in self.graph.getVertex(artist_name).coArtists:
                if artist in self.graph.getVertex(friend2).coArtists:
                    count += self.graph.getVertex(friend2).coArtists[artist]
                    if count > numSongs:
                        numSongs = count
                        artist_name = artist
            count = 0
        return numSongs, artist_name

    """
    Search the information of an artist based on the artist name

    """

    def shortest_path(self, artist_name):

        path = {}

        #
        # Write your code here
        #
        return path


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    artistGraph = ArtistConnections()
    songLib = SongLibrary()
    songLib.loadLibrary("TenKsongs_proj2.csv")
    print(songLib.libraryInfo())
    artistGraph.load_graph(songLib)
    print(artistGraph.graph_info())
    #print(artistGraph.graph.getVertex("Dr. Elmo").coArtists)
    #print(songLib.songArray[0].toString()) # how to reference
    #print(artistGraph.search_artist("Santana"))
    #print(artistGraph.find_new_friends("Kaskaad"))
    print(artistGraph.recommend_new_collaborator("Santana"))
