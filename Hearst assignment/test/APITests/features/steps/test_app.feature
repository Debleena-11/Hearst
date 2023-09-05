# Author: Debleena Jana
# Rev: 1.0
# Creation date: 09/04/2023
# This feature file supports and provides step definations for testing the server backend api's 
Feature: Testing FastAPI endpoints

  Scenario: Get endpoint1 numbers
    When I retrieve numbers from endpoint1
    Then the response should contain numbers from 1 to 10

  Scenario Outline: Square a number with endpoint2
    When I send a number <number> to endpoint2
    Then I receive its square <square>

    Examples:
      | number | square |
      | 2      | 4     |
      | 3      | 9     |

  Scenario Outline: Test odd number in endpoint3
    When I send the odd number <oddNumber> to endpoint3
    Then I should get <halfNumber> as the result

    Examples:
      | oddNumber | halfNumber |
      | 3      | 1.5     |
      | 5      | 2.5     |	

  Scenario Outline: Test even number in endpoint3
    When I send the even number <evenNumber> to endpoint3
    Then I should receive an error
    Examples:
      | evenNumber |
      | 2      |
      | 4      |	
	  
  Scenario: Send a large number to endpoint2 and get its square
    When I send a number 10000 to endpoint2
    Then I receive its square 100000000

  Scenario: Send alphabet character to endpoint2
    Given I send the character "a" to endpoint2
    Then I should receive a validation error

  Scenario: Send alphabet character to endpoint3
    Given I send the character "b" to endpoint3
    Then I should receive a validation error
	

  # Edge & Negative Tests
  Scenario: Send 0 to endpoint2 and get its square
    When I send a number 0 to endpoint2
    Then I receive its square 0

  Scenario: Send 0 to endpoint3 and get an error
    When I send the odd number 0 to endpoint3
    Then I should receive an error

  Scenario: Send a fraction to endpoint2
    When I send a number 0.5 to endpoint2
    Then I should receive a validation error

  Scenario: Send a negative number to endpoint2 and get its square
    When I send a number -3 to endpoint2
    Then I receive its square 9
	
  Scenario Outline: Send a negative odd number to endpoint3 and get its halfed value
    When I send the odd number <oddNumber> to endpoint3
    Then I should get <halfNumber> as the result

    Examples:
      | oddNumber | halfNumber |
      | -3      | -1.5     |
      | -5      | -2.5     |

  Scenario Outline: Test negative even number in endpoint3
    When I send the even number <evenNumber> to endpoint3
    Then I should receive an error
    Examples:
      | evenNumber |
      | -2      |
      | -4      |

  Scenario: Send a large number to endpoint2 and get its square
    When I send a number 10000 to endpoint2
    Then I receive its square 100000000

  Scenario: Send alphabet character to endpoint2
    Given I send the character "a" to endpoint2
    Then I should receive a validation error

  Scenario: Send alphabet character to endpoint3
    Given I send the character "b" to endpoint3
    Then I should receive a validation error