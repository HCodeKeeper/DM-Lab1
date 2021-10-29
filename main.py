#created by Ivannikov Maksym, Sobol Oleg, Mendyk Sofiia

from own_set import *

arrayA = [int(item) for item in input("Enter the list items for array A : ").split()]
arrayB = [int(item) for item in input("Enter the list items for array B : ").split()]


def decart_print(result_array):
    print("decart: ")
    for i in result_array:
        for j in i:
            print(j, end="; ")
        print("\n")
    print("~~~~~Completed~~~~~")


print("unification: ")
print(unification(arrayA, arrayB))
print("intersection: " )
print(intersection(arrayA, arrayB))


print("difference: " )
print(difference(arrayA, arrayB))

print("supplementing: ")
print(supplementing(arrayA))

print("symetrical_difference: " )
print(symetrical_difference(arrayA, arrayB))

decart_print([decart(arrayA, arrayB)])

print("a is a subset of set b" if subset(arrayA, arrayB) else "a is not a subset of set b")
print("a equals b" if is_equal(arrayA, arrayB) else "a doesn't equal b")


print("a translated(bit): " )
print(translate_to_bit(arrayA))


print("b translated(bit): " )
print(translate_to_bit(arrayB))

print()

print("bit unification: ")
print(unification_bit(arrayA, arrayB))


print("bit intersection: ")
print(intersection_bit(arrayA, arrayB))


print("bit difference: ")
print(difference_bit(arrayA, arrayB))


print("bit symetrical difference: ")
print(symetrical_bit_difference(arrayA, arrayB))