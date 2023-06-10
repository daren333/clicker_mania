import unittest
from src.app import create_app
import json

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def test_health_endpoint(self):
        response = self.client.get('/health')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'ok')

    def test_create_pet_endpoint(self):
        data = {
            'name': 'Fluffy',
            'age': 3
        }
        response = self.client.post('/pets', json=data)
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Pet created successfully')
        self.assertEqual(data['pet']['name'], 'Fluffy')
        self.assertEqual(data['pet']['age'], 3)

    def test_get_pets_endpoint(self):
        response = self.client.get('/pets')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data['pets'], list)

    def test_create_pet_function(self):
        from pet_service import create_pet

        pet = create_pet('Buddy', 5)

        self.assertEqual(pet['name'], 'Buddy')
        self.assertEqual(pet['age'], 5)

    def test_get_all_pets_function(self):
        from pet_service import create_pet, get_all_pets

        create_pet('Buddy', 5)
        create_pet('Max', 2)
        pets = get_all_pets()

        self.assertIsInstance(pets, list)
        self.assertEqual(len(pets), 2)

if __name__ == '__main__':
    unittest.main()
