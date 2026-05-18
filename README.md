# 🧮 Smart Calculator

A simple yet powerful command-line calculator written in Python. Built at the **Junior+** level with clean code, error handling, and calculation history.

---

## ✨ Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division (with division-by-zero protection)
- 🔢 Exponentiation (`**`)
- 〽️ Modulo (`%`)
- 📜 Calculation history
- ❗ Input error handling

---

## 🚀 Getting Started

### Requirements

- Python 3.x

### Run the calculator

```bash
python calculator.py
```

---

## 🖥️ Usage

```
=== Smart Calculator ===

Available operations:
+  Addition
-  Subtraction
*  Multiplication
/  Division
** Exponentiation
%  Modulo
history - Show History
exit    - Quit

Enter operation: +
Enter first number: 10
Enter second number: 5
Result: 15.0
```

### Show history

Type `history` to see all previous calculations:

```
Enter operation: history

=== Calculation History ===
10.0 + 5.0 = 15.0
8.0 * 3.0 = 24.0
```

### Exit

Type `exit` to quit the program.

---

## 🛡️ Error Handling

| Situation | Response |
|---|---|
| Invalid operation entered | `Error: unknown operation` |
| Non-numeric input | `Error: please enter numbers only!` |
| Division by zero | `Error: division by zero!` |

---

## 📁 Project Structure

```
📦 smart-calculator
 ┗ 📜 calculator.py
 ┗ 📜 README.md
```

---

## 👤 Author

Made with ❤️ and Python.

---

## 📄 License

This project is open source and free to use.
