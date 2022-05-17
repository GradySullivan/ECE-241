"""
UMass ECE 241 - Advanced Programming
Project #1     Fall 2019
SongLibrary.py - SongLibrary class
"""

from Song import Song
import random
import time


class SongLibrary:
    """
    Intialize your Song library here.
    You can initialize an empty songArray, empty BST and
    other attributes such as size and whether the array is sorted or not
    """

    def __init__(self):
        self.songArray = list()
        self.songBST = None
        self.isSorted = False
        self.size = 0

    """
    load your Song library from a given file. 
    It takes an inputFilename and store the songs in songArray
    """

    def loadLibrary(self, inputFilename):
        i = 0 # initialize i counter
        song_file = open(inputFilename, "r") # open file to read
        with open(inputFilename) as file:
            self.songArray = file.readlines() # puts lines into array
            for i in self.songArray: # calculates size
                self.size += 1 # adds 1 to size per iteration
        song_file.close()

    """
    Linear search function.
    It takes a query string and attibute name (can be 'title' or 'artist')
    and return the number of songs fonud in the library.
    Return -1 if no songs is found.
    Note that, Each song name is unique in the database,
    but each artist can have several songs.
    """

    def linearSearch(self, query, attribute):
        found = -1 # set to -1 since it has not been found yet
        result = [] # array for results
        if attribute == "title": # title search
            for i in self.songArray: # loops for each element
                song = Song(i) # creates Song object
                if song.title == query: #if the title is foud
                    found = 1
                    result.append(song.title)  #adds title to results list
        else: # artist search
            for i in self.songArray: # loops for each element
                song = Song(i) # creates Song object
                if song.artist == query: # if the artist is found
                    found = 1
                    result.append(song.title)  #adds title to results list
        if found == -1: # if matching query NOT found
            return found

    """
    Build a BST from your Song library based on the song title. 
    Store the BST in songBST variable
    """

    def buildBST(self):
        return
    #
    # Write your code here
    #

    """
    Implement a search function for a query song (title) in the songBST.
    Return the song information string
    (After you find the song object, call the toString function)
    or None if no such song is found.
    """

    def searchBST(self, query):
        self.searchBSThelper(self.songArray, 0, len(self.songArray) - 1)

    def searchBSThelper(self, alist, min, max):
        if min > max:
            return -1
        mid = int((min + max)/2)


    """
    Return song libary information
    """

    def libraryInfo(self):
        return "Size: " + str(self.size) + ";  isSorted: " + str(self.isSorted)

    """
    Sort the songArray using QuickSort algorithm based on the song title.
    The sorted array should be stored in the same songArray.
    Remember to change the isSorted variable after sorted
    """

    def quickSort(self):
        self.quickSortHelper(self.songArray, 0, len(self.songArray) - 1)
        self.isSorted = True

    def quickSortHelper(self, alist, first, last):
        if first < last:
            splitpoint = self.partition(alist, first, last)
            self.quickSortHelper(alist, first, splitpoint - 1)
            self.quickSortHelper(alist, splitpoint + 1, last)

    def partition(self, alist, first, last):
        pivotvalue = alist[first]
        pivotObj = Song(pivotvalue)  # makes Song object from line
        leftmark = first + 1  # mark next to pivot
        rightmark = last  # at end of list
        done = False  # to cause while loop to occur
        while done != True:
            leftmarkString = alist[leftmark] # string from the "leftmark" index of the read file
            rightmarkString = alist[rightmark] # string from the "rightmark" index of the read file
            leftmarkObj = Song(leftmarkString) # creates object from the leftmarkString
            rightmarkObj = Song(rightmarkString) # creates object from the rightmarkString
            while leftmark <= rightmark and leftmarkObj.title <= pivotObj.title: # compares left title to right title
                leftmark += 1 # moves the left counter up one
                if leftmark > len(alist) - 1: # ends if leftmark bypasses end of list
                    break
                leftmarkString = alist[leftmark] # updates leftmarkString
                leftmarkObj = Song(leftmarkString) #updates leftmarkObj
            while rightmarkObj.title >= pivotObj.title and rightmark >= leftmark:
                rightmark -= 1 # moves rightmark over
                rightmarkString = alist[rightmark] # updates rightmarkString
                rightmarkObj = Song(rightmarkString) # updates rightmarkObj
            if rightmark < leftmark: # checks whether to stop partition
                done = True
            else: #swaps left and right values
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp
        temp = alist[first] # switches first and current markers
        alist[first] = alist[rightmark]
        alist[rightmark] = temp

        return rightmark

#
# Write your code here
#

# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    songLib = SongLibrary()
    songLib.loadLibrary("TenKsongs.csv")
    print(songLib.libraryInfo())

    print(songLib.linearSearch("q","artist"))

    print(songLib.quickSort())
    for item in songLib.songArray:
        song = Song(item)
        print(song.title)


