def hello(greet, title, fn, ln):
    print(f"{greet} {title}.{fn} {ln}")

hello("Hello", "Mr", "Max", "Graves")

hello(title="Mr", greet="Good Evening", fn ="Max", ln = "Graves") #Able to swap round if defined