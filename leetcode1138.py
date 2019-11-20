class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        pos = {}
        for i in range(26):
            r, c = int(i/5), i % 5
            pos[chr(i+97)] = [r,c]
        pos_x, pos_y = 0, 0
        res = ""
        for i in range(len(target)):
            target_pos_x, target_pos_y = pos[target[i]]
            dr, dc = target_pos_x - pos_x, target_pos_y - pos_y
            if target_pos_x == 5 and target_pos_y == 0:
                if dc > 0:
                    res += "R"*dc
                elif dc < 0:
                    res += "L"*(-dc)
                if dr > 0:
                    res += "D"*dr
                elif dr < 0:
                    res += "U"*(-dr)
            else:
                if dr > 0:
                    res += "D"*dr
                elif dr < 0:
                    res += "U"*(-dr)
                if dc > 0:
                    res += "R"*dc
                elif dc < 0:
                    res += "L"*(-dc)
            res += "!"
            pos_x, pos_y = target_pos_x, target_pos_y
        return res
        
        
        
        