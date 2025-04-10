# Currency Conversion
The Currency Converter project allows you to convert from one currency to another with real-time exchange rates.
It is built using Python and [Exchange Rate Api](https://www.exchangerate-api.com/) that provides accurate and reliable currency conversion rates for 161 currencies. It provides integration for SaaS, Dashboards, and E-Commerce with exceptional uptime and support.

# Table Of Contents
1. [Code](https://github.com/karanzaveri/Currency-Conversion/#code)
2. [UML Diagrams](https://github.com/karanzaveri/Currency-Conversion/#uml-diagrams)
3. [Requirements Engineering](https://github.com/karanzaveri/Currency-Conversion/#requirements-engineering)
4. [Analysis](https://github.com/karanzaveri/Currency-Conversion/#analysis)
5. [DDD](https://github.com/karanzaveri/Currency-Conversion/#ddd)
6. [Metrics](https://github.com/karanzaveri/Currency-Conversion/#metrics)
7. [Clean Code Development](https://github.com/karanzaveri/Currency-Conversion/#clean-code-development)
8. [Build Management](https://github.com/karanzaveri/Currency-Conversion/#build-management)
9. [Unit Tests](https://github.com/karanzaveri/Currency-Conversion/#unit-tests)
10. [IDE](https://github.com/karanzaveri/Currency-Conversion/#ide)
11. [Functional Programming](https://github.com/karanzaveri/Currency-Conversion/#functional-programming)

# Code
To access the code: [Currency Conversion Code](https://github.com/karanzaveri/Currency-Conversion/blob/main/currency_conversion.py)

# UML Diagrams
### 1. Activity Diagram
* The activity diagram showcases a user-driven process, starting with entering source currency followed by target currency and then the amount. Once the valid data is entered, the conversion process is triggered and the converted amount with the applied exchange rate is displayed. 
* [Activity Diagram](https://github.com/karanzaveri/Currency-Conversion/blob/main/UML%20Diagrams/ActivityDiagram.png)

### 2. Use Case Diagram
* The use case diagram outlines how the users interact with the system. Users initiate the currency conversion process by specifying source currency, target currency and amount, while the system performs conversions and provides the results.
* [Use Case Diagram](https://github.com/karanzaveri/Currency-Conversion/blob/main/UML%20Diagrams/UseCaseDiagram.png)

### 3. Class Diagram
* The class diagram represents classes like Currency Converter, Currency Rates, GUI and Error Handling elements, illustrating their relationships and interactions in facilitating user input, data retrieval, and conversion processes within the application.
* [Class Diagram](https://github.com/karanzaveri/Currency-Conversion/blob/main/UML%20Diagrams/ClassDiagram.png)

# Requirements Engineering
### 1. Functional Requirements
* Currency Conversion
* Real-Time Exchange Rates
* Graphical User Interface (GUI)
* User Input Handling
* Transaction History

### 2. Non-Functional Requirements
* Performance
* User Experience (UX)
* Reliability
* Maintainability
* Quality Assurance

### [Trello](https://trello.com/invite/b/g0aGcUnD/ATTI873728185d133e582c79efe96ca36a855FA179CA/currency-conversion)
* Tasklist [Screenshot](https://github.com/karanzaveri/Currency-Conversion/blob/main/images/trello.png)

### [JIRA](https://karanzaveri92.atlassian.net/jira/software/projects/CC/boards/1?atlOrigin=eyJpIjoiZGZkYzc3ZDhjOTY0NGE0Mzg4NjU0MTQyNTNkNThkMzQiLCJwIjoiaiJ9)
* Kanban Board [Screenshot](https://github.com/karanzaveri/Currency-Conversion/blob/main/images/jira.png)

# Analysis
* [Analysis Documentation](https://karan-zaveri.notion.site/Analysis-Currency-Conversion-4b10a770f85840edb3819946a50278b5?pvs=4)
* [Analysis Checklist](https://karan-zaveri.notion.site/Analysis-Checklist-Currency-Conversion-8a3efe00fa5d469d974ba3072fc94a0d?pvs=4)

You can find my Analysis for the Semester Project [here](https://karan-zaveri.notion.site/Analysis-for-the-Semester-Project-60ff70e4746e4fd99f3af4bc02509e2b?pvs=4)

# DDD
Domain-Driven Design (DDD) is an approach to software development that centers around a deep understanding of the business domain. 
[PDF](https://github.com/karanzaveri/Currency-Conversion/blob/main/docs/DDD.pdf)

# Metrics
* [Sonarqube](https://github.com/karanzaveri/Currency-Conversion/blob/main/images/sonarqube.png)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=karanzaveri_Currency-Conversion&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=karanzaveri_Currency-Conversion)

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=karanzaveri_Currency-Conversion&metric=bugs)](https://sonarcloud.io/summary/new_code?id=karanzaveri_Currency-Conversion)

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=karanzaveri_Currency-Conversion&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=karanzaveri_Currency-Conversion)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=karanzaveri_Currency-Conversion&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=karanzaveri_Currency-Conversion)

[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=karanzaveri_Currency-Conversion&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=karanzaveri_Currency-Conversion)

# Clean Code Development

Clean Code Development (CCD) focuses on writing code that is easy to read, understand, and maintain.
[PDF](https://github.com/karanzaveri/Currency-Conversion/blob/main/docs/Clean%20Code%20Development.pdf)

# Build Management

Build management for the Currency Conversion project has been implemented using [Github Actions](https://github.com/karanzaveri/TestCC/actions)

[![Python CI](https://github.com/karanzaveri/Currency-Conversion/actions/workflows/python-ci.yml/badge.svg)](https://github.com/karanzaveri/Currency-Conversion/actions/workflows/python-ci.yml)

# Unit Tests
The unit tests has been done in 2 parts and is written using the unittest framework in Python.

[Unit Test 1](https://github.com/karanzaveri/Currency-Conversion/blob/main/test_main.py)
[Unit Test 2](https://github.com/karanzaveri/Currency-Conversion/blob/main/test_non_gui.py)

#### 1. TestRealTimeCurrencyConverter Class
* [TestRealTimeCurrencyConverter](https://github.com/karanzaveri/Currency-Conversion/blob/main/test_main.py#L4): This is a test case class that inherits from 'unittest.TestCase'. It contains test methods for the 'RealTimeCurrencyConverter' class.
###### test_main.py
* [test_get_exchange_rates](https://github.com/karanzaveri/Currency-Conversion/blob/main/test_main.py#L5): Checks if the 'get_exchange_rates' method of 'RealTimeCurrencyConverter' returns valid data.
* [test_convert](https://github.com/karanzaveri/Currency-Conversion/blob/main/test_main.py#L12): Checks if the 'convert' method of 'RealTimeCurrencyConverter' behaves as expected.
###### test_non_gui.py
* [test_get_exchange_rates](https://github.com/karanzaveri/Currency-Conversion/blob/main/test_non_gui.py#L5): Checks if the API request to obtain exchange rates for USD is successful and if the returned data contains the 'rates' key.
* [test_convert](https://github.com/karanzaveri/Currency-Conversion/blob/main/test_non_gui.py#L12): Tests the currency conversion functionality by converting 1 unit of USD to INR, ensuring that the result is not None and is of type float.

#### 2. TestCurrencyConverterApp Class
* [TestCurrencyConverterApp](https://github.com/karanzaveri/Currency-Conversion/blob/main/test_main.py#L19): This is another test case class for the 'CurrencyConverterApp' class.
* [setUp](https://github.com/karanzaveri/Currency-Conversion/blob/main/test_main.py#L20): A special method that is run before each test method. It creates instances of 'RealTimeCurrencyConverter' and 'CurrencyConverterApp'.
* [test_restrict_number_only](https://github.com/karanzaveri/Currency-Conversion/blob/main/test_main.py#L25): Checks the 'restrict_number_only' method of 'CurrencyConverterApp' for different input cases.

#### 3. Running Tests:
* The [main](https://github.com/karanzaveri/Currency-Conversion/blob/main/test_main.py#L37) block ensures that if the script is run directly (not imported as a module), the 'unittest.main()' function is called, which discovers and runs the tests.

![Result](https://github.com/karanzaveri/Currency-Conversion/blob/main/images/unittestresult.png)

# IDE
I have used Visual Studio Code IDE, mentioned below are my few favorite shortcuts:
* F5 : Run and Debug
* Ctrl + ] / Ctrl + [ : Indentation
* Ctrl + / : Comment/Uncomment code lines
* Ctrl + B : Show or hide the sidebar
* Ctrl + Shift + P : Open the command palette

# Functional Programming
In my Currency Conversion code, certain functional programming principles are applied. Here's how the code adheres to these principles:

1. Final Data Structures:
The 'data' attribute in [RealTimeCurrencyConverter](https://github.com/karanzaveri/Currency-Conversion/blob/main/currency_conversion.py#L11) is initialized with the final result of the API call ('response.json()'), representing exchange rates. It remains unmodified afterward.

2. Side-Effect-Free Functions:
The [get_exchange_rates](https://github.com/karanzaveri/Currency-Conversion/blob/main/currency_conversion.py#L16) function has no side effects, performing an HTTP GET request and returning the JSON response without modifying external state. The [convert](https://github.com/karanzaveri/Currency-Conversion/blob/main/currency_conversion.py#L25) method is also side-effect-free.

3. Higher-Order Functions:
The [requests.get](https://github.com/karanzaveri/Currency-Conversion/blob/main/currency_conversion.py#L18) function in 'get_exchange_rates' is a higher-order function, taking a URL as an argument and returning a function ('get') that performs an HTTP GET request.

4. Functions as Parameters and Return Values:
The 'convert' method takes parameters and returns a calculated value. Button widgets use functions like [perform_conversion](https://github.com/karanzaveri/Currency-Conversion/blob/main/currency_conversion.py#L112) and [show_transaction_history](https://github.com/karanzaveri/Currency-Conversion/blob/main/currency_conversion.py#L140) as parameters for the 'command' attribute.

5. Closures / Anonymous Functions:
While 'lambda' functions are not explicitly used, functions passed to the [command](https://github.com/karanzaveri/Currency-Conversion/blob/main/currency_conversion.py#L103) attribute of buttons can be considered as anonymous functions.

# Built Using
![python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

# Contact Me
[![gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:karanzaveri92@gmail.com)