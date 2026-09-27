import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SymPy Learning Lab",
    page_icon="∑",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# LESSON INFORMATION
# ============================================================

LESSONS = {

    "1. Getting Started": {
        "aim":
            "Learn how to create symbolic variables and perform basic symbolic calculations.",

        "concept":
            "Unlike ordinary numerical Python, SymPy keeps mathematical expressions "
            "symbolic. This allows exact algebraic manipulation.",

        "topics":
            "symbols, expressions, expand, simplify, substitution, numerical evaluation",
    },

    "2. Algebraic Expressions": {
        "aim":
            "Use SymPy to expand, simplify and factor algebraic expressions.",

        "concept":
            "SymPy manipulates expressions exactly instead of immediately converting "
            "them into decimal approximations.",

        "topics":
            "expand, factor, collect, cancel, simplify",
    },

    "3. Substitution & Evaluation": {
        "aim":
            "Substitute values into symbolic expressions and evaluate them numerically.",

        "concept":
            "The subs() method performs symbolic substitution, while evalf() provides "
            "a numerical approximation.",

        "topics":
            "subs, evalf, N, exact arithmetic",
    },

    "4. Solving Equations": {
        "aim":
            "Solve algebraic equations symbolically.",

        "concept":
            "The solve() function finds symbolic solutions of algebraic equations.",

        "topics":
            "solve, equations, roots, symbolic solutions",
    },

    "5. Simultaneous Equations": {
        "aim":
            "Solve systems of two or more equations.",

        "concept":
            "SymPy can solve systems of equations exactly for several unknowns.",

        "topics":
            "systems, solve, dictionaries, multiple variables",
    },

    "6. Differentiation": {
        "aim":
            "Find first and higher-order derivatives symbolically.",

        "concept":
            "The diff() function differentiates symbolic expressions with respect "
            "to a chosen variable.",

        "topics":
            "diff, partial derivatives, higher derivatives",
    },

    "7. Integration": {
        "aim":
            "Find indefinite and definite integrals symbolically.",

        "concept":
            "The integrate() function computes antiderivatives and definite integrals.",

        "topics":
            "integrate, definite integrals, antiderivatives",
    },

    "8. Limits": {
        "aim":
            "Evaluate limits of symbolic functions.",

        "concept":
            "The limit() function evaluates the limiting value as a variable "
            "approaches a point or infinity.",

        "topics":
            "limit, infinity, one-sided limits",
    },

    "9. Series Expansion": {
        "aim":
            "Generate Taylor and Maclaurin series using SymPy.",

        "concept":
            "The series() function produces a symbolic power-series approximation "
            "around a specified point.",

        "topics":
            "series, Taylor expansion, Maclaurin expansion",
    },

    "10. Matrices": {
        "aim":
            "Perform matrix operations symbolically.",

        "concept":
            "SymPy Matrix supports matrix addition, multiplication, determinant, "
            "inverse, eigenvalues and more.",

        "topics":
            "Matrix, determinant, inverse, eigenvalues",
    },

    "11. Symbolic Plotting": {
        "aim":
            "Connect symbolic mathematics with graphical visualization.",

        "concept":
            "A SymPy expression can be converted into a numerical function and "
            "visualized using NumPy and Matplotlib.",

        "topics":
            "lambdify, NumPy, Matplotlib, visualization",
    },
}


# ============================================================
# PYTHON PROGRAMS
# ============================================================

