import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones] # Converts all elements into their negative values
        heapq.heapify(maxHeap) # Turn array into a heap

        while maxHeap: # Iterate over the array
            y = heapq.heappop(maxHeap) # Get largest element
            if not maxHeap: # If last element, then return it
                return -y
            x = heapq.heappop(maxHeap) # Get second largest element
            if x != y: # Add stone with updated weight
                heapq.heappush(maxHeap, y - x) # O(log(n))
        return 0 
    
"""
    Knew it was a heap question because of the "2 max elements" and also
    the question required re-adding elements into the list. Thus we not 
    only wanted to order the elements but also maintain the ordering 
    as elements were inserted.
"""