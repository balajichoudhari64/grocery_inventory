The Grocery Inventory Management System is a project that aims to provide a convenient way to manage a grocery inventory. It includes two main components: an API server for handling inventory management operations and a user interface (UI) for visualizing and interacting with the inventory.The project allows users to add grocery items to the inventory and retrieve a list of all items stored in the inventory. 

Run the application:
  1.Open a terminal or command prompt.
  2.Navigate to the directory where your project files are located.
  3.Run the command python app.py to start the Flask server.

Test the endpoints:
  1.Open a web browser and go to http://localhost:5000.
  2.You should see the form for adding items to the inventory and the current inventory table.
  3.Fill out the form with an item name and quantity, then click the "Add Item" button.
  4.You should see a success message indicating that the item was added.
  5.The inventory table should now display the item you added.
  6.To view the JSON representation of the inventory directly, you can access http://localhost:5000/inventory in your browser or use tools like Postman or cURL to send a GET request to that endpoint.
