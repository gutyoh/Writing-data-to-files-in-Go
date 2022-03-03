import os

from hstest import StageTest, CheckResult, WrongAnswer, TestCase

existing_menu = [
    "Krabby Pattie $2.00\n "
    "Krusty Combo $3.99\n "
    "Krusty Deluxe $3.00\n "
    "Seaweed Salad $1.50\n "
    "Coral Bits $1.95\n"
]

# Create new file 'galley_grub.txt' and add the lines of "existing_menu" to it
with open("galley_grub.txt", "w") as f:
    for lines in existing_menu:
        f.write(lines)

inputs = [
    "Krabby Pattie $2.00\n "
    "Krusty Combo $3.99\n "
    "Krusty Deluxe $3.00\n "
    "Seaweed Salad $1.50\n "
    "Coral Bits $1.95\n"
    "Kelp Shake $2.00"
]

FILENAME = "galley_grub.txt"

class TestAdmissionProcedure(StageTest):
    def generate(self):
        return [TestCase(stdin=[test], attach=[test]) for test in inputs]

    def check(self, reply: str, attach: list):
        if not os.path.exists(FILENAME):
            raise WrongAnswer(f"Cannot find file {FILENAME}")

        with open(FILENAME, "r") as f:
            content = f.read().strip()
            if content != attach[0]:
                raise WrongAnswer(
                    f'Invalid content of {FILENAME} file, got "{content}" want "{attach[0]}"'
                )

        return CheckResult.correct()


if __name__ == '__main__':
    TestAdmissionProcedure().run_tests()
