def is_palindrome(s):

	if (len(s) == 0) or (len(s) == 1):
		return True
	else:
		if s[0] == s[-1]:
			return is_palindrome(s[1:-1])
	
		else:   
			return False
				




while True:
	input_str = input("문자열을 입력하세요(Q 입력 시 종료): ")

	if input_str == "Q":
		break


	#함수 실행
	palindrome_output = is_palindrome(input_str)

	if palindrome_output:
		print(f"{input_str}은 palindrome 입니다.\n")
	else:
		print(f"{input_str}은 palindrome이 아닙니다.\n")
