def chave_ordenacao(elemento):
    """
    A function that determines the ordering of an element.

    :param elemento: The element to determine the ordering for.
    :type elemento: Any

    :return: True if the element is not equal to 1, False otherwise.
    :rtype: bool
    """
    return elemento != 1

def ordenar_com_1_primeiro(array):
    """
    Sorts the given array in ascending order using the `chave_ordenacao` function as the key for comparison.

    Parameters:
    - array (list): The list to be sorted.

    Returns:
    - list: The sorted list.
    """
    array.sort(key=chave_ordenacao)
    return array

array = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
resultado = ordenar_com_1_primeiro(array)
print(resultado)
