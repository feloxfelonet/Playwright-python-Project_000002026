@regression @products @sorting @sort_products
Feature: Product sorting

  Scenario: Sort products by price low to high
    Given I log in as "standard_user" with password "secret_sauce"
    When I sort products by "Price (low to high)"
    Then product prices should be sorted from low to high
