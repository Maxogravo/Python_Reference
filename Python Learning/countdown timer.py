from time import sleep 

len = int(input("How long is your timer: "))
len += 1

for x in range(1, len):
    sleep(1)
    print(x)
print("WAKEY WAKEY")