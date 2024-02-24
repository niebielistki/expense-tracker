## Expense Tracker 

### Overview

Expense Tracker Pro is a web application designed to help users meticulously manage and analyze their personal finances. 
Built with **Django**, the application offers a robust platform for tracking expenses, categorizing them, and generating insightful summaries. 
It stands out for its user-friendly interface, detailed expense categorization, and powerful search and summarization capabilities.

### Features

* **Expense Management:** 
Users can add, edit, and delete expenses, capturing details such as the expense category, amount, and date.
* **Category Management:** Provides the ability to create, update, and delete categories for organizing expenses effectively.ization.
* **Advanced Filtering:** Expenses can be filtered by date ranges, categories, or both, allowing users to easily locate specific transactions.ly what you're looking for. 
* **Sorting and Summarization:** Features include sorting expenses by date or category and generating summaries of expenses per category and per year-month.r easy viewing.
* **Responsive Design:** The application is fully responsive, ensuring a seamless user experience across various devices and screen sizes.bits at a glance.


### Technologies Used

* **Backend:** Django (Python)
* **Database:** SQLite
* **Frontend:** HTML, CSS (Bootstrap for potential future enhancements)

### Getting Started

#### Prerequisites:

- Python 3.x
- Django 3.x

#### Installation:

**1.** Clone the repository:

`git clone https://github.com/niebielistki/expense-tracker.git`

**2.** Navigate to the project directory:

`cd expense-tracker`

**3.** Install the requirements:

`pip install -r requirements.txt`

**4.** Run the migrations:

`python manage.py migrate`

**5.** Load the initial data:

`python manage.py loaddata fixtures.json`

**6.** Start the development server:

`python manage.py runserver`


#### Usage:

After setting up the project, you can start tracking your expenses by creating categories and adding expenses under these categories. Use the search and filter functionalities to review your expenses based on specific criteria such as date ranges and categories.

**For a demonstration of the program in action, watch this video:**

### Future Enhancements

* **Dashboard:** A dashboard for visualizing expenses with charts and graphs for a quick financial overview.
* **API Development:** Developing a RESTful API for integration with other applications and services.

### Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.