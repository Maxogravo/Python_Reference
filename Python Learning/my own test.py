from time import sleep

act = input("Activate Launch Sequence: ")

if act == "y":
    numbers = [1,2,3,4,5]

    for number in reversed(numbers):
        print(number)
        sleep(1)
    print("Launched")

else:
    print("Activation dismissed")