from flask import Flask, render_template
from random import sample

cat = Flask(__name__)


@cat.route("/")
def home():
    return "<h1>Hello Flask!</h1>"


@cat.route("/about")
def about_page():
    return render_template("pages/about.html")


@cat.route("/lottery")
def lottery():
    lottery_numbers = number_generator(6)
    return render_template("lottery.html", lottery_numbers=lottery_numbers)


def number_generator(n):
    numbers = range(1, 50)

    return sorted(sample(numbers, n))


# def number_generator(n):
#     all_numbers = set(range(1, 50))
#     excluded_numbers = set([9, 5, 2, 7])
#     numbers = list(all_numbers - excluded_numbers)

#     return sorted(sample(numbers, n))


# def number_generator(n):
#     odd_nums = list(range(1, 50, 2))
#     even_nums = list(range(2, 50, 2))

#     all_nums = []
#     for _ in range(n):
#         if random() > 0.7:
#             all_nums.append(choice(odd_nums))
#             odd_nums.remove(all_nums[-1])
#         else:
#             all_nums.append(choice(even_nums))
#             even_nums.remove(all_nums[-1])

#     return sorted(all_nums)

if __name__ == "__main__":
    cat.run(port=9527, debug=True)
