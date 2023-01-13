try:
    import numpy as np

    inst = True
except ModuleNotFoundError:
    con = input(
        """Для работы этого скрипта необходима установленная библиотека Numpy. Команда: pip install numpy
Для закрытия нажмите любую клавишу.\n""")
    inst = False
if inst:
    while True:
        dec = input('Выберите точность:\n1) float64\n2) float32\n')
        if dec.lower() in ['1', 'float64', '64']:
            y = np.array([np.pi / 999, np.pi / 999], dtype=np.float_)
            dec = True
            break
        if dec.lower() in ['2', 'float32', '32']:
            y = np.array([np.pi / 999, np.pi / 999], dtype=np.float32)
            dec = False
            break
        print('Введите 1 или 2')

    print(f'Начальные данные:\ny0={y[0]}\ny1={y[1]}')

    while True:
        n = input('Введите N: ')
        try:
            n = int(n)
            break
        except ValueError:
            print('Введите целое число')

    for i in range(1, n):
        if dec:
            x = np.float_((np.pi - 400 * y[i - 1] - 500 * y[i]) / 99)
        else:
            x = np.float32((np.pi - 400 * y[i - 1] - 500 * y[i]) / 99)
        y = np.append(y, x)
        print(f'y{i + 1}={x}')

    cls = input('Для закрытия нажмите любую клавишу.\n')
