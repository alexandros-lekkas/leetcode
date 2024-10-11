class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_map = {}

        empty = []

        for i, s in enumerate(strs):
            sorted_s = ''.join(sorted(s))

            if s == "":
                empty.append("")
            else:
                if sorted_s in s_map:
                    s_map[sorted_s] += s + " "
                else:
                    s_map[sorted_s] = s + " "

        grouped_list = []

        for k in s_map:
            val = s_map[k]
    
            grouped_list.append(val.strip().split())

        if len(empty) > 0:
            grouped_list.append(empty)
        
        return grouped_list
            

        