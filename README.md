# Expense Tracker

A desktop expense tracking application built with PyQt6 that helps you monitor your spending with persistent storage.

## Features:
- Add expenses with amount, category, and description
- View all expenses in a formatted list
- Automatic total calculation
- Persistent storage using JSON
- Expenses automatically load when you reopen the app
- Error handling for invalid inputs
- Clean, color-coded interface

## How to use:
1. Install PyQt6: `pip install PyQt6`
2. Run `python expense-tracker.py`
3. Enter amount (e.g., 15.99)
4. Enter category (e.g., food, gas, entertainment)
5. Enter optional description
6. Click "Add Expense"
7. Your expenses are automatically saved!

## Example:
```
$5.99 - food - lunch at cafe
$20.00 - gas - gas station
$15.50 - entertainment - movie ticket
Total: $41.49
```

## How it works:
- Expenses stored as JSON in `expenses.json`
- Each expense contains amount, category, and description
- Total is recalculated with each addition
- Data persists across sessions

## What I learned:
- Working with dictionaries to store structured data
- JSON file handling for data persistence
- Formatting currency with Python
- Managing multiple related pieces of data
- Error handling with try/except
- Building a complete financial tracking application

Created: March 2026
