from typing import List

import cProfile
import math
class Solution:
	def reverse_digit(self, n):		
		rev = 0
		while n > 0:
			digit = n % 10
			rev = (rev * 10) + digit
			n = n // 10
		return rev
	
	def power1(self,N,R):
		flag =0
		Original_rem = 1
		while (R>0):
			if (R%2 == 0):
				R = R//2
				N  =  N * N
			else:
				flag =1
				Original_rem = Original_rem * N
				print("Original_rem :", Original_rem)
				R = R-1 
		if flag == 1:
			N = Original_rem
		return N%(10**9 + 7)


	def power(self, N, R):
		MOD = 10**9 + 7  # Modulo constant
		result = 1       # To hold the final result
		base = N         # The current base valu        
		while R > 0:
			if R % 2 == 1:
				result = (result * base) % MOD     
			base = (base * base) % MOD
			R = R // 2
		return result
	
	def gcd1(self, a, b):
		result = min(a, b)
		while result:
			if a % result == 0 and b % result == 0:
				break
			result =  result -1
		return result
	def gcd(self, a, b):
		if (a == 0):
			return b
		if (b == 0):
			return a
		if (a > b):
			return self.gcd(a%b, b)
		return self.gcd(a, b%a)
	def printDivisors(self, n:int)-> List[int]:
		divisor_list = []

		for i in range(1, 10**5):
			if n % i == 0:
				divisor_list.append(i)
		return divisor_list
	def isPrime (self, N):
		count = []
		for i in range(2, int(math.sqrt(N)) + 1):
			if (N %i == 0 and not i == N):
				count.append(i)
		if len(count) >=1 or N ==1:
			return 0
		else:
			return 1		
	def armstrongNumber (self, n):
		result = 0
		original_num =  n
		while n>0:
			digit = n%10
			result = result + digit **3
			n = n // 10
			#print(digit,  result, n)
		if result == original_num:
			return True
		else:
			return False
	def is_palindrome(self, n):
		result = 0
		original_num =  n
		while n>0:
			digit = n%10
			result = result * 10 + digit
			n = n // 10
			#print(digit,  result, n)
		if result == original_num:	
			return "Yes"
		else:
			return "No"
	def isPerfectNumber(self, N):
		result = 1
		print("NNNN", N)
		for i in range(2, int(math.sqrt(N))+1):
			print("i: ", i)
			if N%i == 0 :
				result = result+i
				if i != N // i:
					result += N // i
		print("RESULT:", result)
		if result == 1:
			return 0
		elif result == N:
			return 1 



		
	
#
#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
	ob = Solution();
	N= 98

	R =56
	#N = 955491230
	#R= 4412
	Number = 10
	primeN = 15
	amnum = 153
	palN = 555
	perN = 1000000000000

	ans = ob.power(N, R)
	gcd_value = ob.gcd(N, R)
	div_Value = ob.printDivisors(Number)
	prime = ob.isPrime(primeN)
	amstong_num = ob.armstrongNumber(amnum)
	pal_num = ob.is_palindrome(palN)
	perfect_num = ob.isPerfectNumber(perN)
	print("The Final answer is :", ans, gcd_value, div_Value, prime, amstong_num, pal_num, perfect_num)


if __name__ == '__main__':
	#n = int(input("Enter a number :"))
	cProfile.run('main()', sort = 'tottime')


# } Driver Code Ends