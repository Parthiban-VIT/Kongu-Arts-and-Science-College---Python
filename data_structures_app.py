"""
Unit V - Data Structures in Python (Lists, Tuples, Dictionaries)
Run:  pip install streamlit
      streamlit run data_structures_app.py
"""
import io
import contextlib
import streamlit as st

st.set_page_config(page_title="Unit V – Data Structures", page_icon="🐍", layout="wide")


# ----------------------------------------------------------------- helpers
def run(code: str) -> str:
    """Execute code and return everything it printed."""
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            exec(code, {})
    except Exception as e:  # show errors as learning material
        buf.write(f"{type(e).__name__}: {e}")
    return buf.getvalue()


def example(code: str, title: str = None, editable: bool = False, key: str = None):
    """Show a code example together with its live output."""
    if title:
        st.markdown(f"**{title}**")
    code = code.strip("\n")
    if editable:
        code = st.text_area("Edit and re-run the code:", code, height=200, key=key)
    else:
        st.code(code, language="python")
    out = run(code)
    st.markdown("Output:")
    st.code(out if out.strip() else "(no output)", language="text")


def note(text):
    st.info(text, icon="💡")


# ----------------------------------------------------------------- pages
def page_home():
    st.title("🐍 Unit V – Data Structures")
    st.caption("Python Programming Using Problem Solving Approach – Reema Thareja (Chapter 8)")
    st.markdown(
        """
Welcome! Use the **sidebar** to move through the unit.

| Part | Topics |
|---|---|
| **Lists** | Sequence, access, update, nested lists, cloning, basic operations, methods |
| **Tuples** | Creating, utility, access, update, delete, operations, assignment, returning multiple values, nested tuples |
| **Dictionaries** | Creating, accessing, adding/modifying, deleting, sorting |
| **Practice** | Playgrounds and a quiz |
"""
    )
    st.subheader("Quick comparison")
    st.table(
        {
            "Feature": ["Syntax", "Mutable?", "Ordered?", "Duplicates?", "Access by", "Typical use"],
            "List": ["[1, 2, 3]", "Yes", "Yes", "Allowed", "Index", "Collection that changes"],
            "Tuple": ["(1, 2, 3)", "No", "Yes", "Allowed", "Index", "Fixed data, return values"],
            "Dictionary": ["{'a': 1}", "Yes", "Yes (insertion order)", "Keys unique", "Key", "Look-ups / records"],
        }
    )


def page_sequence():
    st.header("Sequence")
    st.markdown(
        """
A **sequence** is an ordered collection of items where each item has a position (**index**).
Strings, lists and tuples are all sequences and share these features:

- Indexing starts at **0** (negative indexes count from the end: `-1` = last)
- Slicing `seq[start:stop:step]`
- `len()`, `in`, `+` (concatenation), `*` (repetition), iteration with `for`
"""
    )
    example(
        """
s = "PYTHON"
print(s[0], s[-1])        # first and last
print(s[1:4])             # slice
print(s[::-1])            # reversed
print(len(s), 'T' in s)
print(s * 2)
""",
        "Same operations work on any sequence",
    )
    st.subheader("Try slicing")
    text = st.text_input("Sequence (string):", "PROGRAMMING")
    c1, c2, c3 = st.columns(3)
    a = c1.number_input("start", value=0, step=1)
    b = c2.number_input("stop", value=len(text), step=1)
    c = c3.number_input("step", value=1, step=1)
    if c == 0:
        st.error("step cannot be 0")
    else:
        st.code(f"'{text}'[{a}:{b}:{c}]  →  '{text[a:b:c]}'")


