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