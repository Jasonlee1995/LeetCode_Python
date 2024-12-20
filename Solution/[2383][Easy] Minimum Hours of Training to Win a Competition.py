class Solution:
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        answer = 0
        for en, ex in zip(energy, experience):
            if initialExperience <= ex:
                answer += (ex - initialExperience + 1)
                initialExperience += (ex - initialExperience + 1)
            if initialEnergy <= en:
                answer += (en - initialEnergy + 1)
                initialEnergy += (en - initialEnergy + 1)
            
            initialEnergy -= en
            initialExperience += ex
        return answer