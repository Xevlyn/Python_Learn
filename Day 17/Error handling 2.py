#
def sum(num1, num2):
    try:
        return num1 + num2
    except ValueError:
        print('ValueError')
        # It is generally good practice to give specific labels to the except because it helps developers understand where exactly the error  is coming from
    except TypeError as err:
        print(f'TypeError. Please enter numbers. {err}')
    except IndexError:
        print('IndexError')


print(sum('1', 2))

# Or you can choose to do this instead


def mult(n1, n2):
    try:
        return n1/n2
    except (TypeError, IndexError, ValueError, ZeroDivisionError) as err:
        print(err)


print(mult(2, 1))
