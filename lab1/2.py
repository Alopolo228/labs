import itertools

def words_count():
    letters = ['В', 'И', 'Ш', 'Н', 'Я']
    vowels = {'И', 'Я'}
    count = 0
    
    for word in itertools.product(letters, repeat=6):
        if word[0] == 'Ш':
            continue
        if word[-1] in vowels:
            continue
        if word.count('В') > 1:
            continue
        count += 1
    
    return count


def binary_ones():
    a = 4**2014+2**2015-8
    a = bin(a)[2:]
    a = a.count("1")
    return a


def numbers_powers():
    """
    Задача: найти числа N из [400_000_000; 600_000_000] вида N = 2^m * 3^n,
    где m чётное, n нечётное
    """
    result = []
    for m in range(0, 100, 2):
        for n in range(1, 100, 2):
            N = 2**m * 3**n
            if 400000000 <= N <= 600000000:
                result.append(N)
    return sorted(result)

if __name__ == "__main__":
    print("слова:", words_count())
    print("двоичная запись:", binary_ones())
    print("числа N:", numbers_powers())

