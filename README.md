# Django Contacts Project

A web application for managing personal and professional contacts, built using Django.

## Features
- Add, edit, and delete contact information.
- Search contacts by name or other attributes.
- View detailed information about each contact.
- User authentication to secure access to contact data.

## Requirements
- Python 3.8+
- Django 4.x+
- SQLite (default) or any other supported database
- Optional: Bootstrap 5 for front-end styling

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-contacts.git
   cd django-contacts
2. Start the server:
   ```bash
   python manage.py runserver


### **Project Description:**
The Contact Management Website is a web application built using **Django** (backend framework), **SQLite** (database), and **Bootstrap** (frontend framework). It allows users to efficiently manage contacts by adding, updating, deleting, and searching for contact details.

---

### **Major Technical Decisions:**
1. **Framework Choice**:
   - **Django**: Chosen for its robust ORM, rapid development capabilities, and ease of handling CRUD operations.
   - **SQLite**: Lightweight, file-based database ideal for small to medium-sized applications.

2. **Frontend Design**:
   - **Bootstrap**: Used for responsive and clean UI components without needing extensive custom CSS.

3. **Separation of Concerns**:
   - Models handle data.
   - Views handle business logic.
   - Templates render the user interface.

---

### **How Each Part Works:**

#### **1. Models (Database Layer)**:
- The `UserModel` is used to define fields such as `first_name`, `last_name`, `email`, `phone_number`, `company`, and `job_title`.
- **How it works**:
  - Stores all user data in a structured format.
  - Facilitates easy querying, filtering, and manipulation of records.

#### **2. Views (Business Logic)**:
- **`user_list_create` View**:
  - Handles displaying a list of users.
  - Processes form submissions for adding new contacts.
  - Supports search functionality to filter contacts by name.
- **`delete_user` View**:
  - Retrieves a contact by ID and deletes it from the database.
- **`update_user` View**:
  - Retrieves a specific contact by ID, pre-populates its details in a form, and updates them upon submission.

#### **3. Templates (Presentation Layer)**:
- HTML templates with **Django Template Tags** dynamically render content, such as:
  - Listing all users with details.
  - Displaying forms for adding or updating contacts.
  - Showing search results in real time.
- **How it works**:
  - Template tags like `{% for user in users %}` are used to loop through user records.
  - Forms use `{% csrf_token %}` for secure POST requests.

#### **4. Static Files (CSS and JavaScript)**:
- **Bootstrap** ensures a responsive, user-friendly interface with components like tables, buttons, and form styling.

#### **5. Search Functionality**:
- The `search` parameter in the `GET` request is processed in the `user_list_create` view to filter contacts using case-insensitive matching.

#### **6. CRUD Operations**:
- **Create**: Users can add new contacts using a form.
- **Read**: A paginated list of all contacts is displayed.
- **Update**: Users can edit contact details via pre-filled forms.
- **Delete**: Users can remove unwanted contacts with a single click.

---

### **Key Features:**
1. Add and manage contact details.
2. Search functionality for quick access to specific contacts.
3. Simple and clean UI with responsive design.
4. Database operations are seamless with Django ORM.

Let me know if you need further elaboration! 😊
   
