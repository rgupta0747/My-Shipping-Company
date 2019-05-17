import math

cities = [['INUVIK', 'YELLOWKNIFE'], ['WHITEHORSE'], ['VICTORIA', 'VANCOUVER', 'ABBOTSFORD', 'WHISTLER', 'PRINCE GEORGE', 'KAMLOOPS', 'KELOWNA', 'PENTICTON', 'CRANBROOK'], ['GRANDE PRAIRIE', 'FORT MCMURRAY','EDMONTON',  'RED DEER', 'CALGARY', 'MEDICINE HAT', 'LETHBRIDGE', 'LLOYDMINSTER'], ['SWIFT CURRENT', 'SASKATOON', 'PRINCE ALBERT', 'REGINA'], ['BRANDON', 'WINNIPEG', 'THOMPSON'], ['KENORA', 'DRYDEN', 'THUNDER BAY', 'SAULT STE. MARIE', 'WINDSOR', 'SARNIA', 'CHATHAM-KENT', 'LONDON', 'KITCHNER', 'BRANTFORD', 'HAMILTON', 'OWEN SOUND', 'BARRIE','SUDBURY', 'TIMMINS', 'NORTH BAY', 'BRAMPTON', 'MISSISSAUGA', 'TORONTO', 'NIAGARA FALLS', 'OSHAWA', 'PETERBOROUGH', 'BELLEVILLE', 'KINGSTON', 'OTTAWA', 'CORNWALL'], ['GATINEAU', "VAL-D'OR", 'MONTREAL', 'SHERBROOKE', 'TROIS-RIVIERES', 'QUEBEC CITY', 'SAGUENAY', 'SEPT-ILES', 'RIMOUSKI'], ['FREDERICTON', 'SAINT JOHN', 'MONCTON'], ['STEPHENVILLE', 'DEER LAKE', 'GANDER', "SAINT JOHN'S"], ['CHARLOTTETOWN'], ['SYDNEY', 'HALIFAX'], ['IQALUIT']]
origin = input('Please enter the origin city: ').upper()			#asks user for the origin cityf
for i in range(len(cities)):	
	for j in range(len(cities[i])):
		if origin == cities[i][j]:
			origin_city = cities[i][j]				#checks list of cities and assigns it a location
			province_origin = i
			city_origin = j
		else:
			continue
destination = input('Please enter the destination: ').upper()			#asks user for destination city
for i in range(len(cities)):
	for j in range(len(cities[i])):
		if destination == cities[i][j]:
			destination_city = cities[i][j]				#checks list and assings city a location
			province_destination = i
			city_destination = j
		else:
			continue
expedited = input('Do you want expedited service (y/n): ').lower()		#asks user if they want expedited shipping
if expedited[0] == 'y':
	expedited = True 
else:
	expedited = False
weight = float(input('What is the weight of the item you are sending (in oz): '))	#asks user for the weight of the package
weight /= 16										#converts package to lbs
package_location = origin_city								#Sets the package location to it's origin
print('This is the route your package will go:')	
print()
print('ORIGIN:', package_location)
print('DESTINATION:', destination_city)
print()
#checks where the package starts and ends and charges a fee based on how far it travels
#If the package starts in a city with a main hub, fee is less
if origin_city == 'VANCOUVER' or origin_city == 'CALGARY' or origin_city == 'REGINA' or origin_city == 'WINNIPEG' or origin_city == 'MISSISSAUGA' or origin_city == 'OTTAWA' or origin_city == 'MONTREAL' or origin_city == 'QUEBEC CITY' or origin_city == 'MONCTON' or origin_city == "SAINT JOHN'S":
	surcharge_fee = 0
elif abs(province_origin - province_destination) == 0:					
	surcharge_fee = 0
elif abs(province_origin - province_destination) > 0 and abs(province_origin - province_destination) <= 3:
	surcharge_fee = 0.10
elif abs(province_origin - province_destination) > 10:
	surcharge_fee = .35
