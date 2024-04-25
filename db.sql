CREATE TABLE Restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    phone_number VARCHAR(20)
);

CREATE TABLE Users (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

CREATE TABLE FoodItems (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    restaurant_id INT,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurants(id)
);

CREATE TABLE Orders (
    id INT PRIMARY KEY,
    user_id INT,
    food_item_id INT,
    quantity INT,
    order_date TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (food_item_id) REFERENCES FoodItems(id)
);