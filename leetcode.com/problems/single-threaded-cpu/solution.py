class Solution:
	def getOrder(self, tasks: List[List[int]]) -> List[int]:
		# adding original task index to the tasks
		for i in range(len(tasks)):
		   tasks[i].append(i)
		
		# sorting based on start, duration then index
		tasks.sort(key=lambda x:(x[0],x[1],x[2]))

		result  = [] 

		# to use with heapq as priority queue
		queue = []

		t = 1
		for task in tasks:

			# pick a task from the priority queue if there is any
			# while there is time in starting of the current task
			while t < task[0] and len(queue)>0:

				# picking the next prioritized task and adding to the result
				dur,i,start = heapq.heappop(queue)
				result.append(i)

				# taking time to the starting time of next task if it is behind
				if start > t:
					t = start

				# adding time taken by the current task
				t += dur


			# adding current task to the priority queue
			# prioritizing based on duration and then index
			# start time here is not important becuase it's already passed
			heapq.heappush(queue, (task[1],task[2],task[0]))

		# current tasks are completed,
		# checking if there are more tasks left in the queue
		while len(queue)>0:
				# picking the next prioritized task and adding to the result
				dur,i,start = heapq.heappop(queue)
				result.append(i)

		return result