def page_lists():
    st.title("📋 Lists")
    tabs = st.tabs(["Basics & Access", "Updating", "Nested", "Cloning", "Operations", "Methods", "Playground"])

    with tabs[0]:
        st.markdown("A **list** is an ordered, **mutable** sequence written with square brackets.")
        example(
            """
fruits = ["apple", "banana", "cherry", "mango"]
mixed = [10, "hi", 3.5, True]     # can hold different types
empty = []
print(fruits, type(fruits))
print(list("abc"))                 # from any iterable
print(list(range(1, 10, 2)))
""",
            "Creating lists",
        )
        example(
            """
nums = [10, 20, 30, 40, 50]
print(nums[0])       # first
print(nums[-1])      # last
print(nums[1:4])     # slice -> [20, 30, 40]
print(nums[:3])      # first three
print(nums[::2])     # every 2nd element
for i, v in enumerate(nums):
    print(i, "->", v)
""",
            "Accessing values",
        )
        note("Accessing an index that doesn't exist raises `IndexError: list index out of range`.")

    with tabs[1]:
        example(
            """
marks = [45, 60, 72, 88]
marks[0] = 50                 # change one value
print(marks)
marks[1:3] = [65, 75]         # change a slice
print(marks)
marks[1:3] = [1, 2, 3, 4]     # slice can grow the list
print(marks)
""",
            "Updating values in lists (lists are mutable)",
        )

    with tabs[2]:
        st.markdown("A **nested list** is a list that contains other lists — great for tables/matrices.")
        example(
            """
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[1])        # a row
print(matrix[1][2])     # row 1, column 2 -> 6
matrix[0][0] = 100
for row in matrix:
    print(row)

# sum of each row
print([sum(r) for r in matrix])
""",
            "2-D list example",
        )

    with tabs[3]:
        st.markdown(
            "`b = a` does **not** copy — both names refer to the *same* list. To **clone** a list, make a real copy."
        )
        example(
            """
a = [1, 2, 3]
b = a                   # alias, NOT a copy
b.append(99)
print("a:", a, "b:", b, "same object?", a is b)
""",
            "Aliasing (the trap)",
        )
        example(
            """
import copy
a = [1, 2, 3]
c1 = a[:]               # slicing
c2 = list(a)            # list()
c3 = a.copy()           # copy()
c1.append(4)
print("a:", a, "c1:", c1, "independent?", a is not c1)

# Shallow vs deep copy for nested lists
n = [[1, 2], [3, 4]]
shallow = n.copy()
deep = copy.deepcopy(n)
n[0][0] = "X"
print("shallow:", shallow)   # inner list shared -> changed
print("deep   :", deep)      # fully independent
""",
            "Cloning techniques",
        )

    with tabs[4]:
        example(
            """
a = [1, 2, 3]
b = [4, 5]
print(a + b)            # concatenation
print(a * 3)            # repetition
print(2 in a, 9 not in a)   # membership
print(len(a), max(a), min(a), sum(a))
print(a == [1, 2, 3])   # comparison
for x in a:             # iteration
    print(x, end=" ")
print()
del a[1]                # delete by index
print(a)
""",
            "Basic list operations",
        )

    with tabs[5]:
        st.markdown("Common list methods:")
        st.table(
            {
                "Method": ["append(x)", "extend(iter)", "insert(i, x)", "remove(x)", "pop([i])", "index(x)",
                           "count(x)", "sort()", "reverse()", "clear()"],
                "Purpose": ["Add x at end", "Add all items of iterable", "Insert x at position i",
                            "Remove first x", "Remove & return item (last by default)", "Position of first x",
                            "How many times x occurs", "Sort in place", "Reverse in place", "Remove everything"],
            }
        )
        example(
            """
L = [5, 2, 9, 2]
L.append(7);           print("append :", L)
L.extend([1, 3]);      print("extend :", L)
L.insert(0, 100);      print("insert :", L)
L.remove(2);           print("remove :", L)
print("pop    :", L.pop(), L)
print("index  :", L.index(9))
print("count  :", L.count(2))
L.sort();              print("sort   :", L)
L.sort(reverse=True);  print("sort ↓ :", L)
L.reverse();           print("reverse:", L)
print("sorted() returns a new list:", sorted([3, 1, 2]))
""",
            "Methods in action",
        )

    with tabs[6]:
        st.markdown("Build a list and apply methods interactively.")
        if "pl" not in st.session_state:
            st.session_state.pl = [5, 3, 8]
        lst = st.session_state.pl
        st.code(f"my_list = {lst}")
        c1, c2 = st.columns([1, 1])
        val = c1.number_input("Value", value=0, step=1, key="pl_val")
        idx = c2.number_input("Index (for insert)", value=0, step=1, key="pl_idx")
        b = st.columns(6)
        if b[0].button("append"):
            lst.append(int(val))
            st.rerun()
        if b[1].button("insert"):
            lst.insert(int(idx), int(val))
            st.rerun()
        if b[2].button("remove"):
            if val in lst:
                lst.remove(int(val))
                st.rerun()
            else:
                st.warning("Value not in list")
        if b[3].button("pop"):
            if lst:
                lst.pop()
                st.rerun()
        if b[4].button("sort"):
            lst.sort()
            st.rerun()
        if b[5].button("reverse"):
            lst.reverse()
            st.rerun()
        if st.button("Reset"):
            st.session_state.pl = [5, 3, 8]
            st.rerun()


