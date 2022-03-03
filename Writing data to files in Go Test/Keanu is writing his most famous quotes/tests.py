import os

from hstest import StageTest, CheckResult, WrongAnswer, TestCase

inputs = [
    "You're breathtaking!\nWake up Samurai! We have a city to burn.\nLose? I don't lose; I win! I'm a lawyer, "
    "that's my job, that's what I do!"
]

# Create new file 'keanu_quotes.txt'
with open("keanu_quotes.txt", "w") as f:
    for i in inputs:
        f.write(i)

FILENAME = "keanu_quotes.txt"


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
