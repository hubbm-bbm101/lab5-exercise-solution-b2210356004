def ex1(N=int(input("Typer a number:"))):
    total_odd = 0
    total_even = 0
    even_counter = 0
    even_average = 0
    for i in range(1, N + 1):
        if i % 2 == 0:  #if even
            total_even += i
            even_counter += 1
        else:
            total_odd += i  #else it is odd
    even_average = total_even / even_counter
    print("Even Average: ", even_average)
    print("Total of odds:", total_odd)


ex1()