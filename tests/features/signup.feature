Feature: Signup
    User is able to register, login

Scenario: Login with invalid credentials
    Given I am on the login page
    When I login with dummy@email.com and password
    Then I see error message