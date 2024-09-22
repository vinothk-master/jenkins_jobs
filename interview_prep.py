
class Solution:
	def reverse_digit(self, n):		
		rev = 0
		while n > 0:
			digit = n % 10
			rev = (rev * 10) + digit
			n = n // 10
		return rev
	
	def power(self,N,R):
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


#	def power(self, N, R):
#		MOD = 10**9 + 7  # Modulo constant
#		result = 1       # To hold the final result
#		base = N         # The current base valu        
#		while R > 0:
#			if R % 2 == 1:
#				result = (result * base) % MOD     
#			base = (base * base) % MOD
#			R = R // 2
#		return result
#
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	#n = int(input("Enter a number :"))
	ob = Solution();
	#ans = ob.reverse_digit(n)
	N= 12
	R =21
	ans = ob.power(N, R)
	print(ans)
# } Driver Code Ends