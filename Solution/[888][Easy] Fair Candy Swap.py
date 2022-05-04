class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        difference_candy = sum(aliceSizes) - sum(bobSizes)
        alice_set = set(aliceSizes)
        for bob_candy in bobSizes:
            alice_candy = bob_candy + difference_candy / 2
            if alice_candy in alice_set:
                return (int(alice_candy), bob_candy)
