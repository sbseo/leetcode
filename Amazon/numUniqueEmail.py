class Solution:
    def numUniqueEmails(self, emails) -> int:
        
        emails = [email.split('@') for email in emails]
        answer = set()
        
        for local, domain in emails:
            name_candidate = list()
            for c in local:
                if c == '+':
                    break
                if not c == '.':
                    name_candidate.append(c)
            answer.add((''.join(name_candidate), domain))
        
        return len(answer)        
    
print(Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))