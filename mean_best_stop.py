import random
cardinality=10000
percentile_limit=2000
best_stop_list=[]
no_of_simulations=1000
for simulations in range(no_of_simulations):
	hotness_list=[]
	for i in range(cardinality):
		hotness_list.append(random.randint(0,cardinality))
	#print(hotness_list)
	best_stop_score=0
	best_stop=0
	score=[]
	for ii in range(100):
		hottest=0
		superliked=0
		swipe_limit=0
		score.append(0)
		for i in range(ii):
			if(hotness_list[i]>percentile_limit):
				if hottest<=hotness_list[i]:
					hottest=hotness_list[i]
				score[ii]+=hotness_list[i]
				swipe_limit+=1	
		for i in range(ii,cardinality):
			if(hotness_list[i]>percentile_limit):
				if swipe_limit<100:
						if hotness_list[i]>hottest and superliked==0:
							score[ii]+=hotness_list[i]*3
							superliked=1
						else:
							score[ii]+=hotness_list[i]
						swipe_limit+=1
	for i in range(1,100):
		if best_stop_score<score[i]:
			best_stop_score=score[i]
			best_stop=i+1
	best_stop_list.append(best_stop)
print(best_stop_list)
mean_best_stop=0
for i in range(no_of_simulations):
	mean_best_stop+=best_stop_list[i]
mean_best_stop/=no_of_simulations
print(mean_best_stop)
