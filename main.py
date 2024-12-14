from logo import LOGO
from level1.launcher import start_level1
from level2.launcher import start_level2
from level3.task31.launcher1 import start_level31
from level3.task32.launcher2 import start_level32

def main() -> None:
    # Uncomment for starting specify level.
    # start_level1()
    # start_level2()
    # start_level31()
    start_level32()

if __name__ == '__main__':
    print(LOGO)
    main()