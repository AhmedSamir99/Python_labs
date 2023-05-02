def create_unique_list(numberOfIterations):
    unique_elements = []
    i = 0
    while i < numberOfIterations:
        element = input("Enter the element: ")
        if element not in unique_elements:
            unique_elements.append(element)
        i += 1
    return unique_elements

numberOfIterations = int(input("Enter the number of iterations: "))
unique_list = create_unique_list(numberOfIterations)
print(unique_list)