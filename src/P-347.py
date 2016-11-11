import heapq

class Solution(object):
	def topKFrequent(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		d = {}
		h = []
		ret = []

		for n in nums:
			if n not in d:
				d[n] = 1
			else:
				d[n] += 1
		
		for key,val in d.iteritems():
			heapq.heappush(h, (-val, key))

		for i in range(k):
			val, key = heapq.heappop(h)
			ret.append(key)

		return ret