# Bank Accounts

Today's Focus is object-oriented design. We will be working with the concept of bank accounts in order to explore more object-oriented code as well as a few other new topics.

## Part 1

### Learning Goals
- Create a **class** 
- Create **methods** inside the **class** to perform actions
- Learn how Python does error handling

### Requirements

1. Create a `Bank` class which will contain your `Account` class and any future bank account logic.
2. Create an `Account` class which should have the following functionality:
  - A new account should be created with an `ID` and an initial `balance`
  - Should have a `withdraw` method that accepts a single parameter which represents the amount of money that will be withdrawn. This method should return the updated account balance.
  - Should have a `deposit` method that accepts a single parameter which represents the amount of money that will be deposited. This method should return the updated account balance.
  - Should be able to access the current `balance` of an account at any time.

### Error handling

- A new account cannot be created with initial negative balance - this should `raise` an `Exception` (leverage those Googling skills!)
- The `withdraw` method does not allow the account to go negative - it should output a warning message and return the original un-modified balance

### Optional:
- Create an `Owner` class which will store information about those who own the `Accounts`.
  - This should have info like name and address and any other identifying information that an account owner would have.
- Add an `owner` property to each Account to track information about who owns the account.
  - The `Account` can be created with an `owner`, OR you can create a method that will add the `owner` after the `Account` has already been created.


## Part 2

### Learning Goals
- Create and use class methods
- Use a CSV file for loading data

### Requirements
- Update the `Account` class to be able to handle all of these fields from the CSV file used as input.
  - For example, manually choose the data from the first line of the CSV file and ensure you can create a new instance of your Account using that data
- Add the following **class** methods to your existing `Account` class
  - `.all_accounts` - returns a collection of `Account` instances, representing all of the Accounts described in the CSV. See below for the CSV file specifications
  - `.find(id)` - returns an instance of `Account` where the value of the id field in the CSV matches the passed parameter


### CSV Data File

**Bank::Account**

The data, in order in the CSV, consists of:
- **ID** - (Integer) a unique identifier for that Account
- **Balance** - (Integer) the account balance amount, in cents (i.e., 150 would be $1.50)
- **OpenDate** - (Datetime) when the account was opened

**Bank::Owner**

The data, in order in the CSV, consists of:
  - **ID** - (Integer) a unique identifier for that Owner
  - **Last Name** - (String) the owner's last name
  - **First Name** - (String) the owner's first name
  - **Street Addess** - (String) the owner's street address
  - **City** - (String) the owner's city
  - **State** - (String) the owner's state

To create the relationship between the accounts and the owners use the `account_owners` CSV file.

The data for this file, in order in the CSV, consists of:
  - **Account ID** - (Integer) a unique identifier corresponding to an account
  - **Owner ID** - (Integer) a unique identifier corresponding to an owner

## Part 3
### Learning Goals
- Use inheritance to share some behavior across classes
- Enhance functionality built in Wave 1

### Requirements
Create a `SavingsAccount` class which should inherit behavior from the `Account` class. It should include the following updated functionality:

- The initial balance cannot be less than $10. If it is, this will `raise` an `ArgumentError`
- Updated withdrawal functionality:
  - Each withdrawal 'transaction' incurs a fee of $2 that is taken out of the balance.
  - Does not allow the account to go below the $10 minimum balance - Will output a warning message and return the original un-modified balance

It should include the following new method:
- `add_interest(rate)`: Calculate the interest on the balance and add the interest to the balance. Return the **interest** that was calculated and added to the balance (not the updated balance).

  - Input rate is assumed to be a percentage (i.e. 0.25).
  - The formula for calculating interest is `balance * rate/100`
    - Example: If the interest rate is 0.25% and the balance is $10,000, then the interest that is returned is $25 and the new balance becomes $10,025.

Create a `CheckingAccount` class which should inherit behavior from the `Account` class. It should include the following updated functionality:

- Updated withdrawal functionality:
  - Each withdrawal 'transaction' incurs a fee of $1 that is taken out of the balance. Returns the updated account balance.
    - Does not allow the account to go negative. Will output a warning message and return the original un-modified balance.
- `withdraw_using_check(amount)`: The input amount gets taken out of the account as a result of a check withdrawal. Returns the updated account balance.
  - Allows the account to go into overdraft up to -$10 but not any lower
  - The user is allowed three free check uses in one month, but any subsequent use adds a $2 transaction fee
- `reset_checks()`: Resets the number of checks used to zero


### Optional:

Create a `MoneyMarketAccount` class which should inherit behavior from the `Account` class.

- A maximum of 6 transactions (deposits or withdrawals) are allowed per month on this account type
- The initial balance cannot be less than $10,000 - this will `raise` an `ArgumentError`
- Updated withdrawal logic:
  - If a withdrawal causes the balance to go below $10,000, a fee of $100 is imposed and no more transactions are allowed until the balance is increased using a deposit transaction.
  - Each transaction will be counted against the maximum number of transactions
- Updated deposit logic:
  - Each transaction will be counted against the maximum number of transactions
  - Exception to the above: A deposit performed to reach or exceed the minimum balance of $10,000 is not counted as part of the 6 transactions.
- `add_interest(rate)`: Calculate the interest on the balance and add the interest to the balance. Return the interest that was calculated and added to the balance (not the updated balance).
    - **Note** This is the same as the `SavingsAccount` interest.
- `reset_transactions`: Resets the number of transactions to zero
