# Sample employee data.
employees = [
    {"name": "Anne", "availability": [1, 2, 3, 4, 5], "max_hours": 30},
    {"name": "Belle", "availability": [2, 3, 4, 5, 6], "max_hours": 20},
    {"name": "Carrie", "availability": [1, 2, 3, 4, 5, 6], "max_hours": 40},

    # Add more employees
]

# Sample shift data
shifts = [
    {"day": 1, "shift_type": "Morning", "required_employees": 2, "hours": 4},
    {"day": 1, "shift_type": "Afternoon", "required_employees": 1, "hours": 4},
    {"day": 2, "shift_type": "Morning", "required_employees": 2, "hours": 4},
    {"day": 2, "shift_type": "Afternoon", "required_employees": 1, "hours": 4},
    {"day": 3, "shift_type": "Morning", "required_employees": 2, "hours": 4},
    {"day": 3, "shift_type": "Afternoon", "required_employees": 1, "hours": 4},
    # Add more shifts
]

# Initialize a schedule
schedule = []

# Sort shifts by priority (e.g., by day and required employees)
shifts.sort(key=lambda x: (x["day"], -x["required_employees"]))

# Assign employees to shifts
for shift in shifts:
    assigned_employees = []

    for employee in employees:
        # Check if the employee is available on the shift day
        if shift["day"] in employee["availability"]:
            # Check if the employee hasn't exceeded their max hours
            if sum([s.get("hours", 0) for s in assigned_employees]) + shift["hours"] <= employee["max_hours"]:
                assigned_employees.append(employee)
                shift["hours"] = shift.get("hours", 0) + 4  # Assuming a 4-hour shift

        # Check if we've met the required number of employees for the shift
        if len(assigned_employees) == shift["required_employees"]:
            break

    # Add the assigned employees to the schedule
    schedule.append({"shift": shift, "assigned_employees": assigned_employees})

# Print the final schedule
for entry in schedule:
    shift = entry["shift"]
    employees = ", ".join([e["name"] for e in entry["assigned_employees"]])
    print(f"{shift['day']} - {shift['shift_type']} - Employees: {employees}")