CODE = {

"1. Getting Started": r'''import sympy as sp

x, y = sp.symbols("x y")

expr = x**2 + 2*x + 1

print("Expression:", expr)
print("Expanded:", sp.expand(expr))
print("Simplified:", sp.simplify(expr))
print("Value at x = 3:", expr.subs(x, 3))
''',

"2. Algebraic Expressions": r'''import sympy as sp

x = sp.symbols("x")

expr = (x + 2)*(x - 3)

print("Original:", expr)
print("Expanded:", sp.expand(expr))

expr2 = x**2 - 5*x + 6

print("Factored:", sp.factor(expr2))

expr3 = (x**2 - 1)/(x - 1)

print("Cancelled:", sp.cancel(expr3))
''',

"3. Substitution & Evaluation": r'''import sympy as sp

x = sp.symbols("x")

f = x**3 + 2*x**2 - x + 5

print("f(x) =", f)
print("f(2) =", f.subs(x, 2))
print("f(2.5) =", f.subs(x, 2.5))

print("sqrt(2) =", sp.sqrt(2))
print("Decimal value =", sp.sqrt(2).evalf())
''',

"4. Solving Equations": r'''import sympy as sp

x = sp.symbols("x")

equation = sp.Eq(x**2 - 5*x + 6, 0)

solutions = sp.solve(equation, x)

print("Equation:", equation)
print("Solutions:", solutions)
''',

"5. Simultaneous Equations": r'''import sympy as sp

x, y = sp.symbols("x y")

eq1 = sp.Eq(2*x + y, 7)
eq2 = sp.Eq(x - y, 1)

solution = sp.solve((eq1, eq2), (x, y))

print("Solution:", solution)
''',

"6. Differentiation": r'''import sympy as sp

x = sp.symbols("x")

f = x**4 - 3*x**2 + 2*x

first = sp.diff(f, x)
second = sp.diff(f, x, 2)

print("f(x) =", f)
print("First derivative =", first)
print("Second derivative =", second)

# Partial derivatives

x, y = sp.symbols("x y")

g = x**2*y + x*y**3

print("∂g/∂x =", sp.diff(g, x))
print("∂g/∂y =", sp.diff(g, y))
''',

"7. Integration": r'''import sympy as sp

x = sp.symbols("x")

f = 3*x**2 + 4*x + 1

indefinite = sp.integrate(f, x)

definite = sp.integrate(f, (x, 0, 2))

print("Function:", f)
print("Indefinite integral:", indefinite)
print("Definite integral from 0 to 2:", definite)
''',

"8. Limits": r'''import sympy as sp

x = sp.symbols("x")

expr = sp.sin(x)/x

print("lim(x→0) sin(x)/x =", sp.limit(expr, x, 0))

expr2 = (2*x**2 + 3*x)/(x**2 - 1)

print("lim(x→∞) =", sp.limit(expr2, x, sp.oo))
''',

"9. Series Expansion": r'''import sympy as sp

x = sp.symbols("x")

print("Maclaurin series of sin(x):")

print(
    sp.series(
        sp.sin(x),
        x,
        0,
        7
    )
)

print("Maclaurin series of e^x:")

print(
    sp.series(
        sp.exp(x),
        x,
        0,
        6
    )
)
''',

"10. Matrices": r'''import sympy as sp

A = sp.Matrix([
    [1, 2],
    [3, 4]
])

print("A =")

sp.pprint(A)

print("Determinant =", A.det())

print("Inverse =")

sp.pprint(A.inv())

print("Eigenvalues =", A.eigenvals())
''',

"11. Symbolic Plotting": r'''import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols("x")

f = x**2 - 4*x + 3

f_num = sp.lambdify(
    x,
    f,
    "numpy"
)

X = np.linspace(-1, 5, 400)

Y = f_num(X)

plt.plot(X, Y)

plt.axhline(0)
plt.axvline(0)

plt.xlabel("x")
plt.ylabel("f(x)")

plt.title(
    "y = x² - 4x + 3"
)

plt.grid()

plt.show()
''',
}


# ============================================================
# SAMPLE OUTPUT
# ============================================================

