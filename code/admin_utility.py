from typing import Final
import os

admin_list_str: Final[str] = os.getenv('ADMIN_LIST')
cached_admin_list = None
is_admin_locked = False

def get_admin_list_with_parameter(admin_list_str, use_caching):
    global cached_admin_list
    if(use_caching and cached_admin_list is not None): 
        return cached_admin_list
    if(admin_list_str == None):
        return []
    admin_list_str = admin_list_str.strip('[]')
    elements = admin_list_str.split(',')
    admin_list = []
    for element in elements:
        try:
            admin_list.append(int(element.strip()))
        except ValueError:
            continue 
    cached_admin_list = admin_list
    return admin_list

    
def get_admin_list():
    return get_admin_list_with_parameter(admin_list_str, True)

def activate_admin_lock():
    global is_admin_locked
    is_admin_locked = True

def deactivate_admin_lock():
    global is_admin_locked
    is_admin_locked = False
    
def check_is_admin_locked() -> bool:
    global is_admin_locked
    return is_admin_locked
