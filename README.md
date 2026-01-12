# Library Sequel

A practical learning project for SQL database operations with Python, featuring a virtual library management system built with CustomTkinter GUI framework.

## Overview

This repository is designed as a hands-on learning experience to practice SQL database operations alongside Python programming. The project implements a virtual library system where users can manage book lending operations through an intuitive graphical interface.

## Features

- **SQLite Database Integration**: Learn SQL operations (CREATE, INSERT, SELECT, UPDATE, DELETE) with a real database
- **Modern GUI**: Built with CustomTkinter for a clean, modern interface
- **Book Management**: Track books, customers, and lending status

## Technologies Used

- **Python 3.14**: Core programming language
- **SQLite3**: Lightweight database for data persistence
- **CustomTkinter**: Modern GUI framework for Python applications

## Database Schema

The application uses a simple `Books` table structure:

```sql
CREATE TABLE Books (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    book TEXT NOT NULL,
    status TEXT NOT NULL,
    date TEXT NOT NULL DEFAULT 'unknown'
);
```

## Getting Started

### Prerequisites

- Python 3.14 installed on your system
- CustomTkinter library

### Installation

1. Install required dependencies:
```bash
pip install customtkinter
```

2. Run the application:
```bash
python main.py
```

## Project Structure

```
├── main.py          # Main application file
├── library.db       # SQLite database file
└── README.md        # Project documentation
```
