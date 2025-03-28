Feature: Test Scenarios for target cart
  Scenario: User can see empty cart when he click on the cart icon
    Given Open target page
    When click on cart icon
    Then your cart is empty message is shown
    And Verify cart page opens



Scenario: User can see the added product at the cart
    Given Open target page
    When search for tea
    And click on add to cart button
    Then verify 'added to cart' text is shown