SAMPLE_OUTPUT = {

"1. Getting Started": r'''Expression: x**2 + 2*x + 1
Expanded: x**2 + 2*x + 1
Simplified: x**2 + 2*x + 1
Value at x = 3: 16
''',

"2. Algebraic Expressions": r'''Original: (x + 2)*(x - 3)
Expanded: x**2 - x - 6
Factored: (x - 2)*(x - 3)
Cancelled: x + 1
''',

"3. Substitution & Evaluation": r'''f(x) = x**3 + 2*x**2 - x + 5
f(2) = 15
f(2.5) = 26.875
sqrt(2) = sqrt(2)
Decimal value = 1.41421356237310
''',

"4. Solving Equations": r'''Equation: Eq(x**2 - 5*x + 6, 0)
Solutions: [2, 3]
''',

"5. Simultaneous Equations": r'''Solution: {x: 8/3, y: 5/3}
''',

"6. Differentiation": r'''f(x) = x**4 - 3*x**2 + 2*x
First derivative = 4*x**3 - 6*x + 2
Second derivative = 12*x**2 - 6
∂g/∂x = 2*x*y + y**3
∂g/∂y = x**2 + 3*x*y**2
''',

"7. Integration": r'''Function: 3*x**2 + 4*x + 1
Indefinite integral: x**3 + 2*x**2 + x
Definite integral from 0 to 2: 18
''',

"8. Limits": r'''lim(x→0) sin(x)/x = 1
lim(x→∞) = 2
''',

"9. Series Expansion": r'''Maclaurin series of sin(x):
x - x**3/6 + x**5/120 + O(x**7)

Maclaurin series of e^x:
1 + x + x**2/2 + x**3/6 + x**4/24 + x**5/120 + O(x**6)
''',

"10. Matrices": r'''Determinant = -2

Inverse =
Matrix([
[-2, 1],
[3/2, -1/2]
])

Eigenvalues =
{5/2 - sqrt(33)/2: 1,
 5/2 + sqrt(33)/2: 1}
''',

"11. Symbolic Plotting": r'''A graph of

y = x² - 4x + 3

is displayed for -1 ≤ x ≤ 5.
''',
}


# ============================================================
# EXERCISES
# ============================================================

EXERCISES = {

"1. Getting Started": [
    "Create symbols x and y and form x² + 3xy + y².",
    "Substitute x = 2 and y = 3 into x² + 3xy + y².",
    "Create 1/3 as an exact SymPy Rational number and display it.",
],

"2. Algebraic Expressions": [
    "Expand (x + 3)(x − 5).",
    "Factor x² − 9x + 20.",
    "Simplify (x² − 4)/(x − 2).",
],

"3. Substitution & Evaluation": [
    "For f(x) = x³ − 4x + 1, find f(2).",
    "Evaluate √3 to 10 decimal places.",
    "For x² + y², substitute x = 3 and y = 4.",
],

"4. Solving Equations": [
    "Solve x² − 7x + 12 = 0.",
    "Solve 2x + 5 = 17.",
    "Solve x³ − 8 = 0.",
],

"5. Simultaneous Equations": [
    "Solve 3x + 2y = 12 and x − y = 1.",
    "Solve x + y + z = 6, x − y = 0 and y − z = 0.",
    "Use solve() to find x and y for x² + y² = 25 and y = x.",
],

"6. Differentiation": [
    "Find d/dx of x⁵ − 4x³ + 7x.",
    "Find the second derivative of sin(x)·exp(x).",
    "Find both partial derivatives of x²y + xy².",
],

"7. Integration": [
    "Find ∫(4x³ − 2x + 1) dx.",
    "Evaluate ∫₀¹ (x² + 1) dx.",
    "Find ∫ x·sin(x) dx.",
],

"8. Limits": [
    "Evaluate lim(x→0) sin(3x)/x.",
    "Evaluate lim(x→∞) (3x² + 1)/(x² − 2).",
    "Evaluate lim(x→1) (x² − 1)/(x − 1).",
],

"9. Series Expansion": [
    "Find the Maclaurin series of cos(x) up to x⁶.",
    "Find the Maclaurin series of ln(1+x) up to x⁵.",
    "Find the Taylor series of e^x about x = 1.",
],

"10. Matrices": [
    "Create a 3×3 SymPy matrix and find its determinant.",
    "Find the inverse of [[2,1],[1,1]].",
    "Find the eigenvalues of [[2,1],[1,2]].",
],

"11. Symbolic Plotting": [
    "Plot y = x³ − 3x over −3 ≤ x ≤ 3.",
    "Plot y = sin(x) and y = cos(x) on the same axes.",
    "Plot y = x² − 4x + 3 and identify its x-intercepts.",
],
}


