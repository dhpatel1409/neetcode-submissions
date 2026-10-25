class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic={}
        t_dic={}
        if len(s)!=len(t):
            return False
        
        else:
            for i in range(len(s)):
                if s[i] in s_dic:
                    s_dic[s[i]]+=1

                else:
                    s_dic[s[i]]=1
            # for i in range(len(s)):
                if t[i] in t_dic:
                    t_dic[t[i]]+=1

                else:
                    t_dic[t[i]]=1

            # for key,val in s_dic.items():
            #     if key not in t_dic:
            #         return False

            #     if t_dic[key]!=val:
            #         return False

                
            # return True
            return s_dic == t_dic


        

        