from tools.numbers.simp import add, subtract,check_simp_first_flag
from tools.numbers.comp import sum_of_digits, is_palindrome
from tools.col import myzip, it_a, it_b
from tools.numbers.flag import check_simp_first_flag, check_simp_two



def main():
    global check_simp_first_flag
    global check_simp_two
    try:
        print(add(1, 2))
        print(sum_of_digits(12345))
        print(myzip(it_a, it_b))
        print(subtract(1, 2))
        print(is_palindrome(121))


    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()