'''
TO DO: Actor and dyad IDs are currently only numeric, though UCDP also has
strings that could be included.
'''

import pickle
import numpy as np

with open('dictionaries/actor_id.txt', 'rb') as f:
    data = f.read()
actor_dict = pickle.loads(data)

with open('dictionaries/conflict_id.txt', 'rb') as f:
    data = f.read()
conflict_dict = pickle.loads(data)

with open('dictionaries/dyad_id.txt', 'rb') as f:
    data = f.read()
dyad_dict = pickle.loads(data)


def get_key(dicts, val):
    for key, value in dicts.items():
        if val == value:
            return key


def actor_ids(id_var, source_id, target_id):
    '''
    Coverting between old and new UCDP actor ids. The imputs
    as the variable with the ID to be converted (id), whether the variable
    is the new or the old ID (source_id), and whether the varible is being
    converted to the new or old ID (target_var).
    '''
    valid_ids = ['new_id', 'old_id']
    target_id_var = list()
    if source_id not in valid_ids:
        return "Error: unknown source_id"
    if target_id not in valid_ids:
        return "Error: unknown target_id"
    if source_id == 'new_id' and target_id == 'old_id':
        for i in range(len(id_var)):
            if id_var[i] in actor_dict:
                target_id_var.append(actor_dict.get(id_var[i]))
            else:
                target_id_var.append(np.nan)
    elif source_id == 'old_id' and target_id == 'new_id':
        for i in range(len(id_var)):
            if id_var[i] in actor_dict.values():
                target_id_var.append(get_key(actor_dict, id_var[i]))
            else:
                target_id_var.append(np.nan)
    return target_id_var


def conflict_ids(id_var, source_id, target_id):
    '''
    Coverting between old and new UCDP state-based conflict ids. The imputs
    as the variable with the ID to be converted (id), whether the variable
    is the new or the old ID (source_id), and whether the varible is being
    converted to the new or old ID (target_var).
    '''
    valid_ids = ['new_id', 'old_id']
    target_id_var = list()
    if source_id not in valid_ids:
        return "Error: unknown source_id"
    if target_id not in valid_ids:
        return "Error: unknown target_id"
    if source_id == 'new_id' and target_id == 'old_id':
        for i in range(len(id_var)):
            if id_var[i] in conflict_dict:
                target_id_var.append(conflict_dict.get(id_var[i]))
            else:
                target_id_var.append(np.nan)
    elif source_id == 'old_id' and target_id == 'new_id':
        for i in range(len(id_var)):
            if id_var[i] in conflict_dict.values():
                target_id_var.append(get_key(conflict_dict, id_var[i]))
            else:
                target_id_var.append(np.nan)
    return target_id_var


def dyad_ids(id_var, source_id, target_id):
    '''
    Coverting between old and new UCDP dyad ids. The imputs
    as the variable with the ID to be converted (id), whether the variable
    is the new or the old ID (source_id), and whether the varible is being
    converted to the new or old ID (target_var).
    '''
    valid_ids = ['new_id', 'old_id']
    target_id_var = list()
    if source_id not in valid_ids:
        return "Error: unknown source_id"
    if target_id not in valid_ids:
        return "Error: unknown target_id"
    if source_id == 'new_id' and target_id == 'old_id':
        for i in range(len(id_var)):
            if id_var[i] in dyad_dict:
                target_id_var.append(dyad_dict.get(id_var[i]))
            else:
                target_id_var.append(np.nan)
    elif source_id == 'old_id' and target_id == 'new_id':
        for i in range(len(id_var)):
            if id_var[i] in dyad_dict.values():
                target_id_var.append(get_key(dyad_dict, id_var[i]))
            else:
                target_id_var.append(np.nan)
    return target_id_var


def ucdp_ids(id_var, source_id, target_id, code_type):
    '''
    Coverting between old and new UCDP IDs. The imputs
    as the variable with the ID to be converted (id), whether the variable
    is the new or the old ID (source_id), and whether the varible is being
    converted to the new or old ID (target_var), and wether the ID is for
    actors, conflicts, or dyads.
    '''
    if code_type == 'actor_id':
        return actor_ids(id_var, source_id, target_id)
    elif code_type == 'conflict_id':
        return conflict_ids(id_var, source_id, target_id)
    elif code_type == 'dyad_id':
        return dyad_ids(id_var, source_id, target_id)
    else:
        return "Error: code_type not valid"
