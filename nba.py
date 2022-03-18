import operator
import requests

def pair_nba_players(json=[], heigh_sum=0):
	if type(json) is not list:
		print('No valid list of objects')
		return

	try:
		json.sort(key=operator.itemgetter("h_in"))
	except:
		print('Problem sorting json object')
		return

	leftIdx, rightIdx = 0,len(json)-1
	match = None	# used to know at which index there is a match, to return to this index when leftIdx increase in case it's another match.
	are_results = False
	while leftIdx < rightIdx:
		try:
			left,right = json[leftIdx],json[rightIdx]
			add = int(left.get('h_in',0))+int(right.get('h_in',0))
			if add == heigh_sum:
				print("- " +left.get('first_name','')+" "+left.get('last_name','')+ "		"+ right.get('first_name','')+" "+right.get('last_name',''))
				if match is None: # store the match for the next iteration
					match = rightIdx
				rightIdx -= 1
				are_results = True
			elif add < heigh_sum:
				leftIdx += 1
				if match is not None: #is there a match use it for this iteration
					rightIdx = match
					match = None
			elif add > heigh_sum:
				rightIdx -= 1
		except:
			print('an error occurred')
			rightIdx -= 1

	print("No matches found") if not are_results else ''

if __name__ == "__main__":
	heigh_sum = ''
	response = requests.get("https://mach-eight.uc.r.appspot.com/")

	if response.status_code == 200:
		json = response.json()['values']
		while heigh_sum == '':
			try:
				heigh_sum = int(input('Type the input height in inches: '))
			except:
				print('Not an integer typed, try again')

		pair_nba_players(json, heigh_sum)
	else:
		print('Error getting the json from source')