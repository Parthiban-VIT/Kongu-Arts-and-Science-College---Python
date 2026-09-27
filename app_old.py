
import streamlit as st
import math
import cmath
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Python Practical Lab",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)

PROGRAMS = [
    "1. Sum & Average",
    "2. Armstrong Numbers",
    "3. Matrix Multiplication",
    "4. Variance & Standard Deviation",
    "5. Fibonacci Sequence",
    "6. Factorial",
    "7. Count Vowels",
    "8. Pie Chart",
    "9. Student Grade",
    "10. Quadratic Equation",
]

INFO = {
    "1. Sum & Average": {
        "aim": "To calculate the sum and average of two numbers, including an integer and a decimal number.",
        "concept": "The sum is obtained by addition. The average of n values is their sum divided by n.",
        "formula": "Average = Sum / Number of values",
        "topics": "Variables, input, arithmetic operators, type conversion, formatted output.",
    },
    "2. Armstrong Numbers": {
        "aim": "To generate Armstrong numbers within a user-specified interval.",
        "concept": "A number is an Armstrong number if the sum of its digits, each raised to the number of digits, equals the number itself.",
        "formula": "For a k-digit number n = d1d2...dk: n = d1^k + d2^k + ... + dk^k",
        "topics": "Loops, modulo, integer division, strings, functions.",
    },
    "3. Matrix Multiplication": {
        "aim": "To multiply two matrices when their dimensions are compatible.",
        "concept": "If A is m×n and B is n×p, then AB is an m×p matrix. Each entry is the dot product of a row of A and a column of B.",
        "formula": "Cij = Σ Aik Bkj",
        "topics": "Nested loops, lists, matrices, dimension checking.",
    },
    "4. Variance & Standard Deviation": {
        "aim": "To calculate the variance and standard deviation of a data set.",
        "concept": "Variance measures the average squared deviation from the mean. Standard deviation is the positive square root of variance.",
        "formula": "Population variance = Σ(x − x̄)² / N;  Standard deviation = √variance",
        "topics": "Lists, mean, loops/list comprehensions, arithmetic, square root.",
    },
    "5. Fibonacci Sequence": {
        "aim": "To display the first n terms of the Fibonacci sequence.",
        "concept": "Starting with 0 and 1, each new term is the sum of the previous two terms.",
        "formula": "Fn = F(n−1) + F(n−2)",
        "topics": "Loops, variables, sequence generation.",
    },
    "6. Factorial": {
        "aim": "To find the factorial of a given non-negative integer.",
        "concept": "The factorial of n is the product of all positive integers from 1 to n. By definition, 0! = 1.",
        "formula": "n! = n(n−1)(n−2)...2·1",
        "topics": "Loops, multiplication, validation, functions.",
    },
    "7. Count Vowels": {
        "aim": "To count the number of vowels present in a string.",
        "concept": "Each character is examined and counted if it belongs to the set of vowels a, e, i, o, u.",
        "formula": "No mathematical formula is required.",
        "topics": "Strings, loops, membership operator, conditional statements.",
    },
    "8. Pie Chart": {
        "aim": "To represent categorical data using a pie chart.",
        "concept": "A pie chart divides a circle into sectors. Each sector represents the proportion of a category.",
        "formula": "Sector angle = (Category value / Total) × 360°",
        "topics": "Lists, dictionaries, Matplotlib, data visualization.",
    },
    "9. Student Grade": {
        "aim": "To calculate a student's grade from the marks obtained.",
        "concept": "An if-elif-else structure compares the mark with grade boundaries and assigns a corresponding grade.",
        "formula": "The grade is determined by the mark interval.",
        "topics": "Conditional statements, comparison operators, user input.",
    },
    "10. Quadratic Equation": {
        "aim": "To solve a quadratic equation ax² + bx + c = 0.",
        "concept": "The discriminant determines the nature of the roots. This app also handles complex roots.",
        "formula": "D = b² − 4ac;  x = (−b ± √D) / (2a)",
        "topics": "Functions, discriminant, square root, complex numbers, conditionals.",
    },
}

