from api import PetPriends
from settings import valid_email, valid_pass

pf = PetPriends()
pet_name = 'чучело23'
pet_type = 'Котопёс2'
pet_age = 100
pet_name_with_photo = 'чучелоWithPhoto'
pet_type_with_photo = 'КотопёсWithPhoto'
pet_age_with_photo = 1144
pet_changed_name = 'чучело22222'
pet_changed_type = 'Котопёс22222'
pet_changed_age = 10222220
pet_changed_age_not_valid = -1


def get_id_of_added_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_pass)
    _, pet_id = pf.get_pets_list(auth_key, filter='')
    return pet_id['pets'][0]['id'], pet_id['pets'][0]['name']


def test_get_api_key_for_valid_user(email=valid_email, password=valid_pass):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_list_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_pass)
    status, result = pf.get_pets_list(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_create_pet_without_photo_with_valid_data():
    _, auth_key = pf.get_api_key(valid_email, valid_pass)
    status, result = pf.post_create_pet_simple(auth_key, pet_name, pet_type, pet_age)
    assert status == 200
    assert result['id'] != ''


def test_edit_pet_name_width_valid_key():
    pet_id_to_change, old_pet_name = get_id_of_added_pet()
    _, auth_key = pf.get_api_key(valid_email, valid_pass)
    status, result = pf.put_adit_information_about_pet(auth_key, pet_id_to_change, pet_changed_name, pet_changed_type,
                                                       pet_changed_age)
    assert status == 200
    assert result['age'] != pet_changed_name


def test_change_pet_age_with_valid_key_and_not_valid_data():
    pet_id_to_change, old_pet_name = get_id_of_added_pet()
    _, auth_key = pf.get_api_key(valid_email, valid_pass)
    status, result = pf.put_adit_information_about_pet(auth_key, pet_id_to_change, '', '',
                                                       pet_changed_age_not_valid)
    assert status != 200
    assert result['age'] != pet_changed_age_not_valid


def test_delete_pet_with_valid_key_and_id():
    _, auth_key = pf.get_api_key(valid_email, valid_pass)
    pet_id_for_delete, _ = get_id_of_added_pet()
    status = pf.delete_pet_from_db(auth_key, pet_id_for_delete)
    assert status == 200


def test_post_create_pet_with_photo_with_valid_auth_key():
    _, auth_key = pf.get_api_key(valid_email, valid_pass)
    status, result = pf.post_create_pet_with_photo(auth_key, pet_name_with_photo, pet_type_with_photo,
                                                   pet_age_with_photo, 'cat.jpg')
    assert status == 200
    assert result['name'] == pet_name_with_photo


# negative tests
def test_get_api_key_for_valid_user_and_wrong_pass(email=valid_email, password='125410'):
    status, result = pf.get_api_key(email, password)
    assert status != 200


def test_get_api_key_for_valid_user_and_no_password(email=valid_email, password=''):
    status, result = pf.get_api_key(email, password)
    assert status != 200


def test_get_api_key_for_not_valid_user_and_correct_password(email='test', password=valid_pass):
    status, result = pf.get_api_key(email, password)
    assert status != 200


def test_create_pet_without_photo_with_valid_data_without_valid_key():
    auth_key = {'key': ''}
    status, result = pf.post_create_pet_simple(auth_key, pet_name, pet_type, pet_age)
    assert status != 200


def test_simple_create_pet_with_valid_key_with_empty_data():
    _, auth_key = pf.get_api_key(valid_email, valid_pass)
    status, result = pf.post_create_pet_simple(auth_key, ' ', ' ', ' ')
    assert status != 200



