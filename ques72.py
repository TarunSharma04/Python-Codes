try:
    with open('5.txt', 'r') as f:
        f.read()
    with open('6.txt', 'r') as f:
        f.read()
    with open('7.txt', 'r') as f:
        f.read()

except Exception as e:
    print(f"The file is not present. Reason: {e}")

print("Thanks for using this program")