def page_tuples():
    st.title("📦 Tuples")
    tabs = st.tabs(["Creating & Utility", "Access", "Update / Delete", "Operations", "Assignment & Returning",
                    "Nested"])

    with tabs[0]:
        st.markdown("A **tuple** is an ordered, **immutable** sequence written with parentheses.")
        example(
            """
t1 = (1, 2, 3)
t2 = 4, 5, 6            # parentheses optional
t3 = (7,)               # single item needs a trailing comma!
t4 = ()                 # empty
t5 = tuple([8, 9])      # from list
print(t1, t2, t3, t4, t5)
print(type((7)), type((7,)))
""",
            "Creating tuples",
        )
        st.markdown("**Utility of tuples:** faster than lists, protect data from changes, can be used as dictionary keys, "
                    "and are ideal for returning several values.")
        example(
            """
point = (3, 4)
d = {point: "Home"}           # tuples are hashable -> valid key
print(d[(3, 4)])
import sys
print("list  bytes:", sys.getsizeof([1, 2, 3]))
print("tuple bytes:", sys.getsizeof((1, 2, 3)))
""",
            "Why use tuples?",
        )

    with tabs[1]:
        example(
            """
t = ("a", "b", "c", "d", "e")
print(t[0], t[-1])
print(t[1:4])
print(t[::-1])
print(t.index("c"), t.count("a"))
for item in t:
    print(item, end=" ")
""",
            "Accessing values in a tuple",
        )

    with tabs[2]:
        st.markdown("Tuples **cannot** be changed in place — but you can build a new tuple.")
        example(
            """
t = (1, 2, 3)
try:
    t[0] = 10
except TypeError as e:
    print("Error:", e)

# Updating: convert -> modify -> convert back
lst = list(t)
lst[0] = 10
t = tuple(lst)
print("updated:", t)

# or concatenate
t = t + (4, 5)
print("extended:", t)
""",
            "Updating a tuple",
        )
        example(
            """
t = (10, 20, 30, 40)
# Deleting single elements is not allowed
try:
    del t[1]
except TypeError as e:
    print("Error:", e)

# Delete an element by rebuilding
t = t[:1] + t[2:]
print("without index 1:", t)

# Delete the whole tuple
del t
try:
    print(t)
except NameError as e:
    print("Error:", e)
""",
            "Deleting elements in a tuple",
        )

    with tabs[3]:
        example(
            """
a = (1, 2, 3)
b = (4, 5)
print(a + b)              # concatenation
print(a * 2)              # repetition
print(2 in a)             # membership
print(len(a), max(a), min(a), sum(a))
print(a < (1, 2, 4))      # lexicographic comparison
print(sorted((3, 1, 2)))  # returns a LIST
""",
            "Basic tuple operations",
        )

    with tabs[4]:
        st.subheader("Tuple assignment")
        example(
            """
a, b = 10, 20
print("before:", a, b)
a, b = b, a               # swap without a temp variable
print("after :", a, b)

x, y, z = (1, 2, 3)       # unpacking
first, *rest = (1, 2, 3, 4)
print(x, y, z)
print(first, rest)
""",
        )
        st.subheader("Tuples for returning multiple values")
        example(
            """
def min_max_avg(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

result = min_max_avg([4, 8, 15, 16, 23, 42])
print(result, type(result))
lo, hi, avg = result
print(f"min={lo}, max={hi}, avg={avg:.2f}")

def divide(a, b):
    return a // b, a % b     # quotient and remainder
q, r = divide(17, 5)
print(q, r)
""",
        )

    with tabs[5]:
        example(
            """
students = (("Asha", 85), ("Ravi", 72), ("Meena", 91))
print(students[1])          # ('Ravi', 72)
print(students[1][0])       # 'Ravi'
for name, mark in students:
    print(f"{name:<6} {mark}")

# A tuple is immutable, but a mutable item inside it can change
t = (1, [2, 3])
t[1].append(4)
print(t)
""",
            "Nested tuples",
        )
        note("Immutability applies to the tuple itself — a list *inside* a tuple can still be modified.")


