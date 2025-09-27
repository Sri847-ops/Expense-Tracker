# Expense Tracker

A modern, responsive web application built with Flask and SQLite for tracking personal expenses with beautiful charts and analytics.

## Features

- ✅ Add, view, and delete expenses
- ✅ Categorize expenses (Food, Travel, Entertainment, Bills, etc.)
- ✅ Interactive charts and reports
- ✅ Responsive design with modern UI
- ✅ Real-time total calculations
- ✅ Form validation and error handling
- ✅ Beautiful gradient design

## Installation

1. Clone or download this repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and go to `http://localhost:5000`

## Usage

1. **Add Expenses**: Click "Add Expense" to add new expenses with title, amount, category, and date
2. **View All Expenses**: The home page shows all expenses in a table with total amount
3. **Delete Expenses**: Click the delete button to remove expenses (with confirmation)
4. **View Reports**: Click "Report" to see expense breakdown by category with interactive charts

## Database

The application uses SQLite database (`expenses.db`) which is automatically created when you first run the app. The database contains a single table `expenses` with the following structure:

- `id`: Primary key (auto-increment)
- `title`: Expense title/description
- `amount`: Expense amount (decimal)
- `category`: Expense category
- `date`: Expense date (YYYY-MM-DD format)

## Technologies Used

- **Backend**: Python Flask
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5
- **Charts**: Chart.js
- **Icons**: Bootstrap Icons

## Features in Detail

### Modern UI/UX
- Gradient backgrounds and modern card design
- Responsive layout that works on all devices
- Smooth animations and hover effects
- Professional color scheme

### Data Management
- Form validation with user-friendly error messages
- Confirmation dialogs for destructive actions
- Auto-dismissing success/error alerts
- Real-time total calculations

### Charts and Analytics
- Interactive doughnut charts showing expense distribution
- Category breakdown with amounts and percentages
- Responsive chart design
- Professional chart styling

## Customization

You can easily customize the application by:

1. **Adding new categories**: Edit the category options in `templates/add.html`
2. **Changing colors**: Modify the CSS variables in `static/style.css`
3. **Adding new features**: Extend the Flask routes in `app.py`

## License

This project is open source and available under the MIT License.
