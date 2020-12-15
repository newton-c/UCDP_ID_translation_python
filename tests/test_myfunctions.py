from UCDP_ID_translation import ucdp

test_id = [201, 204, 207, 208, 216, 219, 229,
    238, 241, 244, 245, 246, 248, 254, 256, 257,
    263, 273, 279, 285, 286, 214, 215, 218, 226,
    228, 232, 235]

def test_ucdp():
    assert ucdp.ucdp_ids(test_id, 'new_id', 'old_id', 'conflict_id')