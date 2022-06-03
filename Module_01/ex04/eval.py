class Evaluator:

    @staticmethod
    def arg_checker(coeff: list, words: list) -> bool:
        if not isinstance(words, list) or not isinstance(coeff, list):
            return False
        elif len(words) != len(coeff) or len(words) == 0:
            return False
        elif not all(isinstance(w, str) for w in words):
            return False
        elif not all(isinstance(n, float) for n in coeff):
            return False
        else:
            return True

    @staticmethod
    def zip_evaluate(coeff: list, words: list) -> int:
        if not Evaluator.arg_checker(coeff, words):
            return -1
        else:
            return sum(c * len(w) for c, w in zip(coeff, words))

    @staticmethod
    def enumerate_evaluate(coeff: list, words: list):
        if not Evaluator.arg_checker(coeff, words):
            return -1
        else:
            return sum(coeff * len(words[c]) for c, coeff in enumerate(coeff))


if __name__ == '__main__':
    print("<-------------ERRORS------------->")
    words = ["Le", "Lorem", "Ipsum", "est"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0]
    print(Evaluator.zip_evaluate(coefs, words))
    words = []
    coefs = [1.0, 2.0, 1.0, 4.0]
    print(Evaluator.zip_evaluate(coefs, words))
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = []
    print(Evaluator.zip_evaluate(coefs, words))
    words = []
    coefs = []
    print(Evaluator.zip_evaluate(coefs, words))

    print("<-------------ZIP------------->")
    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print(Evaluator.zip_evaluate(coefs, words))
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))
    print("<-------------ENUM------------->")
    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print(Evaluator.enumerate_evaluate(coefs, words))
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.enumerate_evaluate(coefs, words))
