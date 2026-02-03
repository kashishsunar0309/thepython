#store informatioin about a pizza being ordered.
pizza ={
    'crust':'thick',
    'topping':['mushroom','extra cheese'],
}
#summarize the order.
print(f'you ordered a {pizza["crust"]}-crust pizza','with the following topping:')
for topping in pizza['topping']:
    print(f'\t {topping}')
# self one 
grade ={  
        'totalstudents':'grade 8',
        'gender':['boy are 25','girl are 20'],
    }
print(f"the student are {grade['totalstudents']}","they are going  to complete this year ble exam")
for gender in grade['gender']:
    print(f'\t{gender}')
print('')
#self two
fav_language ={
    
    'kashish':['java','python','rust'],
    'deepson':['c','c++','c holy'],
    'roshan':['javascript','ruby','css','typescript'],
    'aryan':['css','html','django'],
}
for name,language in fav_language.items():
    print(f'my name is {name} mine fav language are:')
    for languages in language:
        print(f"{languages}")
        
#dict in dict method
user = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },    
}
for username,user_info in user.items():
    print(f'\n Username: {username}')
    full_name = f'{user_info["first"]}{user_info ["last"]}'
    location = user_info['location']
    print(f'\t Full name: {full_name.title()}')
    print(f'\t location:{location.title()}')
    
print('')
    
 #self one  
place= {
    'nepal':{
        'capital':'kathmandu',
        'tourist':'porkhara',
        'temple':'janaki temple ommmmm!',
    },
    'india':{
        'capital':'new delhi',
        'tourist':'kolkata',
        'temple':'kadarnath temple ommmm!',
    },
}
for country,place_info in place.items():
    print(f'country_name:{country}')
    place_name = f'{place_info["capital"]}, {place_info["tourist"]}'
    temple_name = place_info['temple']
    print(f'\tplace_name:{place_name.title()}')
    print(f'\ttemple_name:{temple_name.title()}')