# ============================================================
# CHALLENGE QUESTIONS
# ============================================================

CHALLENGES = {

"1. Getting Started":
    "Create a symbolic expression involving x, y and z, simplify it, "
    "and evaluate it for three different sets of values.",

"2. Algebraic Expressions":
    "Use SymPy to show that two different-looking algebraic expressions "
    "are equivalent.",

"3. Substitution & Evaluation":
    "Create a function of two variables and generate a small table of "
    "values using substitution.",

"4. Solving Equations":
    "Solve a cubic equation and verify every solution by substituting "
    "it back into the original equation.",

"5. Simultaneous Equations":
    "Solve a 3×3 linear system and compare the result with matrix methods.",

"6. Differentiation":
    "Find the critical points of a polynomial by solving f'(x) = 0.",

"7. Integration":
    "Find the area under a curve between two specified limits and "
    "verify it numerically.",

"8. Limits":
    "Compare the left-hand and right-hand limits of a function at "
    "a discontinuity.",

"9. Series Expansion":
    "Use a Taylor polynomial to approximate a function value and "
    "compare it with the exact value.",

"10. Matrices":
    "Find eigenvalues and eigenvectors of a 2×2 matrix and verify "
    "Av = λv.",

"11. Symbolic Plotting":
    "Plot a function, identify its zeros, and verify the zeros using solve().",
}


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 2.6rem;
        font-weight: 800;
        margin-bottom: 0.1rem;
    }

    .subtitle {
        font-size: 1.1rem;
        color: #666666;
        margin-bottom: 1.3rem;
    }

    .learning-box {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">∑ SymPy Learning Lab</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'A visual and interactive introduction to symbolic mathematics '
    'with Python and SymPy.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("📚 SymPy Lessons")

    selected = st.radio(
        "Choose a topic",
        list(LESSONS.keys())
    )

    st.divider()

    st.markdown("### Learning Route")

    st.caption(
        "Learn → Explore → See the code → "
        "Try the exercises"
    )

    st.caption(
        "Designed for undergraduate Mathematics students."
    )


lesson = LESSONS[selected]


# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📖 Learn",
        "🔬 Explore",
        "💻 Code & Output",
        "✏️ Exercises",
    ]
)


# ============================================================
# TAB 1 — LEARN
# ============================================================

with tab1:

    st.subheader("🎯 Aim")

    st.write(lesson["aim"])

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 💡 Concept")

        st.info(lesson["concept"])

    with col2:

        st.markdown("### 🐍 Python / SymPy Topics")

        st.success(lesson["topics"])

    st.markdown("### Why SymPy?")

    st.write(
        "SymPy allows us to work with mathematics symbolically. "
        "For example, SymPy can preserve exact fractions, manipulate "
        "algebraic expressions, solve equations, differentiate and "
        "integrate functions, evaluate limits, work with matrices "
        "and generate series expansions."
    )

    st.markdown("### Recommended Teaching Pattern")

    st.write(
        "**Mathematical idea → SymPy command → "
        "Interactive experiment → Python code → Exercise**"
    )


# ============================================================
# TAB 2 — EXPLORE
# ============================================================

