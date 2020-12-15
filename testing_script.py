'''
Testing the UCDP codes library. The line exec(open('ucdp_pds.py').read()) needs
to remain unchanged, and everything needs to stay in the directories as is.
Everything else can be changed to test the functions and try to break this
code.
'''

# exec(open('ucdp_ids.py').read())

import pandas as pd
from UCDP_ID_translation import ucdp

df = pd.read_csv(r'data/ucdp-prio-acd-201.csv')

old_ids = ucdp.ucdp_ids(df['conflict_id'], 'new_id', 'old_id', 'conflict_id')
print(old_ids[:25])

new_ids = ucdp.ucdp_ids(old_ids, 'old_id', 'new_id', 'conflict_id')
print(new_ids[:25])
