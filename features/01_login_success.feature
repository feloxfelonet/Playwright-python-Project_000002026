# @smoke @login @login_success
Feature: Successful login

  Scenario: Standard user can log in
   Given I open the SauceDemo website
   When I enter username "standard_user" and password "secret_sauce"
   And I click the login button
   Then I should see the products page