with tab2:

    # --------------------------------------------------------
    # 1. GETTING STARTED
    # --------------------------------------------------------

    if selected == "1. Getting Started":

        st.subheader("🔬 Symbolic Expression Explorer")

        x = sp.symbols("x")

        expr_text = st.text_input(
            "Enter an expression in x",
            "x**2 + 2*x + 1"
        )

        value = st.number_input(
            "Substitute x =",
            value=3.0
        )

        try:

            expr = sp.sympify(expr_text)

            st.latex(
                sp.latex(expr)
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.markdown("**Expanded**")

                st.code(
                    str(sp.expand(expr))
                )

            with col2:

                st.markdown("**Simplified**")

                st.code(
                    str(sp.simplify(expr))
                )

            with col3:

                st.markdown(
                    f"**At x = {value}**"
                )

                st.code(
                    str(expr.subs(x, value))
                )

        except Exception as e:

            st.error(
                f"Please enter a valid SymPy expression. {e}"
            )


    # --------------------------------------------------------
    # 2. ALGEBRA
    # --------------------------------------------------------

    elif selected == "2. Algebraic Expressions":

        st.subheader(
            "🔬 Expand • Factor • Simplify"
        )

        x = sp.symbols("x")

        expr_text = st.text_input(
            "Expression",
            "(x + 2)*(x - 3)"
        )

        try:

            expr = sp.sympify(expr_text)

            col1, col2, col3 = st.columns(3)

            with col1:

                st.markdown("**Expand**")

                st.code(
                    str(sp.expand(expr))
                )

            with col2:

                st.markdown("**Factor**")

                st.code(
                    str(sp.factor(expr))
                )

            with col3:

                st.markdown("**Simplify**")

                st.code(
                    str(sp.simplify(expr))
                )

            st.latex(
                sp.latex(expr)
            )

        except Exception as e:

            st.error(str(e))


    # --------------------------------------------------------
    # 3. SUBSTITUTION
    # --------------------------------------------------------

    elif selected == "3. Substitution & Evaluation":

        st.subheader(
            "🔬 Substitution Explorer"
        )

        x, y = sp.symbols("x y")

        expr_text = st.text_input(
            "Expression",
            "x**2 + 3*x*y + y**2"
        )

        col1, col2 = st.columns(2)

        with col1:

            xv = st.number_input(
                "x =",
                value=2.0
            )

        with col2:

            yv = st.number_input(
                "y =",
                value=3.0
            )

        try:

            expr = sp.sympify(expr_text)

            result = expr.subs(
                {
                    x: xv,
                    y: yv
                }
            )

            st.latex(
                sp.latex(expr)
            )

            st.metric(
                "Result",
                str(result)
            )

            st.write(
                "Numerical approximation:",
                sp.N(result, 8)
            )

        except Exception as e:

            st.error(str(e))


    # --------------------------------------------------------
    # 4. SOLVING EQUATIONS
    # --------------------------------------------------------

    elif selected == "4. Solving Equations":

        st.subheader(
            "🔬 Equation Solver"
        )

        x = sp.symbols("x")

        expr_text = st.text_input(
            "Enter expression equal to zero",
            "x**2 - 5*x + 6"
        )

        try:

            expr = sp.sympify(expr_text)

            solutions = sp.solve(
                expr,
                x
            )

            st.latex(
                sp.latex(
                    sp.Eq(expr, 0)
                )
            )

            st.success(
                f"Solutions: {solutions}"
            )

        except Exception as e:

            st.error(str(e))


    # --------------------------------------------------------
    # 5. SIMULTANEOUS EQUATIONS
    # --------------------------------------------------------

    elif selected == "5. Simultaneous Equations":

        st.subheader(
            "🔬 System of Equations"
        )

        x, y = sp.symbols("x y")

        eq1 = st.text_input(
            "Equation 1",
            "2*x + y = 7"
        )

        eq2 = st.text_input(
            "Equation 2",
            "x - y = 1"
        )

        def parse_equation(text):

            if "=" in text:

                left, right = text.split(
                    "=",
                    1
                )

                return sp.Eq(
                    sp.sympify(left),
                    sp.sympify(right)
                )

            return sp.Eq(
                sp.sympify(text),
                0
            )

        try:

            equation1 = parse_equation(eq1)
            equation2 = parse_equation(eq2)

            solution = sp.solve(
                (
                    equation1,
                    equation2
                ),
                (
                    x,
                    y
                ),
                dict=True
            )

            st.success(
                f"Solution: {solution}"
            )

        except Exception as e:

            st.error(
                f"Enter valid equations using x and y. {e}"
            )


    # --------------------------------------------------------
    # 6. DIFFERENTIATION
    # --------------------------------------------------------

    elif selected == "6. Differentiation":

        st.subheader(
            "🔬 Derivative Explorer"
        )

        x = sp.symbols("x")

        expr_text = st.text_input(
            "f(x) =",
            "x**4 - 3*x**2 + 2*x"
        )

        order = st.slider(
            "Derivative order",
            1,
            5,
            1
        )

        try:

            expr = sp.sympify(
                expr_text
            )

            result = sp.diff(
                expr,
                x,
                order
            )

            st.latex(
                sp.latex(result)
            )

            st.success(
                f"{order}-order derivative = {result}"
            )

        except Exception as e:

            st.error(str(e))


    # --------------------------------------------------------
    # 7. INTEGRATION
    # --------------------------------------------------------

    elif selected == "7. Integration":

        st.subheader(
            "🔬 Integration Explorer"
        )

        x = sp.symbols("x")

        expr_text = st.text_input(
            "Function f(x) =",
            "3*x**2 + 4*x + 1"
        )

        definite = st.checkbox(
            "Calculate a definite integral"
        )

        try:

            expr = sp.sympify(
                expr_text
            )

            if definite:

                col1, col2 = st.columns(2)

                with col1:

                    a = st.number_input(
                        "Lower limit",
                        value=0.0
                    )

                with col2:

                    b = st.number_input(
                        "Upper limit",
                        value=2.0
                    )

                result = sp.integrate(
                    expr,
                    (
                        x,
                        a,
                        b
                    )
                )

                st.success(
                    f"Definite integral = {result}"
                )

            else:

                result = sp.integrate(
                    expr,
                    x
                )

                st.success(
                    f"Indefinite integral = {result} + C"
                )

            st.latex(
                sp.latex(result)
            )

        except Exception as e:

            st.error(str(e))


    # --------------------------------------------------------
    # 8. LIMITS
    # --------------------------------------------------------

    elif selected == "8. Limits":

        st.subheader(
            "🔬 Limit Explorer"
        )

        x = sp.symbols("x")

        expr_text = st.text_input(
            "Expression",
            "sin(x)/x"
        )

        point_text = st.text_input(
            "Point",
            "0"
        )

        direction = st.selectbox(
            "Direction",
            [
                "Both sides",
                "Right",
                "Left"
            ]
        )

        try:

            if point_text.lower() in [
                "oo",
                "inf",
                "infinity"
            ]:

                point = sp.oo

            else:

                point = sp.sympify(
                    point_text
                )

            if direction == "Right":

                dir_value = "+"

            elif direction == "Left":

                dir_value = "-"

            else:

                dir_value = "+-"

            result = sp.limit(
                sp.sympify(expr_text),
                x,
                point,
                dir=dir_value
            )

            st.success(
                f"Limit = {result}"
            )

            st.latex(
                sp.latex(result)
            )

        except Exception as e:

            st.error(str(e))


    # --------------------------------------------------------
    # 9. SERIES
    # --------------------------------------------------------

    elif selected == "9. Series Expansion":

        st.subheader(
            "🔬 Taylor / Maclaurin Series Explorer"
        )

        x = sp.symbols("x")

        expr_text = st.text_input(
            "Function",
            "sin(x)"
        )

        point = st.number_input(
            "Expansion point",
            value=0.0
        )

        order = st.slider(
            "Series order",
            2,
            12,
            6
        )

        try:

            expr = sp.sympify(
                expr_text
            )

            result = sp.series(
                expr,
                x,
                point,
                order
            )

            st.success(
                "Series expansion:"
            )

            st.latex(
                sp.latex(result)
            )

        except Exception as e:

            st.error(str(e))


    # --------------------------------------------------------
    # 10. MATRICES
    # --------------------------------------------------------

    elif selected == "10. Matrices":

        st.subheader(
            "🔬 Matrix Explorer"
        )

        text = st.text_area(
            "Enter matrix — one row per line",
            "1 2\n3 4"
        )

        try:

            rows = []

            for row in text.strip().splitlines():

                values = row.replace(
                    ",",
                    " "
                ).split()

                rows.append(
                    [
                        sp.sympify(v)
                        for v in values
                    ]
                )

            A = sp.Matrix(rows)

            st.write("### Matrix")

            st.latex(
                sp.latex(A)
            )

            col1, col2 = st.columns(2)

            with col1:

                if A.rows == A.cols:

                    st.metric(
                        "Determinant",
                        str(A.det())
                    )

                else:

                    st.write(
                        "Determinant is defined only for square matrices."
                    )

            with col2:

                if (
                    A.rows == A.cols
                    and A.det() != 0
                ):

                    st.write("Inverse")

                    st.latex(
                        sp.latex(A.inv())
                    )

                else:

                    st.write(
                        "Inverse is not available."
                    )

            if A.rows == A.cols:

                st.write(
                    "### Eigenvalues"
                )

                st.write(
                    A.eigenvals()
                )

        except Exception as e:

            st.error(
                f"Invalid matrix: {e}"
            )


    # --------------------------------------------------------
    # 11. SYMBOLIC PLOTTING
    # --------------------------------------------------------

    elif selected == "11. Symbolic Plotting":

        st.subheader(
            "🔬 Function Plotter"
        )

        x = sp.symbols("x")

        expr_text = st.text_input(
            "y =",
            "x**2 - 4*x + 3"
        )

        col1, col2 = st.columns(2)

        with col1:

            xmin = st.number_input(
                "Minimum x",
                value=-1.0
            )

        with col2:

            xmax = st.number_input(
                "Maximum x",
                value=5.0
            )

        try:

            expr = sp.sympify(
                expr_text
            )

            fn = sp.lambdify(
                x,
                expr,
                "numpy"
            )

            X = np.linspace(
                xmin,
                xmax,
                500
            )

            Y = fn(X)

            fig, ax = plt.subplots(
                figsize=(9, 4.5)
            )

            ax.plot(
                X,
                Y
            )

            ax.axhline(
                0,
                linewidth=0.8
            )

            ax.axvline(
                0,
                linewidth=0.8
            )

            ax.grid(
                True,
                alpha=0.25
            )

            ax.set_xlabel("x")
            ax.set_ylabel("y")

            ax.set_title(
                f"y = {expr}"
            )

            st.pyplot(fig)

        except Exception as e:

            st.error(
                f"Unable to plot expression: {e}"
            )


# ============================================================
# TAB 3 — CODE & OUTPUT
# ============================================================

with tab3:

    st.subheader(
        "💻 Python + SymPy Code"
    )

    st.code(
        CODE[selected],
        language="python"
    )

    st.markdown(
        "### 🖥️ Exact Sample Output"
    )

    st.code(
        SAMPLE_OUTPUT[selected],
        language="text"
    )

    file_name = (
        selected
        .split(". ", 1)[1]
        .lower()
        .replace(" ", "_")
        + ".py"
    )

    st.download_button(
        "⬇️ Download this example as .py",
        data=CODE[selected],
        file_name=file_name,
        mime="text/x-python"
    )


# ============================================================
# TAB 4 — EXERCISES
# ============================================================

with tab4:

    st.subheader(
        "✏️ Practice Exercises"
    )

    st.write(
        "Try these exercises after exploring the example. "
        "Students should write the SymPy code themselves."
    )

    exercises = EXERCISES[selected]

    for i, exercise in enumerate(
        exercises,
        start=1
    ):

        st.markdown(
            f"**Exercise {i}.** {exercise}"
        )

    st.divider()

    st.subheader(
        "⭐ Challenge Activity"
    )

    st.info(
        CHALLENGES[selected]
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "SymPy Learning Lab • Symbolic Mathematics with Python • "
    "Designed for undergraduate Mathematics practical teaching"
)
