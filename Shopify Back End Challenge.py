#author Duc Trung Nguyen
#2018-01-06
#Shopify Back End Challenge

from Menu import Menu

import json 

def parse_menu(menu, py_menus):

    this_id = menu['id']
    this_data = menu['data']
    this_child = menu['child_ids']
    menus = json.loads(req.get('https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page=0').text)
    START_PAGE = menus['pagination']['current_thing']
    TOTAL_PAGES  = int(menus['pagination'] ['total'] / menus['pagination'] ['per_page']) + 1 
    collection = []

    if not 'parent_id' in menu:
        py_menus.append(Menu(this_id, this_data, this_child))
        

    if 'parent_id' in menu:
        this_parent = menu['parent_id']

        for i in py_menus: 
            if i.is_child(this_parent):
                i.add_child(menu) 
    
    for thing in range(START_PAGE, TOTAL_PAGES):
        if (thing !=  START_PAGE): 
            menus = json.loads(req.get('https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page='+ str(thing)).text)
      
        menus = menus['menus']

        for menu in menus :  
            parse_menu(menu , collection)
    
    result = {"invalid_menus":[], "valid_menus":[]}
    for i in collection:
        if not i.is_valid:
            result['invalid_menus'].append(i.__dict__())
        
        if i.is_valid:
            result['valid_menus'].append(i.__dict__())
    