histogram = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

while True:
    user_input = int(input("Enter a number (1-10, -1 to exit): "))
    
    if user_input == -1:
        break
    
    if 1 <= user_input <= 10:
        histogram[user_input] += 1
    else:
        print("Invalid input. Enter a number in the range 1-10.")

for start, end in [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]:
    count = sum(histogram[i] for i in range(start, end + 1))
    percentage = (count / sum(histogram.values())) * 100 if sum(histogram.values()) != 0 else 0
    print(f"{start} - {end}: {' # ' * count} {percentage:.2f} %")