CODE = {
"1. Sum & Average": """# Sum and average of an integer and a decimal number

integer_num = int(input("Enter an integer: "))
decimal_num = float(input("Enter a decimal number: "))

total = integer_num + decimal_num
average = total / 2

print("Sum =", total)
print("Average =", average)
""",
"2. Armstrong Numbers": """# Generate Armstrong numbers in an interval

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Armstrong numbers:")

for number in range(start, end + 1):
    digits = str(number)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)

    if total == number:
        print(number, end=" ")
""",
"3. Matrix Multiplication": """# Matrix multiplication using nested loops

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

rows_A = len(A)
cols_A = len(A[0])
rows_B = len(B)
cols_B = len(B[0])

if cols_A != rows_B:
    print("Matrix multiplication is not possible.")
else:
    C = [[0] * cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    print("Product matrix:")
    for row in C:
        print(row)
""",
"4. Variance & Standard Deviation": """# Population variance and standard deviation

data = [10, 12, 15, 18, 20]

mean = sum(data) / len(data)

variance = sum((x - mean) ** 2 for x in data) / len(data)
standard_deviation = variance ** 0.5

print("Mean =", mean)
print("Variance =", variance)
print("Standard deviation =", standard_deviation)
""",
"5. Fibonacci Sequence": """# Display the first n Fibonacci numbers

n = int(input("Enter the number of terms: "))

a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
""",
"6. Factorial": """# Factorial of a given number

n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    print(n, "! =", factorial)
""",
"7. Count Vowels": """# Count vowels in a string

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for character in text:
    if character in vowels:
        count += 1

print("Number of vowels =", count)
""",
"8. Pie Chart": """# Create a pie chart using Matplotlib

import matplotlib.pyplot as plt

labels = ["Mathematics", "Physics", "Chemistry", "Computer Science"]
values = [30, 25, 20, 25]

plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.title("Subject-wise Distribution")
plt.show()
""",
"9. Student Grade": """# Calculate a student's grade

mark = float(input("Enter the mark (0-100): "))

if mark < 0 or mark > 100:
    print("Invalid mark.")
elif mark >= 90:
    print("Grade: A+")
elif mark >= 80:
    print("Grade: A")
elif mark >= 70:
    print("Grade: B")
elif mark >= 60:
    print("Grade: C")
elif mark >= 50:
    print("Grade: D")
else:
    print("Grade: F")
""",
"10. Quadratic Equation": """# Solve ax^2 + bx + c = 0

import cmath

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    print("This is not a quadratic equation.")
else:
    discriminant = b**2 - 4*a*c

    x1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    x2 = (-b - cmath.sqrt(discriminant)) / (2*a)

    print("Discriminant =", discriminant)
    print("Root 1 =", x1)
    print("Root 2 =", x2)
""",
}

def parse_matrix(text):
    rows = []
    for line in text.strip().splitlines():
        if not line.strip():
            continue
        try:
            row = [float(x) for x in line.replace(",", " ").split()]
        except ValueError:
            raise ValueError("Use only numbers separated by spaces or commas.")
        rows.append(row)
    if not rows:
        raise ValueError("Enter at least one row.")
    if len({len(r) for r in rows}) != 1:
        raise ValueError("All rows must have the same number of entries.")
    return rows

def fmt(x):
    if abs(x - round(x)) < 1e-10:
        return str(int(round(x)))
    return f"{x:.4g}"

