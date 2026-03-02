import streamlit as st


class Expense:
    def __init__(self,name,amount):
        self.name = name
        self.amount = int(amount)
class Goal:
    def __init__(self, name, amount):
        self.name=name
        self.amount =int(amount)


if 'expenses' not in st.session_state:
    st.session_state.expenses = [Expense('Breakfast', 200),Expense('Rent', 1000),
        Expense('Electricity Bill', 5000),
    Expense('Parking', 100),Expense('Grocery', 750),
        Expense('Fruit', 100),
    Expense('Gas Bill', 2000),Expense('Internet', 1000)]

if 'goals' not in st.session_state:
    st.session_state.goals = [Goal('Car', 700000),Goal('Bike', 50000),Goal('Phone', 30000),
    Goal('Laptop', 45000),Goal('House', 1000000)]
if 'budget' not in st.session_state:
    st.session_state.budget = 20000



st.title("Expense Tracker")
st.write("By Ali Ahmed and Rizwan Ahmed")
choice = st.sidebar.selectbox("Menu",["Set Budget","Add Expense","Remove Expense","Show Goals","Add Goal","Remove Goal","Show Expenses"])

if choice=="Show Expenses":
    total=0
    for i in range(len(st.session_state.expenses)):
        exp=st.session_state.expenses[i]
        st.write(str(i+1)+". "+exp.name+" : Rs "+str(exp.amount))
        total=total+exp.amount

    st.write("Total Expenses: Rs "+str(total))
    st.write("Budget: Rs "+str(st.session_state.budget))
    saving=st.session_state.budget - total
    if total>st.session_state.budget:
        st.write("Savings: Rs "+str(saving)+" (Budget Exceeded)")
        st.write("Try to reduce your expenses")
    else:
        st.write("Savings: Rs "+ str(saving))
        st.write("How long to reach your goals:")
        for g in st.session_state.goals:
            months=int(g.amount/saving)
            st.write(g.name+" - Rs "+str(g.amount)+" - "+str(months)+" months")

    st.write("Yearly total with inflation (0.4 percent per month):")
    yearly=0
    for i in range(12):
        yearly=yearly+total
        yearly=yearly+total*0.004
    st.write("Rs "+str(int(yearly)))


elif choice=="Add Expense":
    name=st.text_input("Expense Name")
    amount=st.text_input("Amount in Rs")
    if st.button("Add"):
        st.session_state.expenses.append(Expense(name,amount))
        st.write("Expense added")
elif choice=="Remove Expense":
    name = st.text_input("Enter name of expense to remove")
    if st.button("Remove"):
        for i in range(len(st.session_state.expenses)):
            if st.session_state.expenses[i].name==name:
                st.session_state.expenses.pop(i)
                st.write("Removed")
                break
elif choice=="Show Goals":
    for i in range(len(st.session_state.goals)):
        g = st.session_state.goals[i]
        st.write(str(i+1)+". "+ g.name+" : Rs "+str(g.amount))

elif choice=="Add Goal":
    name = st.text_input("Goal Name")
    amount=st.text_input("Goal Amount in Rs")
    if st.button("Add"):
        st.session_state.goals.append(Goal(name, amount))
        st.write("Goal added")
elif choice=="Remove Goal":
    name=st.text_input("Enter name of goal to remove")
    if st.button("Remove"):
        for i in range(len(st.session_state.goals)):
            if st.session_state.goals[i].name==name:
                st.session_state.goals.pop(i)
                st.write("Removed")
                break
elif choice=="Set Budget":
    new_budget=st.text_input("Enter new budget",value=str(st.session_state.budget))
    if st.button("Update"):
        st.session_state.budget=int(new_budget)
        st.write("Budget updated to Rs "+str(st.session_state.budget))




