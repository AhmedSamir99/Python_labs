def bubble_sort(my_list):
    n=len(my_list)
    for i in range(n):
        for j in range(n-i-1):
            if my_list[j]>my_list[j+1]:
                my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
    return list

sorted= bubble_sort([5,2,3,1,4])

