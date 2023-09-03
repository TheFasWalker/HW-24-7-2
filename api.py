'''
swagger api information
https://petfriends.skillfactory.ru/apidocs/
'''

import requests


class PetPriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru/'

    def get_api_key(self, email, password):
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_pets_list(self, auth_key, filter):
        headers = {
            'auth_key': auth_key['key']
        }
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_create_pet_simple(self, auth_key, name, animal_type, age):
        headers = {
            'auth_key': auth_key['key']
        }
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_pet_from_db(self, auth_key, pet_id, ):
        headers = {
            'auth_key': auth_key['key']
        }
        res = requests.delete(self.base_url + f'api/pets/{pet_id}', headers=headers)
        status = res.status_code
        return status

    def put_adit_information_about_pet(self, auth_key, pet_id, name='', animal_type='', age=''):
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        headers = {
            'auth_key': auth_key['key']
        }
        res = requests.put(self.base_url + f'api/pets/{pet_id}', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_create_pet_with_photo(self, auth_key, name='', animal_type='', age='', pet_photo=''):
        headers = {
            'auth_key': auth_key['key']
        }
        # pet_photo = open('cat.jpg', 'rb')

        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'),'image/jpeg')}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data,files=file)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