elif abs(province_origin - province_destination) > 7 and abs(province_origin - province_destination) <= 10:
	surcharge_fee = .225
elif abs(province_origin - province_destination) > 3 and abs(province_origin - province_destination) <= 7:
	surcharge_fee = .15

#checks if the package is coming from or going to Quebec, Northwest Territory, or Nunavut and charges an extra fee
if province_origin == 7 or province_destination == 7:
	quebec_surcharge = 15
elif province_origin == 7 and province_destination == 7:
	quebec_surcharge = 30
else:
	quebec_surcharge = 0
if province_origin == 0 and province_destination == 0:
	long_distance_surcharge_fee = 0
elif (province_origin == 0 and province_destination == 12) or (province_origin == 12 and province_destination == 0):
	long_distance_surcharge_fee = 60
elif province_origin == 0 or province_origin == 12 or province_destination == 0 or province_destination == 12:
	long_distance_surcharge_fee = 30
else:
	long_distance_surcharge_fee = 0

main_hubs = [['YELLOWKNIFE'], ['WHITEHORSE'], ['VANCOUVER'], ['CALGARY'], ['REGINA'], ['WINNIPEG'], ['MISSISSAUGA', 'OTTAWA'], ['MONTREAL', 'QUEBEC CITY'], ["SAINT JOHN'S"], ['MONCTON'], ['CHARLOTTETOWN']]
regional_hubs = [['KELOWNA'], ['EDMONTON'], ['SASKATOON'], ['THUNDER BAY', 'LONDON', 'SUDBURY', 'HAMILTON'], ['DEER LAKE'], ['SYDNEY', 'HALIFAX']]

#checks to see if the origin city is in the main hub or regional hub
for i in range(len(regional_hubs)):						 
	for j in range(len(regional_hubs[i])):
		if origin_city == regional_hubs[i][j]:
			point_of_origin = origin_city
		else:	
			continue
for i in range(len(main_hubs)):
	for j in range(len(main_hubs[i])):
		if origin_city == main_hubs[i][j]:
			point_of_origin = origin_city
		else:
			continue
#if origin city is not a hub, then it sends the package location to the nearest regional or main hub
if origin_city == 'INUVIK':
	point_of_origin = main_hubs[0][0]
elif origin_city == 'VICTORIA' or origin_city == 'PRINCE GEORGE' or origin_city == 'WHISTLER' or origin_city == 'ABBOTSFORD':
	point_of_origin = main_hubs[2][0]
elif origin_city == 'CRANBROOK' or origin_city == 'KAMLOOPS' or origin_city == 'PENTICTON':
	point_of_origin = regional_hubs[0][0]
elif origin_city == 'GRANDE PRAIRIE' or origin_city == 'FORT MCMURRAY' or origin_city == 'LLOYDMINSTER':
	point_of_origin = regional_hubs[1][0]
elif origin_city == 'MEDICINE HAT' or origin_city == 'LETHBRIDGE':
	point_of_origin = main_hubs[3][0]
elif origin_city == 'SWIFT CURRENT':
	point_of_origin = main_hubs[4][0]
elif origin_city == 'PRINCE ALBERT':
	point_of_origin = regional_hubs[2][0]
elif origin_city == 'BRANDON' or origin_city == 'THOMPSON' or origin_city == 'KENORA' or origin_city == 'DRYDEN':
	point_of_origin = main_hubs[5][0]
elif origin_city == 'SAULT STE. MARIE' or origin_city == 'NORTH BAY' or origin_city == 'TIMMINS':
	point_of_origin = regional_hubs[3][2]
elif origin_city == 'WINDSOR' or origin_city == 'SARNIA' or origin_city == 'CHATHAM-KENT':
	point_of_origin = regional_hubs[3][1]
elif origin_city == 'NIAGARA FALLS' or origin_city == 'KITCHNER' or origin_city == 'BRANTFORD':
	point_of_origin = regional_hubs[3][3]
