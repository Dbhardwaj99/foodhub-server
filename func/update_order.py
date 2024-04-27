from appwrite.client import Client
from appwrite.services.databases import Databases

client = Client()

(client
 .set_endpoint('https://cloud.appwrite.io/v1')  
 .set_project('66266c3fd4129184d064')
 .set_key('0ccca2e3cb4ff3a210867c7b13599d3946d88b2b1085e612b4dbe79c40c0aab1419df2cdfc8a29c261066494960ee58cd7f4af87f84bb273949b2e53ab568ad01819661225d2d4c72f6f0130d6659fa108f68a85b65c3e185061a6c808e075915509ab6729459c6ec9e868b1fbd01ef9df311b6063e1fe83cd7ebffe596a0f4b')  
)

databases = Databases(client)

def update_order(order_id, updated_data):
    try:
        result = databases.update_document(
            '66266c7731d81704bff0',  # Collection ID
            order_id,                 # Document ID
            updated_data              # Data to update
        )
        return True  # Indicate success
    except Exception as e:
        print(f"An error occurred: {e}")
        return False  # Indicate failure
