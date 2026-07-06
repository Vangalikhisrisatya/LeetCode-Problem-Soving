class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	i=0
    	pos=0
    	while i<len(arr):
    	    if arr[i]!=0:
    	        arr[pos]=arr[i]
    	        pos+=1
    	    i+=1
    	while pos<len(arr):
    	    arr[pos]=0
    	    pos+=1
    	return arr