elif origin_city == 'BRAMPTON' or origin_city == 'TORONTO' or origin_city == 'PETERBOROUGH' or origin_city == 'OSHAWA' or origin_city == 'BARRIE' or origin_city == 'OWEN SOUND': 
	point_of_origin = main_hubs[6][0]
elif origin_city == 'KINGSTON' or origin_city == 'BELLEVILLE' or origin_city == 'GATINEAU' or origin_city == "VAL-D'OR" or origin_city == 'CORNWALL':
	point_of_origin = main_hubs[6][1]
elif origin_city == 'SHERBROOKE' or origin_city == 'TROIS-RIVIERES' or origin_city == 'IQALUIT':
	point_of_origin = main_hubs[7][0]
elif origin_city == 'SEPT-ILES' or origin_city == 'SAGUENAY' or origin_city == 'RIMOUSKI':
	point_of_origin = main_hubs[7][1]
elif origin_city == 'GANDER':
	point_of_origin = main_hubs[8][0]
elif origin_city == 'STEPHENVILLE':
	point_of_origin = regional_hubs[4][0]
elif origin_city == 'FREDERICTON' or origin_city == 'SAINT JOHN':
	point_of_origin = main_hubs[9][0]
number_of_moves = 1									#counts the number of moves
package_location = point_of_origin							#changes location of package to a hub
print('Your Package was picked up and is on the way to:', point_of_origin)

#calculates the direction the package is moving
if province_origin - province_destination < 0:
	direction = 'east'
elif province_origin - province_destination > 0:
	direction = 'west'
else:
	direction = 'same province'

