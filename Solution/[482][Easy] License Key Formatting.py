class Solution:
    def licenseKeyFormatting(self, s, k):
        letters = s.replace('-', '').upper()
        remain = len(letters) % k
        answer = []
        if remain: answer.append(letters[:remain])
        for i in range(remain, len(letters), k): answer.append(letters[i:i+k])
        return '-'.join(answer)
