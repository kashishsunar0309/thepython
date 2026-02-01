#list of distionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print('====== aliens =======')
#making empty list for storing aliens:
aliens=[]
#making list of 30 alien 
for aliens_number in range(30):
    new_alien12 ={'color': 'green','point':5,'speed':'slow'}  # PROBLEM 1: Changed '5' to 5 (integer)
    aliens.append(new_alien12)
#show how many aliens have been created.
for alien in aliens[:10]:
    print(alien)  # PROBLEM 2: Changed new_alien12 to alien
#show how many aliens have been created.
print(f'total number of aliens : {len(aliens)}')
print('====== aliens =======')
#making empty list for storing aliens:
aliens=[]
#making list of 30 alien 
for aliens_number in range(30):
    new_alien1 ={'color': 'green','point':5,'speed':'slow'}  # PROBLEM 3: Changed '5' to 5 (integer)
    aliens.append(new_alien1)
for alien in aliens [0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien ["speed"] = 'medium'
        alien ['points'] = 10
    elif alien['color']== 'yellow':
        alien ['color']='red'
        alien['speed']='fast'
        alien['point']=15
#show the first 5 aliens
for alien in aliens [:9]:
    print(alien)
    print('')