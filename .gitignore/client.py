name = input("What is your name? ").capitalize()
age = input("What is your age? ")
while True:
    gender = input("What is your gender? (Male or Female) ").capitalize()
    if gender in ["Male", "Female"]:
        break
    else:
        print("Please input a valid answer")
weight = float(input("What is your current weight in kg? "))
one_rep_squat = float(input("What is your current one rep max for squats? (in kg) "))
one_rep_bench = float(input("What is your current one rep max for bench? (in kg) "))
one_rep_deadlift = float(input("What is your current one rep max for deadlift? (in kg) "))
lifts = [one_rep_bench, one_rep_deadlift, one_rep_squat]
total = float(sum(lifts))

    # wilks computation:
if gender == "Male":
    a = -216.0475144
    b = 16.2606339
    c = -0.002388645
    d = -0.00113732
    e = 7.01863E-06
    f = -1.291E-08


else:
    a = 594.31747775582
    b = -27.23842536447
    c = 0.82112226871
    d = -0.00930733913
    e = 4.731582E-05
    f = -9.054E-08


wilks = (total * 500 / (a + b*weight + c*weight**2 + d*weight**3 + e*weight**4 + f*weight**5))




new_client = {"Name": name, "Age":  age,
    "Gender": gender,
    "Weight": str(weight),
    "Squat": str(one_rep_squat),
    "Bench": str(one_rep_bench),
    "Deadlift": str(one_rep_deadlift),
    "Total": str(total),
    "Wilks": str(wilks)}



print("Welcome to Mayhem Coaching, " + name + "!")
print("Here's the information we gathered from you: ")
print(new_client)


    #example of dictionary in list
#{Paul:[69,69,69], relos:[1,2,3], jeb:[6,6,6]}