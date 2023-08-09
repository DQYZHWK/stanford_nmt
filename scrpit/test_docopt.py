"""
Usage:
  my_program.py <input_file> [--output=<output_file>]
"""


## add to ai_coding 


class A:
  @staticmethod
  def getinfo():
    return "yes"

from docopt import docopt
def main():
    print(A.getinfo())
    print("_________________222")
    arguments = docopt(__doc__)
    input_file = arguments['<input_file>']
    output_file = arguments['--output']
    print(input_file)
    print("_______________________")
    print(output_file)
    # 现在可以使用 input_file 和 output_file 参数进行处理

if __name__ == '__main__':
    main()
