@smoke @cart @add_to_cart
Feature: Add product to cart

  Scenario: Add a backpack to the cart
    Given I log in as "standard_user" with password "secret_sauce"
    When I add "Sauce Labs Backpack" to the cart
    Then the cart badge should show 1 item
