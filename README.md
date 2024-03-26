# [NEW!] Guild App - Mastery Chain Links
#### Video Demo:  <URL HERE>
## Description:
This application is made for the the [NEW!] Guild Members who are playing a 25 year old Ultima Online video game!

The purpose of this application is to maintain a list of "Mastery Chain Links" (in game items) owned by the guild and to allow the guild leaders (admins) to allow guild members (users) to select Links for distribution.

## Registration Page
- Users can register an account
  - Users can register by supplying a username, display name and password. The password must be confirmed
  - Password security requires a minimum of 8 characters including a number, symbol, lower and uppercase letters

## Login Page
- Users with existing username/pass have the ability to login 

### Logout
- Logs user out

## Home Page
- Displays Instructions

## Mastery Chain Link Availability Page
- Users have the ability to view available Mastery Chain Links
- Users can also user the search bar to filter results by text input(name, quality or prices for example)

## Mastery Chain Link Selection Page
- Users have the ability to add Mastery Chain Links by selecting name and quality by dropdown and inputing an amount for quantity
- Users can also view their resulting selections and edit the quality or quantity.
- Users may also delete their selections

### Functions on this page:
- Reset Your Selections
	- Wipes all records of that user's selections in the selection table in order to start over.
- Lock Selections Toggle
	- Toggles selection status. When locked, user cannot add any more selections and displays to admins on admin selection page that user has completed their selections. Otherwise when open, can keep adding selections.

## User Page
- Users have the ability to view and edit user info including username, display name, password
	- Old password is required and new password must be confirmed and adhere to password requirements

## Admin Page - User Management
- Admins have the ability to view, add, delete or edit users including username, display name, password (without restrictions) and user level
	- User levels: 
	```
	0 - Regular User
	1 - Low Admin
	2 - High Admin
	3 - Main Admin
	```

## Admin Page - Link Management
- Admins have the ability to view, add, delete or edit mastery chain links including name, quality, quantity, market price and guild price
- Admins can export a the current mastery chain link list as a csv.
	- Admins can also upload a properly formatted (based on export format) csv list to update many links at once by matching name and quality
	
## Admin Page - Link Selections
- Admins have the ability to view, add, delete or edit user's selections of mastery chain links including quality and quantity
### Functions on this page:
- Toggle Mastery Link Selections
	- Activates/Deactivates ability to select links on the Mastery Chain Link Selection Page
- Reset All Users' Selections
	- Clears selection table in database and wipes all user's selections
- TESTING: Assign Links
	- Same as the Assign Links function, but does not wipe all user's selections for testing purposes. 
- Assign Links
	- Takes all users who have made selections, randomizes their order, goes through each selection of theirs and checks for availability. If available assigns those links to that user and creates a record in a delivery table. If not available, skips and checks next selection. Does this for every user in the randomized order untill all selections are checked. Once complete wipes the records from the selection table

## Admin Page - Link Delivery
- Admins have the ability to view and deliver user's assigned selections of mastery chain links

### Functions on this page:
- TESTING: Erase Delivery Selections
	- For testing purposes, wipes all records in the delivery table
- Deliver
	- When selected by an admin, will confirm links have been delivered in game and will remove these records from the delivery table and copy them to the history table also including datetime and which admin completed the delivery
	- Will also subtract that amount from the Mastery Chain Link list (the mclinks table in the database)
- TESTING: Deliver
  - Will do the same function as deliver but will not wipe the user's delivery records or subtract from the mclinks table
  
## Admin Page - Delivery History
- Admins have the ability to view and deliver user's assigned selections of mastery chain links

### Functions on this page:
- TESTING: Erase All History
	- For testing purposes, wipes all records in the history table
	
## User Levels

### Main Admin
```
- Pages
	- All Pages
- Functions
	- All Functions including testing functions
```

### High Admin
```
- Pages
	- All Pages
- Functions
	- All Functions excluding testing functions
```

### Low Admin
```
- Pages
	- All Pages except for:
	- User Management
	- Link Management
	- Link Selections
- Functions
	- Can use Deliver function on Delivery Page
```

### Regular User
```
- Pages
	- All Pages except for Admin Pages
```

:shipit:

#### Notes:
- This project will be updated in the future as we will host it online for our guild members and include more features based on guild management
- All prices and quanities are based on video game items and currencies. No real items or currencies are used!