#This body moves the package from hub to hub until it arrives at it arrives at a hub connected to the destination 
#If expedited is on, then it will jump around according to it's destination  
package_arrived = False
while not package_arrived:
	if package_location == 'CALGARY' or package_location == 'EDMONTON':
		if package_location == 'EDMONTON':
			if destination_city == 'GRANDE PRAIRIE' or destination_city == 'FORT MCMURRAY' or destination_city == 'RED DEER' or destination_city == 'EDMONTON' or destination_city == 'LLOYDMINSTER':
				package_location = destination_city
				package_arrived = True
			else:
				package_location = main_hubs[3][0]	
				number_of_moves += 1				
				print('Your Package is in:', package_location)
		if package_location == 'CALGARY':
			if destination_city == 'LETHBRIDGE' or destination_city == 'MEDICINE HAT' or destination_city == 'RED DEER' or destination_city == 'CALGARY':
				package_location = destination_city
				package_arrived = True
			elif destination_city == 'GRANDE PRAIRIE' or destination_city == 'FORT MCMURRAY' or destination_city == 'EDMONTON' or destination_city == 'LLOYDMINSTER':
				number_of_moves += 1
				package_location = regional_hubs[1][0]
				print('Your Package is in:', package_location)
			elif destination_city == 'YELLOWKNIFE' or destination_city == 'INUVIK':
				package_location = main_hubs[0][0] 
				number_of_moves += 1
				print('Your Package is in:', package_location)
			elif destination_city == 'WHITEHORSE':
				package_location = main_hubs[1][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
			elif expedited:
				if destination_city == 'HALIFAX' or destination_city == 'MONCTON' or destination_city == 'FREDERICTON' or destination_city == 'SAINT JOHN' or destination_city == 'SYDNEY' or destination_city == 'GANDER' or destination_city == 'DEER LAKE' or destination_city == "SAINT JOHN's" or destination_city == 'CHARLOTTETOWN' or destination_city == 'STEPHENVILLE':
					package_location = main_hubs[9][0]
					number_of_moves += 1
					print('Your Package is in:', package_location)
				elif destination_city == 'VANCOUVER' or destination_city == 'PRINCE GEORGE' or destination_city == 'KELOWNA' or destination_city == 'CRANBROOK' or destination_city == 'KAMLOOPS' or destination_city == 'VICTORIA' or destination_city == 'PENTICTON' or destination_city == 'WHISTLER' or destination_city == 'ABBOTSFORD':
					package_location = main_hubs[2][0]
					number_of_moves += 1
					print('Your Package is in:', package_location)
				elif destination_city == 'YELLOWKNIFE' or destination_city == 'INUVIK':
					package_location = main_hubs[0][0]
					number_of_moves += 1
					print('Your Package is in:', package_location)
				elif destination_city == 'WHITEHORSE':
					package_location = main_hubs[1][0]
					number_of_moves += 1
					print('Your Package is in:', package_location)
				elif destination_city == 'WINNIPEG' or destination_city == 'THOMPSON' or destination_city == 'BRANDON' or destination_city == 'THUNDER BAY' or destination_city == 'KENORA' or destination_city == 'DRYDEN':
					package_location = main_hubs[5][0]
					number_of_moves += 1
					print('Your Package is in:', package_location)
				elif destination_city == 'SASKATOON' or destination_city == 'REGINA' or destination_city == 'PRINCE ALBERT' or destination_city == 'SWIFT CURRENT':
					package_location = main_hubs[4][0]
					number_of_moves += 1
					print('Your Package is in:', package_location)
				else:
					package_location = main_hubs[6][0]
					number_of_moves += 1
					print('Your Package is in:', package_location)
			elif destination_city == 'VANCOUVER' or destination_city == 'PRINCE GEORGE' or destination_city == 'KELOWNA' or destination_city == 'VICTORIA' or destination_city == 'CRANBROOK' or destination_city == 'WHISTLER' or destination_city == 'KAMLOOPS' or destination_city == 'PENTICTON' or destination_city == 'ABBOTSFORD':
				package_location = main_hubs[2][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
			elif direction == 'east':
				package_location = main_hubs[4][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
			elif direction == 'west':
				package_location = main_hubs[2][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
	if package_location == 'KELOWNA' or package_location == 'VANCOUVER':
		if package_location == 'VANCOUVER': 
			if destination_city == 'PRINCE GEORGE' or destination_city == 'VICTORIA' or destination_city == 'VANCOUVER' or destination_city == 'WHISTLER' or destination_city == 'ABBOTSFORD':
				package_location = destination_city
				package_arrived = True
			elif destination_city == 'KELOWNA' or destination_city == 'CRANBROOK' or destination_city == 'KAMLOOPS' or destination_city == 'PENTICTON':
				number_of_moves += 1	
				package_location = regional_hubs[0][0]
				print('Your Package is in:', package_location)
			elif expedited:
				if destination_city == 'HALIFAX' or destination_city == 'MONCTON' or destination_city == 'FREDERICTON' or destination_city == 'SAINT JOHN' or destination_city == 'SYDNEY' or destination_city == 'GANDER' or destination_city == 'DEER LAKE' or destination_city == "SAINT JOHN's" or destination_city == 'CHARLOTTETOWN' or destination_city == 'STEPHENVILLE':
					package_location = main_hubs[9][0]
					number_of_moves += 1	
					print('Your Package is in:', package_location)
				if destination_city == 'WINNIPEG' or destination_city == 'BRANDON' or destination_city == 'THOMPSON' or destination_city == 'KENORA' or destination_city == 'DRYDEN':
					package_location = main_hubs[5][0]
					number_of_moves += 1	
					print('Your Package is in:', package_location)
				else:
					package_location = main_hubs[6][0]
					number_of_moves += 1	
					print('Your Package is in:', package_location)
			else: 
				package_location = main_hubs[3][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
		if package_location == 'KELOWNA':
			if destination_city == 'CRANBROOK' or destination_city == 'KELOWNA' or destination_city == 'KAMLOOPS' or destination_city == 'PENTICTON':
				package_location = destination_city
				package_arrived = True
			else:
				package_location = main_hubs[2][0]
				print('Your Package is in:', package_location)
	if package_location == 'WHITEHORSE':
		if destination_city == 'WHITEHORSE':
			package_location = destination_city
			package_arrived = True
		else:
			package_location = main_hubs[3][0]
			number_of_moves += 1
			print('Your Package is in:', package_location)
	if package_location == 'YELLOWKNIFE':
		if destination_city == 'INUVIK' or destination_city == 'YELLOWKNIFE':
			package_location = destination_city
			package_arrived = True
		else:
			package_location = main_hubs[3][0]
			number_of_moves += 1
			print('Your Package is now at:', package_location)
	if package_location == 'SASKATOON' or package_location == 'REGINA':
		if package_location == 'SASKATOON':
			if destination_city == 'SASKATOON' or destination_city == 'PRINCE ALBERT':
				package_location = destination_city
				package_arrived = True
			else:
				package_location = main_hubs[4][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
		if package_location == 'REGINA':
			if destination_city == 'REGINA' or destination_city == 'SWIFT CURRENT':
				package_location = destination_city
				package_arrived = True	
			elif destination_city == 'SASKATOON' or destination_city == 'PRINCE ALBERT':
				package_location = regional_hubs[2][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
			elif direction == 'west':
				package_location = main_hubs[3][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
			elif direction == 'east':
				package_location = main_hubs[5][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
	if package_location == 'WINNIPEG':
		if destination_city == 'WINNIPEG' or destination_city == 'BRANDON' or destination_city == 'THOMPSON' or destination_city == 'KENORA' or destination_city == 'DRYDEN':
				package_location = destination_city
				package_arrived = True
		elif expedited:
			if destination_city == 'VANCOUVER' or destination_city == 'PRINCE GEORGE' or destination_city == 'KELOWNA' or destination_city == 'CRANBROOK' or destination_city == 'VICTORIA' or destination_city == 'WHISTLER' or destination_city == 'KAMLOOPS' or destination_city == 'PENTICTON' or destination_city == 'ABBOTSFORD':
				package_location = main_hubs[2][0]
				number_of_moves += 1	
				print('Your Package is in:', package_location)
			elif direction == 'west':
				package_location = main_hubs[3][0]
				number_of_moves += 1	
				print('Your Package is in:', package_location)
			else:
				package_location = main_hubs[6][0]
				number_of_moves += 1	
				print('Your Package is in:', package_location)
		elif direction == 'west':
				package_location = main_hubs[4][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
		elif destination_city == 'THUNDER BAY':
				package_location = regional_hubs[3][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
		else:
				package_location = main_hubs[6][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
	if package_location == 'THUNDER BAY' or package_location == 'SUDBURY' or package_location == 'LONDON' or package_location == 'HAMILTON' or package_location == 'MISSISSAUGA' or package_location == 'OTTAWA':
		while True:
			if package_location == 'THUNDER BAY':
				if destination_city == 'THUNDER BAY':
					package_location = destination_city
					package_arrived = True
					break	
				elif destination_city == 'KENORA' or destination_city == 'DRYDEN' or direction == 'west':
					package_location = main_hubs[5][0]					
					number_of_moves += 1
					print('Your Package is in:', package_location)
					break
				elif direction == 'same province' or direction == 'east':
					package_location = regional_hubs[3][2]
					number_of_moves += 1
					print('Your Package is in:', package_location)
			if package_location == 'LONDON':
				if destination_city == 'WINDSOR' or destination_city == 'SARNIA' or destination_city == 'LONDON' or destination_city == 'CHATHAM-KENT':
					package_location = destination_city
					package_arrived = True
					break
				else:
					number_of_moves += 1			
					package_location = regional_hubs[3][3]
					print('Your Package is in:', package_location)
			if package_location == 'SUDBURY':
				if destination_city == 'NORTH BAY' or destination_city == 'TIMMINS' or destination_city == 'SAULT STE. MARIE' or destination_city == 'SUDBURY':
					package_location = destination_city
					package_arrived = True
					break
				elif destination_city == 'THUNDER BAY' or destination_city == 'KENORA' or destination_city == 'DRYDEN' or direction == 'west':
					package_location = regional_hubs[3][0]	
					number_of_moves += 1
					print('Your Package is in:', package_location)
				else:
					package_location = main_hubs[6][0]
					number_of_moves += 1
					print('Your Package is in:', package_location)
			if package_location == 'HAMILTON':
				if destination_city == 'KITCHNER' or destination_city == 'BRANTFORD' or destination_city == 'NIAGARA FALLS' or destination_city == 'HAMILTON':
					package_location = destination_city
					package_arrived = True
					break
				elif destination_city == 'WINDSOR' or destination_city == 'SARNIA' or destination_city == 'LONDON':
					package_location = regional_hubs[3][1]
					number_of_moves += 1
					print('Your Package is in:', package_location)
				else:	
					package_location = main_hubs[6][0]
					number_of_moves += 1
					print('Your Package is in:', package_location)
			if package_location == 'MISSISSAUGA':
				if destination_city == 'THUNDER BAY' or destination_city == 'TIMMINS' or destination_city == 'NORTH BAY' or destination_city == 'SAULT STE. MARIE' or destination_city == 'SUDBURY':
					package_location = regional_hubs[3][2]
					number_of_moves += 1
					print('Your Package is in:', package_location)
				elif destination_city == 'KINGSTON' or destination_city == 'BELLEVILLE' or destination_city == 'OTTAWA' or destination_city == 'GATINEAU' or destination_city == "VAL-D'OR" or destination_city == 'CORNWALL':
					package_location = main_hubs[6][1]
					number_of_moves += 1
					print('Your Package is in:', package_location)
				elif destination_city == 'HAMILTON' or destination_city == 'LONDON' or destination_city == 'WINDSOR' or destination_city == 'SARNIA' or destination_city == 'KITCHNER' or destination_city == 'BRANTFORD' or destination_city == 'NIAGARA FALLS' or destination_city == 'CHATHAM-KENT':
					package_location = regional_hubs[3][3]
					number_of_moves += 1
					print('Your Package is in:', package_location)
				elif destination_city == 'BRAMPTON' or destination_city == 'BARRIE' or destination_city == 'MISSISSAUGA' or destination_city == 'TORONTO' or destination_city == 'OSHAWA' or destination_city == 'PETERBOROUGH' or destination_city == 'OWEN SOUND':
					package_location = destination_city
					package_arrived = True
					break	
				elif expedited:
					if destination_city == 'VANCOUVER' or destination_city == 'KELOWNA' or destination_city == 'PRINCE GEORGE' or destination_city == 'CRANBROOK' or destination_city == 'VICTORIA' or destination_city == 'WHISTLER' or destination_city == 'KAMLOOPS' or destination_city == 'PENTICTON' or destination_city == 'ABBOTSFORD':
						package_location = main_hubs[2][0]
						number_of_moves += 1
						print('Your Package is in:', package_location)
						break
					if destination_city == 'WHITEHORSE' or destination_city == 'YELLOWKNIFE' or destination_city == 'INUVIK' or destination_city == 'CALGARY' or destination_city == 'GRANDE PRAIRIE' or destination_city == 'FORT MCMURRAY' or destination_city == 'EDMONTON' or destination_city == 'LETHBRIDGE' or destination_city == 'MEDICINE HAT' or destination_city == 'SASKATOON' or destination_city == 'REGINA' or destination_city == 'PRINCE ALBERT' or destination_city == 'LLOYDMINSTER' or destination_city == 'SWIFT CURRENT':
						package_location = main_hubs[3][0]
						number_of_moves += 1
						print('Your Package is in:', package_location)
						break
					if destination_city == 'HALIFAX' or destination_city == 'MONCTON' or destination_city == 'FREDERICTON' or destination_city == 'SAINT JOHN' or destination_city == 'SYDNEY' or destination_city == 'GANDER' or destination_city == 'DEER LAKE' or destination_city == "SAINT JOHN's" or destination_city == 'CHARLOTTETOWN' or destination_city == 'STEPHENVILLE':
						package_location = main_hubs[9][0] 
						number_of_moves += 1
						print('Your Package is in:', package_location)
						break
					if destination_city == 'WINNIPEG' or destination_city == 'BRANDON' or destination_city == 'THOMPSON' or destination_city == 'KENORA' or destination_city == 'DRYDEN':
						package_location = main_hubs[5][0]
						number_of_moves += 1
						print('Your Package is in:', package_location)
						break
					else:
						package_location = main_hubs[7][0]
						number_of_moves += 1
						print('Your Package is in:', package_location)
						break
				elif direction == 'west' or destination_city == 'KENORA' or destination_city == 'DRYDEN':
					package_location = main_hubs[5][0]
					number_of_moves += 1
					print('Your Package is in:', package_location)
					break
				elif direction == 'east':
					package_location = main_hubs[7][0]
					number_of_moves += 1
					print('Your Package is in:', package_location)
					break
			if package_location == 'OTTAWA':
				if destination_city == 'GATINEAU' or destination_city == 'KINGSTON' or destination_city == 'BELLEVILLE' or destination_city == "VAL-D'OR" or destination_city == 'OTTAWA' or destination_city == 'CORNWALL':
					package_location = destination_city
					package_arrived = True
					break
				elif direction == 'west' or direction == 'same province':
					package_location = main_hubs[6][0]
					number_of_moves += 1
					print('Your Package is in:', package_location)
				else:
					package_location = main_hubs[7][0]
					number_of_moves += 1
					print('Your Package is in:', package_location)
					break
	if package_location == 'MONTREAL' or package_location == 'QUEBEC CITY':
		if package_location == 'MONTREAL':
			if destination_city == 'MONTREAL' or destination_city == 'SHERBROOKE' or destination_city == 'TROIS-RIVIERES' or destination_city == 'IQALUIT':
				package_location = destination_city
				package_arrived = True
			elif destination_city == "VAL-D'OR" or destination_city == 'GATINEAU' or destination_city == 'OTTAWA' or destination_city == 'KINGSTON' or destination_city == 'BELLEVILLE' or destination_city == 'CORNWALL':
				package_location = main_hubs[6][1]
				number_of_moves += 1
				print('Your Package is in:', package_location)
			elif direction == 'west':
				package_location = main_hubs[6][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
			elif destination_city == 'QUEBEC CITY' or destination_city == 'SAGUENAY' or destination_city == 'SEPT-ILES' or destination_city == 'RIMOUSKI':
				package_location = main_hubs[7][1]
				number_of_moves += 1
				print('Your Package is in:', package_location)
			else:
				package_location = main_hubs[9][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
		if package_location == 'QUEBEC CITY':
			if destination_city == 'QUEBEC CITY' or destination_city == 'SAGUENAY' or destination_city == 'SEPT-ILES' or destination_city == 'RIMOUSKI':
				package_location = destination_city
				package_arrived = True
			elif direction == 'west' or direction == 'same province':
				package_location = main_hubs[7][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
			elif direction == 'east':
				package_location = main_hubs[9][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
	if package_location == 'MONCTON':
		if destination_city == 'FREDERICTON' or destination_city == 'SAINT JOHN' or destination_city == 'MONCTON':
			package_location = destination_city
			package_arrived = True
		elif destination_city == 'GANDER' or destination_city == "SAINT JOHN's" or destination_city == 'DEER LAKE' or destination_city == 'STEPHENVILLE':
			package_location = main_hubs[8][0]
			number_of_moves += 1
			print('Your Package is in:', package_location)
		elif destination_city == 'CHARLOTTETOWN':
			package_location = main_hubs[10][0]
			number_of_moves += 1
			print('Your Package is in:', package_location)
		elif destination_city == 'HALIFAX' or destination_city == 'SYDNEY':
			package_location = regional_hubs[5][1]
			number_of_moves += 1
			print('Your Package is in:', package_location)
		elif expedited:
			if destination_city != 'MONTREAL' or destination_city != 'QUEBEC CITY' or destination_city != 'TROIS-RIVIERES' or destination_city !=  'SHERBROOKE' or destination_city != 'SAGUENAY' or destination_city != 'SEPT-ILES' or destination_city != 'RIMOUSKI' or destination_city != 'IQALUIT':
				if destination_city == 'VANCOUVER' or destination_city == 'KELOWNA' or destination_city == 'PRINCE GEORGE' or destination_city == 'VICTORIA' or destination_city == 'CRANBROOK' or destination_city == 'WHISTLER' or destination_city == 'KAMLOOPS' or destination_city == 'PENTICTON' or destination_city == 'ABBOTSFORD':
					package_location = main_hubs[2][0]
					number_of_moves += 1
					print('Your Package is in:', package_location)
				else: 
					package_location = main_hubs[6][0]
					number_of_moves += 1
					print('Your Package is in:', package_location)
		else:
			package_location = main_hubs[7][1]
			number_of_moves += 1
			print('Your Package is in:', package_location)
	if package_location == 'CHARLOTTETOWN':
		if destination_city == 'CHARLOTTETOWN':
			packge_location = destination_city
			package_arrived = True
		else:	
			package_location = main_hubs[9][0]
			number_of_moves += 1
			print('Your Package is in:', package_location)
	if package_location == 'DEER LAKE' or package_location == "SAINT JOHN'S":
		if package_location == 'DEER LAKE':
			if destination_city == 'DEER LAKE' or destination_city == 'STEPHENVILLE':
				package_location = destination_city
				package_arrived = True
			else:
				package_location = main_hubs[8][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
		if package_location == "SAINT JOHN'S":
			if destination_city == 'GANDER':
				package_location = destination_city
				package_arrived = True
			elif destination_city == 'DEER LAKE' or destination_city == 'STEPHENVILLE':
				package_location = regional_hubs[4][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
			else:
				package_location = main_hubs[9][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
	if package_location == 'HALIFAX' or package_location == 'SYDNEY':
		if package_location == 'HALIFAX':
			if destination_city == 'HALIFAX':
				package_location = destination_city
				package_arrived = True
			elif destination_city == 'SYDNEY':
				package_location = regional_hubs[5][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
			else: 
				package_location = main_hubs[9][0]
				number_of_moves += 1
				print('Your Package is in:', package_location)
		if package_location == 'SYDNEY':
			if destination_city == 'SYDNEY':
				package_location = destination_city
				package_arrived = True
			else:
				package_location = regional_hubs[5][1]
				number_of_moves += 1
				print('Your Package is in:', package_location)
	#once package arrives, it will calculate all costs
	if package_arrived == True:						
		print("Your Package is at it's final destination.")
		print()
		cost = 7.5 * weight
		print('The base charge is: $', format(cost, ',.2f'), sep='')
		cost = cost + long_distance_surcharge_fee
		print('The long distance fee is: $', format(long_distance_surcharge_fee, ',.2f'), sep='')
		surcharge_fee = cost * surcharge_fee
		print('The surcharge fee is: $', format(surcharge_fee, ',.2f'), sep='')
		print('The quebec surcharge is: $', format(quebec_surcharge, ',.2f'), sep='')
		cost = cost + surcharge_fee + quebec_surcharge
		if expedited == True:
			expedited_fee = cost * .35
			print('The expedited fee is: $', format(expedited_fee, ',.2f'), sep='')	
		else:
			expedited_fee = 0
		price_before_tax = cost + expedited_fee 
		tax = price_before_tax * .1
		print('The taxes are: $', format(tax, ',.2f'), sep='')
		final_cost = price_before_tax + tax
		print('The cost to ship this item will be: $', format(final_cost, ',.2f'), sep='')
		print()
		if origin_city == point_of_origin:			#determines how many days it took for package to travel
			print('Your package will arrive in:', number_of_moves - 1, 'days')
		else:			
			print('Your package will arrive in:', number_of_moves, 'days')
		print()
