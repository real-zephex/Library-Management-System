# Library Management System

A Library management should include all the basic functions that an actual library has, ranging from allowing users to borrow and returns books, view available books to allowing admins to update, add and remove books

The program should keep track of books which are being borrowed and increment/decrement the number of copies available properly. A suitable database should be used to make this task easier and practical. 

As for the admin, there should be an authentication system at place to validate the credentials. _a simple authentication system will just work fine, nothing sophisticated is required._

For the user, they should login with an user id of a given format and the program should make sure that the format is properly followed or not.

## Feature List

#### User
- [ ] Ability to login using user ids
- [ ] Ability to see available books
- [ ] Ability to borrow books
- [ ] Ability to return books

#### Admin
- [ ] All of the features from user
- [ ] Ability to add, update and manipulate the books or their info
- [ ] Ability to see which books are borrowed
- [ ] Ability to login via a hardcoded username and password

#### Optional Books
- [ ] Customer Service
	- [ ] Fine Calculation
	- [ ] Issues regarding returning of books etc.
- [ ] Search Option (search for a book etc)

## Database Design
#### Books.db

| ID | Book Name | Author Name | Date of Publication | Publisher | Number of copies |
| - | - | - | - | - | -|
| 1 | Book 1 | Author 1 | Some Date | ABC Publisher | n copies |
| 2 | Books 2 | Author 2 | Some Date 2 | XYZ Publisher | m copies |

#### Borrowed_books.db

| Recipient Name | Borrowed Books | Days left |
| - | - | - |
| Person 1 | Book 1 | 3 |
| Person 2 | Book 2 | 4 |


