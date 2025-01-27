## RestaurantDB - Relacyjna Baza Danych dla Restauracji 🍽️

📋 Opis projektu
**RestaurantDB** to projekt relacyjnej bazy danych stworzony w celu zarządzania operacjami restauracyjnymi. System obsługuje takie obszary, jak:
- Zarządzanie klientami, pracownikami, daniami i zamówieniami.
- Przechowywanie informacji o dostawcach i składnikach.
- Monitorowanie stanów magazynowych oraz analizy najczęściej zamawianych dań i kategorii.

Projekt został zaprojektowany w celu prezentacji zaawansowanych umiejętności SQL, takich jak:
- Tworzenie struktury bazy danych.
- Implementacja widoków, wyzwalaczy i procedur składowanych.
- Generowanie danych testowych i przeprowadzanie analiz biznesowych za pomocą zapytań SQL.

## 🛠️ Funkcjonalności
1. **Modelowanie danych**:
   - Tabele dla klientów, pracowników, dostawców, składników, dań i zamówień.
   - Relacje między tabelami z wykorzystaniem kluczy obcych.

2. **Automatyzacje**:
   - Wyzwalacze (triggers), które reagują na wstawianie, aktualizowanie i usuwanie danych.
   - Procedury składowane (stored procedures) dla ułatwienia operacji na danych.

3. **Analizy i widoki**:
   - Widok identyfikujący klientów z największymi wydatkami.
   - Widok pokazujący najczęściej zamawiane dania oraz kategorie.

4. **Zapytania SQL**:
   - Przykłady gotowych zapytań analitycznych i operacyjnych, np.:
     - Lista klientów, którzy dołączyli po konkretnej dacie.
     - Najczęściej zamawiane dania.
     - Obliczenie całkowitych wydatków na wynagrodzenia pracowników.

5. **Generowanie danych testowych**:
   - Wstawienie przykładowych rekordów do wszystkich tabel, umożliwiając łatwe testowanie i demonstrację funkcjonalności bazy.

📂 Struktura bazy danych
Baza danych składa się z następujących tabel:
- **Customers** - Przechowuje informacje o klientach, takie jak imię, nazwisko, e-mail i numer telefonu.
- **Employees** - Przechowuje dane pracowników, w tym stanowiska i wynagrodzenia.
- **Dishes** - Przechowuje informacje o daniach, w tym cenach, dostępnych sztukach i kategoriach.
- **Orders** - Rejestruje zamówienia klientów, powiązane z pracownikami i klientami.
- **OrderDetails** - Szczegóły zamówień, takie jak ilości i ceny jednostkowe.
- **Suppliers** - Informacje o dostawcach składników.
- **Ingredients** - Składniki używane w restauracji, powiązane z dostawcami.
- **Inventory** - Stan magazynowy składników.

🔍 Przykładowe zapytania
1. Klienci, którzy dołączyli po określonej dacie:
   ```sql
   SELECT FirstName, LastName, PhoneNumber
   FROM Customers
   WHERE JoinDate >= '2024-12-10';
   ```
2. Najczęściej zamawiane dania:
   ```sql
   SELECT DishName, SUM(Quantity) AS TotalOrders
   FROM OrderDetails
   JOIN Dishes ON OrderDetails.DishID = Dishes.DishID
   GROUP BY DishName
   ORDER BY TotalOrders DESC;
   ```
3. Obliczenie całkowitych wydatków na pracowników:
   ```sql
   SELECT SUM(Salary) AS TotalSalary
   FROM Employees;
   ```

🚀 Jak uruchomić projekt
1. **Stwórz bazę danych**:
   Uruchom plik `RestaurantDB.sql` w swojej ulubionej aplikacji do zarządzania bazami danych, np. SQL Server Management Studio (SSMS), MySQL Workbench lub Azure Data Studio.

2. **Wstaw dane testowe**:
   Kod automatycznie generuje dane testowe dla tabel. Dodatkowo możesz je modyfikować lub dodawać więcej danych.

3. **Testowanie zapytań i funkcji**:
   Użyj przykładowych zapytań zawartych w pliku, aby przetestować funkcjonalności bazy danych.

4. **Rozwijaj projekt**:
   Możesz rozszerzyć projekt, dodając nowe funkcjonalności lub zmieniając istniejące widoki i procedury.

💡 Przykładowe zastosowania
Ten projekt może być użyty jako:
- Przykład umiejętności SQL w portfolio.
- Podstawa dla systemu zarządzania restauracją w rzeczywistym projekcie.
- Narzędzie do nauki i eksperymentowania z SQL.

