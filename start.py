from enum import Enum
from app.template_methods import Double, SumAscii, Split


class TransformMap(Enum):
    double = Double
    sum_ascii = SumAscii
    split = Split


def main():
    """
        Example of using:

        "Transformator" started!
        Enter read from: text.txt
        Enter write to: result.txt
        Sort types: double, sum_ascii, split
        Enter transform type: split
        End.
    """
    print('"Transformator" started!')

    read_from = input('Enter read from: ')
    write_to = input('Enter write to: ')
    print(f'Sort types: {TransformMap.double.name}, {TransformMap.sum_ascii.name}, {TransformMap.split.name}')
    transform_type = input('Enter transform type: ')

    try:
        program = TransformMap[transform_type].value(read_from=read_from, write_to=write_to)
        program.run()
    except KeyError:
        print(f'"{transform_type}" is wrong transform type, please start program again.')

    print('End.')


if __name__ == '__main__':
    main()
