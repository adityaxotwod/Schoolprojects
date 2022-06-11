'''WAP to print the following pattern:
1
1 2
1 2 3'''
for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')