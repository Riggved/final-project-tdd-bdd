Feature: The product store service back-end
    As a Product Store Owner
    I need a RESTful catalog service
    So that I can keep track of all my products

Background:
    Given the following products
        | name       | description     | price | available | category    |
        | Hat        | A red hat       | 59.99 | True      | CLOTHS      |
        | Pants      | Blue jeans      | 39.95 | True      | CLOTHS      |
        | Shirt      | Casual shirt    | 24.50 | False     | CLOTHS      |
        | Apple      | Fresh red apple | 1.99  | True      | FOOD        |
        | Banana     | Yellow fruit    | 0.99  | False     | FOOD        |
        | Pots       | Cooking pots    | 89.95 | True      | HOUSEWARES  |

Scenario: The server is running
    When I visit the "Home Page"
    Then I should see "Product Catalog Administration" in the title
    And I should not see "404 Not Found"

Scenario: Read a Product
    When I visit the "Home Page"
    And I set the "Name" to "Hat"
    And I press the "Search" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    And I should see "Hat" in the "Name" field
    And I should see "A red hat" in the "Description" field
    And I should see "59.99" in the "Price" field
    And I should see "Cloths" in the "Category" dropdown
    And I should see "True" in the "Available" dropdown

Scenario: Update a Product
    When I visit the "Home Page"
    And I set the "Name" to "Hat"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the "Name" field
    And I should see "A red hat" in the "Description" field
    When I change the "Description" to "A blue hat"
    And I press the "Update" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    And I should see "A blue hat" in the "Description" field
    When I press the "Clear" button
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "A blue hat" in the results
    And I should not see "A red hat" in the results

Scenario: Delete a Product
    When I visit the "Home Page"
    And I set the "Name" to "Hat"
    And I press the "Search" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Delete" button
    Then I should see the message "Product has been Deleted!"
    When I press the "Clear" button
    And I press the "Search" button
    Then I should see the message "Success"
    And I should not see "Hat" in the results

Scenario: List all Products
    When I visit the "Home Page"
    And I press the "Clear" button
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the results
    And I should see "Pants" in the results
    And I should see "Shirt" in the results
    And I should see "Apple" in the results

Scenario: Search by Category
    When I visit the "Home Page"
    And I select "Food" in the "Category" dropdown
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Apple" in the results
    And I should not see "Hat" in the results
    And I should not see "Pants" in the results

Scenario: Search by Availability
    When I visit the "Home Page"
    And I select "True" in the "Available" dropdown
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the results
    And I should see "Pants" in the results
    And I should not see "Shirt" in the results

Scenario: Search by Name
    When I visit the "Home Page"
    And I set the "Name" to "Hat"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the results
    And I should not see "Pants" in the results
    And I should not see "Shirt" in the results
