class Solution:
	def restoreIpAddresses(self, s: str) -> List[str]:
		n = len(s)
		if n < 4 or n > 12:
			return []

		def getAfterDot(i, dc):
			if i>= n:
				return []

			if dc == 3:
				if int(s[i:]) > 255 or (i!=n-1 and s[i]=='0'):
					return []
				else:
					return [s[i:]]

			ips = [s[i:i+1]+'.'+ip for ip in getAfterDot(i+1, dc+1)]

			if s[i]!='0':
				if i+1<n:
					ips += [s[i:i+2]+'.'+ip for ip in getAfterDot(i+2, dc+1)]
				if i+2 < n and int(s[i:i+3]) < 256:
					ips += [s[i:i+3]+'.'+ip for ip in getAfterDot(i+3, dc+1)]

			return ips


		return getAfterDot(0,0)
    
