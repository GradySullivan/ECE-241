"""
UMass ECE 241 - Advanced Programming
Project #1     Fall 2019
SongLibrary.py - SongLibrary class
"""
import math
import random
import time

from Song import Song

# ---------- Classes (From Professor Zink's Lectures/Discussions) ---------- #

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False

    def delete(self,key):
      if self.size > 1:
         nodeToRemove = self._get(key,self.root)
         if nodeToRemove:
             self.remove(nodeToRemove)
             self.size = self.size-1
         else:
             raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
      else:
         raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)

    def spliceOut(self):
       if self.isLeaf():
           if self.isLeftChild():
                  self.parent.leftChild = None
           else:
                  self.parent.rightChild = None
       elif self.hasAnyChildren():
           if self.hasLeftChild():
                  if self.isLeftChild():
                     self.parent.leftChild = self.leftChild
                  else:
                     self.parent.rightChild = self.leftChild
                  self.leftChild.parent = self.parent
           else:
                  if self.isLeftChild():
                     self.parent.leftChild = self.rightChild
                  else:
                     self.parent.rightChild = self.rightChild
                  self.rightChild.parent = self.parent

    def findSuccessor(self):
      succ = None
      if self.hasRightChild():
          succ = self.rightChild.findMin()
      else:
          if self.parent:
                 if self.isLeftChild():
                     succ = self.parent
                 else:
                     self.parent.rightChild = None
                     succ = self.parent.findSuccessor()
                     self.parent.rightChild = self
      return succ

    def findMin(self):
      current = self
      while current.hasLeftChild():
          current = current.leftChild
      return current

    def remove(self,currentNode):
         if currentNode.isLeaf(): #leaf
           if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
           else:
               currentNode.parent.rightChild = None
         elif currentNode.hasBothChildren(): #interior
           succ = currentNode.findSuccessor()
           succ.spliceOut()
           currentNode.key = succ.key
           currentNode.payload = succ.payload

         else: # this node has one child
           if currentNode.hasLeftChild():
             if currentNode.isLeftChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.leftChild
             elif currentNode.isRightChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.leftChild
             else:
                 currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
           else:
             if currentNode.isLeftChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.rightChild
             elif currentNode.isRightChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.rightChild
             else:
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)

