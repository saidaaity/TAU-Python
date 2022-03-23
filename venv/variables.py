def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {} and salary is {} hire date is {}.".format(fname, lname, company, email, *args, kwargs.get("hire_date")))


application("Jess", "Ingrass", "mail @ mail.com",
"TeachCode.org", 75000, hire_date = "September 2010")