def page_dicts():
    st.title("📖 Dictionaries")
    st.markdown("A **dictionary** stores **key : value** pairs. Keys must be unique and immutable "
                "(str, int, tuple); values can be anything.")
    tabs = st.tabs(["Creating & Accessing", "Add / Modify", "Delete", "Sorting", "Playground"])

    with tabs[0]:
        example(
            """
student = {"name": "Asha", "age": 19, "course": "BCA"}
empty = {}
d2 = dict(a=1, b=2)
d3 = dict([("x", 10), ("y", 20)])
d4 = dict.fromkeys(["p", "q"], 0)
print(student)
print(d2, d3, d4)
""",
            "Creating a dictionary",
        )
        example(
            """
student = {"name": "Asha", "age": 19, "course": "BCA"}
print(student["name"])
print(student.get("age"))
print(student.get("city", "Not given"))   # default, no error
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))
for k, v in student.items():
    print(k, "=", v)
try:
    print(student["city"])
except KeyError as e:
    print("KeyError:", e)
""",
            "Accessing values",
        )

    with tabs[1]:
        example(
            """
d = {"a": 1, "b": 2}
d["c"] = 3                 # add new item
print(d)
d["a"] = 100               # modify an existing entry
print(d)
d.update({"b": 20, "z": 26})   # add/modify many
print(d)
d.setdefault("k", 0)       # add only if missing
print(d)
""",
            "Adding and modifying an item / entry",
        )

    with tabs[2]:
        example(
            """
d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
del d["a"]                       # by key
print(d)
print(d.pop("b"))                # returns removed value
print(d.popitem())               # removes last inserted pair
print(d)
d.clear()                        # empties dictionary
print(d)
del d                            # deletes the dictionary itself
""",
            "Deleting items",
        )

    with tabs[3]:
        st.markdown("Dictionaries keep insertion order; to *sort*, use `sorted()`, which returns a **new list**.")
        example(
            """
marks = {"Ravi": 72, "Asha": 85, "Meena": 91, "Kiran": 60}

print(sorted(marks))                                  # keys A-Z
print(sorted(marks, reverse=True))                    # keys Z-A
print(sorted(marks.items()))                          # by key -> list of tuples
print(sorted(marks.items(), key=lambda kv: kv[1]))    # by value ascending
print(sorted(marks.items(), key=lambda kv: kv[1], reverse=True))

# Rebuild a sorted dictionary
by_value = dict(sorted(marks.items(), key=lambda kv: kv[1], reverse=True))
print(by_value)
""",
            "Sorting items in a dictionary",
        )
        example(
            """
text = "to be or not to be"
freq = {}
for w in text.split():
    freq[w] = freq.get(w, 0) + 1
print(freq)
print(dict(sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))))
""",
            "Mini project: word frequency",
        )

    with tabs[4]:
        if "pd" not in st.session_state:
            st.session_state.pd = {"apple": 50, "banana": 20}
        d = st.session_state.pd
        st.code(f"inventory = {d}")
        c1, c2 = st.columns(2)
        k = c1.text_input("Key", "orange")
        v = c2.number_input("Value", value=30, step=1)
        b = st.columns(4)
        if b[0].button("Add / Modify"):
            d[k] = int(v)
            st.rerun()
        if b[1].button("Delete key"):
            if k in d:
                del d[k]
                st.rerun()
            else:
                st.warning("Key not found")
        if b[2].button("Sort by key"):
            st.session_state.pd = dict(sorted(d.items()))
            st.rerun()
        if b[3].button("Sort by value"):
            st.session_state.pd = dict(sorted(d.items(), key=lambda kv: kv[1]))
            st.rerun()
        if st.button("Reset dictionary"):
            st.session_state.pd = {"apple": 50, "banana": 20}
            st.rerun()


