# Library Sequel

A practical learning project focused on studying SQL database operations with Python through a simple virtual library management system.

## Overview

This repository is a **learning project** designed to practice SQL operations in a hands-on way using Python. The main goal was to understand how SQL works in real-world scenarios by building a functional library management system.

## Project Purpose

- **Primary Focus**: Practical study of SQL database operations
- **Secondary Focus**: Integration of SQL with Python programming
- **Learning Approach**: Hands-on experience with real database scenarios

## Why the Simple Interface?

The graphical interface is deliberately basic because **the main focus of this project is SQL**, not UI design. The simple interface allows for:

- Clear focus on database operations
- Easy understanding of SQL query results
- Minimal distractions from the core learning objectives
- Quick implementation to spend more time on SQL practice

## Technologies Used

- **Python 3.14**: Programming language for application logic
- **SQLite3**: Database engine for practicing SQL operations
- **CustomTkinter**: Basic GUI framework

## Database Schema

### Books Table
```sql
CREATE TABLE "books" (
    "book_id"       INTEGER NOT NULL UNIQUE,
    "book_name"     TEXT NOT NULL,
    PRIMARY KEY("book_id")
);
```

### Customers Table
```sql
CREATE TABLE "customers" (
    "customer_id"   INTEGER NOT NULL UNIQUE,
    "book_id"       INTEGER NOT NULL UNIQUE,
    "first_name"    TEXT NOT NULL,
    "last_name"     TEXT NOT NULL,
    "email_address" TEXT NOT NULL,
    "status"        INTEGER NOT NULL,
    PRIMARY KEY("customer_id" AUTOINCREMENT),
    FOREIGN KEY("book_id") REFERENCES "books"("book_id")
);
```

## SQL Operations Practiced

This project covers essential SQL operations:

- **CREATE TABLE**: Database schema design
- **INSERT**: Adding new records
- **SELECT**: Querying and filtering data
- **UPDATE**: Modifying existing records
- **DELETE**: Removing records
- **COUNT**: Aggregate functions
- **WHERE clauses**: Conditional queries

## Getting Started

### Prerequisites

- Python 3.14
- CustomTkinter library

### Installation

1. Install dependencies:
```bash
pip install customtkinter
```
2. Run the application:
```bash
python main.py
```

## Project Structure

```
├── main.py          # Main application with SQL operations
├── library.db       # SQLite database file
└── README.md        # Project documentation
```