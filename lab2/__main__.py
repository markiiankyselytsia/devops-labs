import argparse
from modules import common, number_printer
import logging

FORMAT = '%(asctime)-15s %(name)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger()
parser = argparse.ArgumentParser(description='Приклад передачі аргументів у Python програму.')
parser.add_argument('-o', '--optional', dest='opt', type=str, help='Цей параметр є вибірковим.')
parser.add_argument('-l', '--logs', dest='logs', action='store_true',
                    help='Якщо виконати команду з цим параметром будуть виводитись логи.')
parser.add_argument('-b', '--bool', dest='bool', type=int,
                    help='Вкажіть 1, щоб вивести парні числа, 0 в іншому випадку.')
parser.add_argument('-i', '--inverse', dest='number', type=float,
                    help='Введіть будь-яке число, щоб знайти його обернене')


def main(text):
    print(f"We are in the {__name__}")
    print(common.get_current_date().now())
    print(common.get_current_platform())
    if text:
        print("З консолі було передано аргумент\n", 10*"=", f">> {text} <<", 10*"=")


def how_to_write_logs():
    logger.info("Тут буде просто інформативне повідомлення")
    logger.warning("Це Warning повідомлення")
    logger.error("Це повідомлення про помилку")


if __name__ == '__main__':
    args = parser.parse_args()
    if args.logs:
        how_to_write_logs()
    elif args.bool is not None:
        number_printer.print_nums(bool(args.bool))
    elif args.number is not None:
        number_printer.inverse(args.number)
    else:
        main(args.opt)