def page_practice():
    st.title("✍️ Practice")
    tab1, tab2 = st.tabs(["Code sandbox", "Quiz"])

    with tab1:
        st.markdown("Write your own code and see the output.")
        example(
            """
# Try things out here
data = [3, 1, 2]
info = {"list": data, "tuple": tuple(data)}
print(info)
""",
            editable=True,
            key="sandbox",
        )

    with tab2:
        questions = [
            ("What is the output of `[1,2,3][-1]`?", ["1", "3", "Error", "[3]"], "3"),
            ("Which is immutable?", ["list", "dictionary", "tuple", "set"], "tuple"),
            ("How do you create a one-element tuple?", ["(5)", "(5,)", "[5]", "{5}"], "(5,)"),
            ("Which creates an independent copy of list `a`?", ["b = a", "b = a[:]", "b is a", "b == a"], "b = a[:]"),
            ("What does `d.get('x', 0)` return if 'x' is missing?", ["KeyError", "None", "0", "'x'"], "0"),
            ("`sorted()` on a dictionary's items returns a…", ["dictionary", "tuple", "list", "set"], "list"),
            ("`a, b = b, a` is an example of…", ["Slicing", "Tuple assignment", "Cloning", "Nested list"],
             "Tuple assignment"),
            ("Which method removes and returns the last list item?", ["remove()", "delete()", "pop()", "clear()"],
             "pop()"),
        ]
        answers = {}
        for i, (q, opts, _) in enumerate(questions):
            answers[i] = st.radio(f"{i + 1}. {q}", opts, index=None, key=f"q{i}")
        if st.button("Submit quiz"):
            score = 0
            for i, (_, _, correct) in enumerate(questions):
                if answers[i] == correct:
                    score += 1
                elif answers[i] is not None:
                    st.write(f"Q{i + 1}: ❌ correct answer is **{correct}**")
                else:
                    st.write(f"Q{i + 1}: ⚠️ not answered — correct answer is **{correct}**")
            st.success(f"Score: {score} / {len(questions)}")
            if score == len(questions):
                st.balloons()


# ----------------------------------------------------------------- navigation
PAGES = {
    "🏠 Overview": page_home,
    "🔢 Sequence": page_sequence,
    "📋 Lists": page_lists,
    "📦 Tuples": page_tuples,
    "📖 Dictionaries": page_dicts,
    "✍️ Practice": page_practice,
}

st.sidebar.title("Unit V – Data Structures")
choice = st.sidebar.radio("Go to", list(PAGES))
st.sidebar.caption("Textbook: Reema Thareja, Ch. 8 (§8.1, 8.2, 8.4, 8.6)")
PAGES[choice]()
