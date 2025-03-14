Feature: Test Scenarios for target cart
  Scenario: User can see empty cart when he click on the cart icon
    Given Open target page
    When click on cart icon
    Then your cart is empty message is shown

  Scenario: User can see sign in page
    Given Open target page
    When click on sign in button
    Then verify sign in form opened
