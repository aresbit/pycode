

def reverse(lst):
    if lst == []:
        return []
    else:
        hd, tl = lst[0], lst[1:]
        return reverse(tl) + [hd]



def reverse1(lst):
    return reverse_acc(lst, [])

def reverse_acc(lst, acc):
    if lst == []:
        return acc
    else:
        hd, tl = lst[0], lst[1:]
        return reverse_acc(tl, [hd] + acc)

def reverse_iter(lst):
    acc = []
    for i in lst:
        acc = [i] + acc
    return acc


if __name__ == '__main__':
    print(reverse([1, 2, 3, 4, 5]))
    print(reverse_iter([1, 2, 3, 4, 5]))
    print(reverse1([1, 2, 3, 4, 5]))
    
