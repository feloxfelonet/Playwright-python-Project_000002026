@regression @products @product_details
Feature: Product details

  Scenario: Open a product detail page
    Given I log in as "standard_user" with password "secret_sauce"
    When I open the product "Sauce Labs Backpack"
    Then the product details should show "Sauce Labs Backpack"