🛡️ Technologie
- SQL (Microsoft SQL Server, MySQL lub dowolny inny system zarządzania bazą danych obsługujący standard SQL).
- Opcjonalnie: środowiska takie jak SQL Server Management Studio, MySQL Workbench.

📈 Możliwości rozwoju
- Dodanie systemu zarządzania promocjami i rabatami.
- Rozszerzenie o moduł raportowania (np. dzienne/tygodniowe analizy zamówień).
- Wdrożenie bardziej zaawansowanych funkcji walidacji danych.

📝 Licencja
Ten projekt jest dostępny na licencji MIT – możesz go dowolnie wykorzystywać, modyfikować i udostępniać.




English Version 🌍

# RestaurantDB - Relational Database for a Restaurant 🍽️

## 📋 Project Description
**RestaurantDB** is a relational database project designed to manage various restaurant operations. The system supports areas such as:
- Managing customers, employees, dishes, and orders.
- Storing information about suppliers and ingredients.
- Monitoring inventory levels and analyzing the most popular dishes and categories.

This project is designed to demonstrate advanced SQL skills, including:
- Database schema design and relationships.
- Implementation of views, triggers, and stored procedures.
- Generating test data and performing business analyses using SQL queries.

## 🛠️ Features
1. **Data Modeling**:
   - Tables for customers, employees, suppliers, ingredients, dishes, and orders.
   - Relationships between tables using foreign keys.

2. **Automation**:
   - Triggers that respond to data insertion, updates, and deletion.
   - Stored procedures for simplifying data operations.

3. **Analysis and Views**:
   - A view identifying customers with the highest spending.
   - A view showing the most ordered dishes and categories.

4. **SQL Queries**:
   - Examples of analytical and operational queries, such as:
     - Listing customers who joined after a specific date.
     - Finding the most frequently ordered dishes.
     - Calculating total expenses on employee salaries.

5. **Test Data Generation**:
   - Prepopulated sample data for all tables, enabling easy testing and demonstration of the database functionality.

## 📂 Database Structure
The database consists of the following tables:
- **Customers** - Stores customer information such as first name, last name, email, and phone number.
- **Employees** - Stores employee data, including positions and salaries.
- **Dishes** - Stores information about dishes, including prices, available quantities, and categories.
- **Orders** - Records customer orders linked to employees and customers.
- **OrderDetails** - Stores order details, such as quantities and unit prices.
- **Suppliers** - Information about suppliers of ingredients.
- **Ingredients** - Ingredients used in the restaurant, linked to suppliers.
- **Inventory** - Tracks ingredient stock levels.

## 🔍 Example Queries
1. Customers who joined after a specific date:
   ```sql
   SELECT FirstName, LastName, PhoneNumber
   FROM Customers
   WHERE JoinDate >= '2024-12-10';
   ```
2. Most frequently ordered dishes:
   ```sql
   SELECT DishName, SUM(Quantity) AS TotalOrders
   FROM OrderDetails
   JOIN Dishes ON OrderDetails.DishID = Dishes.DishID
   GROUP BY DishName
   ORDER BY TotalOrders DESC;
   ```
3. Calculate total employee expenses:
   ```sql
   SELECT SUM(Salary) AS TotalSalary
   FROM Employees;
   ```

## 🚀 How to Run the Project
1. **Create the Database**:
   Run the `RestaurantDB.sql` file in your preferred database management application, such as SQL Server Management Studio (SSMS), MySQL Workbench, or Azure Data Studio.

2. **Insert Test Data**:
   The script automatically generates test data for all tables. You can modify or add additional data as needed.

3. **Test Queries and Features**:
   Use the provided sample queries to test the database functionality.

4. **Develop the Project Further**:
   Extend the project by adding new features or modifying existing views and stored procedures.

## 💡 Use Cases
This project can be used as:
- A demonstration of SQL skills in your portfolio.
- A foundation for a real-world restaurant management system.
- A learning tool for practicing and experimenting with SQL.

## 🛡️ Technologies
- SQL (Microsoft SQL Server, MySQL, or any other database management system supporting the SQL standard).
- Optional: tools like SQL Server Management Studio or MySQL Workbench.

## 📈 Future Enhancements
- Add a discount and promotions management system.
- Extend with a reporting module (e.g., daily/weekly order analyses).
- Implement more advanced data validation functions.

## 📝 License
This project is licensed under the MIT License – you are free to use, modify, and share it as you wish.