st.markdown("""
<style>
.main-title {font-size: 2.5rem; font-weight: 800; margin-bottom: .1rem;}
.subtitle {font-size: 1.05rem; color: #666; margin-bottom: 1.2rem;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🐍 Python Practical Lab</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Interactive practical programmes for undergraduate Mathematics students — learn, run, modify, and explore.</div>',
    unsafe_allow_html=True
)

with st.sidebar:
    st.header("📚 Practical Programmes")
    selected = st.radio("Choose a programme", PROGRAMS)
    st.divider()
    st.caption("Explore → change inputs → observe output → modify the Python code.")

info = INFO[selected]

tab1, tab2, tab3 = st.tabs(["📖 Learn", "▶️ Explore", "💻 Python Code"])

with tab1:
    st.subheader("Aim")
    st.write(info["aim"])
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Concept**")
        st.write(info["concept"])
    with c2:
        st.markdown("**Formula / Key idea**")
        st.info(info["formula"])
    st.markdown("**Python topics used**")
    st.success(info["topics"])
    st.markdown("### Suggested learning cycle")
    st.write("**Understand → Change the input → Run → Observe → Predict → Modify the code**")

with tab2:
    if selected == "1. Sum & Average":
        st.subheader("Interactive Calculator")
        c1, c2 = st.columns(2)
        integer_num = c1.number_input("Integer", value=10, step=1)
        decimal_num = c2.number_input("Decimal number", value=5.5, step=0.5, format="%.2f")
        total = integer_num + decimal_num
        average = total / 2
        m1, m2 = st.columns(2)
        m1.metric("Sum", f"{total:g}")
        m2.metric("Average", f"{average:g}")

    elif selected == "2. Armstrong Numbers":
        st.subheader("Explore an Interval")
        c1, c2 = st.columns(2)
        start = c1.number_input("Start", value=1, min_value=0, step=1)
        end = c2.number_input("End", value=1000, min_value=0, step=1)
        if end < start:
            st.error("End must be greater than or equal to start.")
        elif end - start > 100000:
            st.warning("Please keep the interval within 100,000 numbers.")
        else:
            ans = []
            for number in range(int(start), int(end) + 1):
                s = str(number)
                if sum(int(d) ** len(s) for d in s) == number:
                    ans.append(number)
            st.metric("Armstrong numbers found", len(ans))
            st.write(ans if ans else "None in this interval.")

    elif selected == "3. Matrix Multiplication":
        st.subheader("Matrix Multiplication Explorer")
        st.caption("Enter one row per line; separate entries with spaces or commas.")
        c1, c2 = st.columns(2)
        A_text = c1.text_area("Matrix A", "1 2\n3 4", height=120)
        B_text = c2.text_area("Matrix B", "5 6\n7 8", height=120)
        if st.button("Multiply Matrices"):
            try:
                A = parse_matrix(A_text)
                B = parse_matrix(B_text)
                if len(A[0]) != len(B):
                    st.error(f"Not possible: A has {len(A[0])} columns but B has {len(B)} rows.")
                else:
                    C = [[sum(A[i][k] * B[k][j] for k in range(len(B)))
                          for j in range(len(B[0]))] for i in range(len(A))]
                    st.success(f"Result dimensions: {len(C)} × {len(C[0])}")
                    st.table([[fmt(x) for x in row] for row in C])
            except ValueError as e:
                st.error(str(e))

    elif selected == "4. Variance & Standard Deviation":
        st.subheader("Data Set Explorer")
        text = st.text_input("Enter data values separated by commas", "10, 12, 15, 18, 20")
        try:
            data = [float(x.strip()) for x in text.split(",") if x.strip()]
            if not data:
                raise ValueError
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            sd = math.sqrt(variance)
            c1, c2, c3 = st.columns(3)
            c1.metric("Mean", f"{mean:.4f}")
            c2.metric("Population variance", f"{variance:.4f}")
            c3.metric("Standard deviation", f"{sd:.4f}")
        except ValueError:
            st.error("Please enter valid comma-separated numbers.")

    elif selected == "5. Fibonacci Sequence":
        st.subheader("Fibonacci Explorer")
        n = st.slider("Number of terms", 1, 50, 10)
        seq, a, b = [], 0, 1
        for _ in range(n):
            seq.append(a)
            a, b = b, a + b
        st.write(seq)
        fig, ax = plt.subplots()
        ax.plot(range(1, n + 1), seq, marker="o")
        ax.set_xlabel("Term number")
        ax.set_ylabel("Fibonacci value")
        ax.set_title("Fibonacci Sequence")
        ax.grid(True, alpha=0.25)
        st.pyplot(fig)

    elif selected == "6. Factorial":
        st.subheader("Factorial Explorer")
        n = st.number_input("Enter n", min_value=0, max_value=100, value=5, step=1)
        n = int(n)
        result = math.factorial(n)
        st.metric(f"{n}!", f"{result:,}")
        st.write("0! = 1" if n == 0 else f"{n}! = " + " × ".join(str(i) for i in range(n, 0, -1)))

    elif selected == "7. Count Vowels":
        st.subheader("String Explorer")
        text = st.text_input("Enter a string", "Mathematics is beautiful")
        counts = {v: text.lower().count(v) for v in "aeiou"}
        st.metric("Total vowels", sum(counts.values()))
        st.write("Counts by vowel:", counts)

    elif selected == "8. Pie Chart":
        st.subheader("Create Your Own Pie Chart")
        labels_text = st.text_input("Labels (comma-separated)", "Mathematics, Physics, Chemistry, Computer Science")
        values_text = st.text_input("Values (comma-separated)", "30, 25, 20, 25")
        try:
            labels = [x.strip() for x in labels_text.split(",") if x.strip()]
            values = [float(x.strip()) for x in values_text.split(",") if x.strip()]
            if len(labels) != len(values):
                st.error("The number of labels and values must be the same.")
            elif not labels or any(v < 0 for v in values) or sum(values) == 0:
                st.error("Enter non-negative values with a non-zero total.")
            else:
                fig, ax = plt.subplots()
                ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
                ax.set_title("Category Distribution")
                st.pyplot(fig)
        except ValueError:
            st.error("Please enter valid numerical values.")

    elif selected == "9. Student Grade":
        st.subheader("Grade Calculator")
        mark = st.slider("Mark", 0.0, 100.0, 82.0, 0.5)
        if mark >= 90:
            grade = "A+"
        elif mark >= 80:
            grade = "A"
        elif mark >= 70:
            grade = "B"
        elif mark >= 60:
            grade = "C"
        elif mark >= 50:
            grade = "D"
        else:
            grade = "F"
        st.metric("Grade", grade)
        st.progress(mark / 100)
        st.caption("A+ ≥ 90, A ≥ 80, B ≥ 70, C ≥ 60, D ≥ 50, F < 50.")

    elif selected == "10. Quadratic Equation":
        st.subheader("Quadratic Equation Explorer")
        c1, c2, c3 = st.columns(3)
        a = c1.number_input("a", value=1.0, step=1.0)
        b = c2.number_input("b", value=-5.0, step=1.0)
        c = c3.number_input("c", value=6.0, step=1.0)
        if a == 0:
            st.error("a must not be zero.")
        else:
            D = b*b - 4*a*c
            st.metric("Discriminant", f"{D:g}")
            st.info("Two distinct real roots." if D > 0 else "One repeated real root." if D == 0 else "Two complex conjugate roots.")
            st.write(f"Root 1 = {(-b + cmath.sqrt(D)) / (2*a)}")
            st.write(f"Root 2 = {(-b - cmath.sqrt(D)) / (2*a)}")

with tab3:
    st.subheader("Python Programme")
    st.code(CODE[selected], language="python")
    st.download_button(
        "⬇️ Download this Python programme",
        data=CODE[selected],
        file_name=f"{selected.split('. ',1)[1].lower().replace(' ', '_')}.py",
        mime="text/x-python",
    )

st.divider()
st.caption("Python Practical Lab • Interactive learning companion for undergraduate Mathematics practical classes.")
