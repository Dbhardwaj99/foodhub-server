from appwrite.client import Client
from appwrite.services.databases import Databases

client = Client()

(client
  .set_endpoint('https://cloud.appwrite.io/v1')
  .set_project('66266c3fd4129184d064')
  .set_key('0ccca2e3cb4ff3a210867c7b13599d3946d88b2b1085e612b4dbe79c40c0aab1419df2cdfc8a29c261066494960ee58cd7f4af87f84bb273949b2e53ab568ad01819661225d2d4c72f6f0130d6659fa108f68a85b65c3e185061a6c808e075915509ab6729459c6ec9e868b1fbd01ef9df311b6063e1fe83cd7ebffe596a0f4b') 
)

databases = Databases(client)

def fetch_items():
    try:
        result = databases.list_documents('66266c7731d81704bff0', 'fooditem')
        return extract_item_data(result['documents'])
    except Exception as e:
        print(f"An error occurred: {e}")
        return []  # Return empty on error
    

def extract_item_data(api_response):
    new_format = {'request': []}  # Initialize output structure

    # Your API response is a list, not a dictionary
    if isinstance(api_response, list):  # Check if it's a list
        for food_item in api_response:  # Iterate directly over food items
            new_format['request'].append({
                'name': food_item['name'],
                'price': food_item['price'],
                'id': food_item['id'],
                'imageURL': food_item.get('imageURL', None),
                'description': food_item.get('description', None),
                'calories': food_item.get('calories', None),
                'protein': food_item.get('protein', None),
                'carbs': food_item.get('carbs', None)
            })

    print(new_format)  # Print the transformed data
    return new_format

