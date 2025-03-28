Feature: search for product

  Scenario: User can search for a tea on Target
    Given Open target page
    When Search for tea
    Then verify user can see the tea
    And Verify tea in URL

  Scenario: User can search for a iPhone on Target
    Given Open target page
    When Search for iPhone
    Then verify user can see the iPhone

  Scenario: User can search for a dress on Target
    Given Open target page
    When Search for dress
    Then verify user can see the dress

  Scenario: Verify that user can see product names and images
    Given Open target page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image