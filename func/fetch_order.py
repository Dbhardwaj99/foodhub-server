from appwrite.client import Client
from appwrite.services.databases import Databases

client = Client()

(client
  .set_endpoint('https://cloud.appwrite.io/v1')
  .set_project('66266c3fd4129184d064')
  .set_key('0ccca2e3cb4ff3a210867c7b13599d3946d88b2b1085e612b4dbe79c40c0aab1419df2cdfc8a29c261066494960ee58cd7f4af87f84bb273949b2e53ab568ad01819661225d2d4c72f6f0130d6659fa108f68a85b65c3e185061a6c808e075915509ab6729459c6ec9e868b1fbd01ef9df311b6063e1fe83cd7ebffe596a0f4b') 
)

databases = Databases(client)

def fetch_orders():
    try:
        
        result = databases.list_documents('66266c7731d81704bff0', 'order')
        return extract_order_data(result['documents'])
    except Exception as e:
        print(f"An error occurred: {e}")
        return []  # Return empty on error

# Data Extraction (similar to your JavaScript logic)
def extract_order_data(api_response):
    print(api_response)
    if api_response and len(api_response) > 0:
        order_list = []
        for orders in api_response:
        #   print(orders)
          # order_data = api_response[0]
          food_item_names = ', '.join(item['name'] for item in orders['orderItem'])
        #   print(orders['time'])

          order_list.append({
            'id': orders['id'],
            'items': food_item_names,
            # 'status': orders['status'],
            'time': orders['time'],
            'price': calculate_price(orders['orderItem']),
            # 'restroName': orders['foodItem'][0]['restraunt']['name']
            'name': orders['name'],
            'address': orders['address'],
            'phone_number': orders['phone_number']
          })
        return order_list
    else:
        return None  

# Helper function (replace if needed)
def calculate_price(food_items):
    if not food_items:
        print('No food items found')
        return '₹0'
    else:
        total_price = sum(item['price'] for item in food_items)
        return '₹' + str(total_price)