class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None,balanceFactor=0):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = balanceFactor # added balanceFactor attribute (not in original)

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class AvlTree(BinarySearchTree):
    '''An extension t the BinarySearchTree data structure which
    strives to keep itself balanced '''

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self,node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self,rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(
            newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(
            rotRoot.balanceFactor, 0)

    def rotateRight(self,rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(
            newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(
            rotRoot.balanceFactor, 0)

    def rebalance(self,node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

# ---------- Project 1 Code ----------#

class SongLibrary:
    """
    Intialize your Song library here.
    You can initialize an empty songArray, empty BST and
    other attributes such as size and whether the array is sorted or not
    """

    def __init__(self):
        self.songArray = list() # to store song attributes
        self.songBST = None
        self.isSorted = False
        self.size = 0

    """
    load your Song library from a given file. 
    It takes an inputFilename and store the songs in songArray
    """

    def loadLibrary(self, inputFilename):
        song_file = open(inputFilename, "r")  # open file to read
        for i in song_file:
            song = Song(i) # creates objects
            self.size += 1  # adds 1 to size per iteration
            self.songArray.append(song)  # appends data for every song to a new index in the array

        """
        Linear search function.
        It takes a query string and attibute name (can be 'title' or 'artist')
        and return the number of songs fonud in the library.
        Return -1 if no songs is found.
        Note that, Each song name is unique in the database,
        but each artist can have several songs.
        """

    def linearSearch(self, query, attribute):
        found = 0  # set to -1 since it has not been found yet
        if attribute == "title":  # title search
            for item in self.songArray: # loops for each element
                if item.title == query:  # if the title is found
                    found += 1 # adds one per title found (max of 1 for this project, but created to be more robust)
        else: # artist search
            for item in self.songArray:
                if item.artist == query: # if artist is found
                    found += 1  # adds every song by that artist to array
        if found == 0: # returns -1 if no results found
            return -1
        return found

        """
        Build a BST from your Song library based on the song title. 
        Store the BST in songBST variable
        """

    def buildBST(self):
        self.songBST = AvlTree()  # creates object
        for item in self.songArray:
            self.songBST.put(item.title, item)  # places song in BST

    """
    Implement a search function for a query song (title) in the songBST.
    Return the song information string
    (After you find the song object, call the toString function)
    or None if no such song is found.
    """

    def searchBST(self, query):
        song = self.songBST.get(query)  # searches for query##
        if song: # if we found a song, return it's toString()
            return song.toString()
        return None # return none if it doesn't find any

    """
    Return song library information
    """

    def libraryInfo(self):
        return "Size: " + str(self.size) + ";  isSorted: " + str(self.isSorted) # returns info on song library

    """
    Sort the songArray using QuickSort algorithm based on the song title.
    The sorted array should be stored in the same songArray.
    Remember to change the isSorted variable after sorted
    """

    def quickSort(self):
        self.quickSortHelper(self.songArray, 0, len(self.songArray) - 1)  # quick sorts for entire list
        self.isSorted = True  # changes boolean once sorted

    def quickSortHelper(self, alist, first, last):
        if first < last:
            pointer = self.partition(alist, first, last)  # split point created
            self.quickSortHelper(alist, first, pointer - 1)  # recursively splits first half
            self.quickSortHelper(alist, pointer + 1, last) # recursively splits second half

    def partition(self, alist, first, last):
        pivot = alist[first]  # takes object in first list index
        rightmark = last  # at end of list
        leftmark = first + 1  # next to pivot

        done = False # causes while loop to occur
        while done == False:
            leftmarkObj = alist[leftmark]  # object at leftmark
            rightmarkObj = alist[rightmark]  # object at rightmark
            while leftmarkObj.title <= pivot.title and leftmark <= rightmark: # compares left and right title
                leftmark += 1  # moves left index up one
                if leftmark > len(alist) - 1: # ends if leftmark bypasses end of list
                    break
                leftmarkObj = alist[leftmark] # updates object
            while rightmarkObj.title >= pivot.title and rightmark >= leftmark:
                rightmark -= 1  # moves rightmark over
                rightmarkObj = alist[rightmark]
            if rightmark < leftmark:  # partitioning will be done at this point if condition is met
                done = True # ends while loop
            else:
                alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark] # swaps left and right mark

        alist[first], alist[rightmark] = alist[rightmark], alist[first] # sets up new "first" index for later partitioning
        return rightmark

# ---------- Test Sorting ---------- #

# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    songLib = SongLibrary() # these first two lines initially given
    songLib.loadLibrary("TenKsongs.csv")

    n = 100  # how many songs to randomly search for
    songLib.quickSort() # test quickSort
    start = time.time()
    songLib.buildBST()  # building BST and recording time
    end = time.time()
    timebuildBST = end - start  # calculating BST build time
    print("BST Build Time (seconds): " + str(timebuildBST))

    counter = 0 # counts each iteration in while loop
    linearTime_total = 0 # total time variable (linear sort)
    BSTTime_total = 0  # total time variable (BST sort)

    while counter < n:
        index = random.randint(0, songLib.size - 1)  # random number for index chosen
        item = songLib.songArray[index]  # object in that index examined

        # for Linear Search
        startL = time.time()
        songLib.linearSearch(item.title, "title")  # linear searching song with title the same as index object generated prior
        endL = time.time()
        time_linear = endL - startL  # calculating time for the search
        linearTime_total += time_linear  # adding calculated time to the total time

        # for BST search
        startB = time.time()
        songLib.searchBST(item.title)  # linear searching each song and timing the search
        endB = time.time()
        BSTTime = endB - startB  # calculating time for the search
        BSTTime_total += BSTTime  # adding calculated time to the total time

        counter += 1 # makes while loop iterate n times

    avglinear = linearTime_total / n  # average linear search time
    print("Average linear search time (seconds): " + str(avglinear))

    avgBST = BSTTime_total / n # average BST search time
    print("Average BST search time (seconds): " + str(avgBST))

    # number of searches until BST is more efficient
    print("Number of searches until building BST and BST search is quicker: " + str(math.ceil(timebuildBST / (avglinear - avgBST))))