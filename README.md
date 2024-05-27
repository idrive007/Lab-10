# Звіт з лабораторної роботи №10. Неповнота бібліотечного класу.
> Виконала студентка групи ІКМ-М223в **Павленко Дарина**
> 
### Мета: Рефакторінг коду з проблемою «Неповнота бібліотечного класу».

### Завдання 1: Наданий код

     class BasicCalculator:
        def add(self, a, b):
            return a + b

        def subtract(self, a, b):
            return a - b

        # Калькулятор не має методів для множення та ділення

    calculator = BasicCalculator()
    print("Addition: “ calculator.add(5,3))
    print("Subtraction: “ calculator.subtract(5,3))
    # print("Multiplication: ", calculator.multiply(5, 3)) # Не працює, метод не визначений 
    # print("Division: ", calculator.divide(5, 3)) # Не працює, метод не визначений

У наведеному коді клас BasicCalculator має лише базові методи додавання та віднімання, але не має методів для множення та ділення. Це обмежує його функціональність як калькулятора. Необхідно додати необхідні методи використовуючи підхід зі створенням підкласу.


### Рішення

      class BasicCalculator:
          def add(self, a, b):
              return a + b

          def subtract(self, a, b):
              return a - b

          # Калькулятор не має методів для множення та ділення

      class AdvancedCalculator(BasicCalculator):
          def multiply(self, a, b):
              return a * b

          def divide(self, a, b):
              if b == 0:
                  raise ValueError("Division by zero is not allowed")
              return a / b
  
      # Використання підкласу
      calculator = AdvancedCalculator()
      print("Addition: ", calculator.add(5, 3))
      print("Subtraction: ", calculator.subtract(5, 3))
      print("Multiplication: ", calculator.multiply(5, 3))
      print("Division: ", calculator.divide(5, 3))

Отже, було створено підклас AdvancedCalculator, який успадковує від BasicCalculator і додає методи для множення та ділення.
Екземпляр класу AdvancedCalculator використовується для виконання всіх чотирьох операцій: додавання, віднімання, множення та ділення.
Таким чином, було розширено функціональність базового калькулятора, новим класом, що додає необхідні методи.


### Завдання 2: Наданий код

    class LibraryBook:
        def __init__(self, title, author, publication_year):
            self.title = title
            self.author = author
            self.publication_year = publication_year
            self.is_checked_out = False

        def check_out(self):
            if not self.is_checked_out:
                self.is_checked_out = True
                return True
             return False
    
        def return_book(self):
            if self.is_checked_out:
                self.is_checked_out = False
                return True
             return False

    # Використання коду
    book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald",1925)
    print(book.check_out())
    print(book.check_out())

У даному коді клас LibraryBook надає базові функції перевірки наявності книги в бібліотеці та її повернення. Проте відсутні методи, які можуть бути корисні для повної роботи з бібліотечною книгою, такі як перевірка стану книги, отримання інформації про книгу тощо. Необхідно додати функціональність використовуючи делегування.

### Рішення

Щоб додати функціональність до класу LibraryBook за допомогою делегування, ми можемо створити додатковий клас LibraryBookInfo, який міститиме додаткові методи, і використовувати його в класі LibraryBook. Це дозволить розширити функціонал, не змінюючи існуючий клас LibraryBook.

    class LibraryBook:
        def __init__(self, title, author, publication_year):
            self.title = title
            self.author = author
            self.publication_year = publication_year
            self.is_checked_out = False

        def check_out(self):
            if not self.is_checked_out:
                self.is_checked_out = True
                return True
            return False

        def return_book(self):
            if self.is_checked_out:
                self.is_checked_out = False
                return True
            return False

    class LibraryBookInfo:
        def __init__(self, library_book):
            self.library_book = library_book

        def get_book_info(self):
            return {
                "Title": self.library_book.title,
                "Author": self.library_book.author,
                "Publication Year": self.library_book.publication_year,
                "Checked Out": self.library_book.is_checked_out
            }

        def check_book_condition(self):
       
            return "Good"  

    book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book_info = LibraryBookInfo(book)

    print(book.check_out())
    print(book.check_out())
    print(book.return_book())
    print(book.return_book())
    print(book_info.get_book_info())
    print(book_info.check_book_condition())

Отже, було створено клас LibraryBookInfo, який отримує екземпляр LibraryBook і надає додаткові методи для отримання інформації про книгу та перевірки її стану.
Використовується делегування для додавання нової функціональності без змін у базовому класі.
