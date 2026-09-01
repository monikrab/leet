class Solution:
    def romanToInt(self, s):
        symbols = list(s)
        value = 0

        # only powers of 10 of the same magnitude
        # can be subtracted from any numeral
        pre_M_D = 'C'
        pre_C_L = 'X'
        pre_X_V = 'I'

        def match_symbol(sym, value=0):
            match sym:
                 case 'M': value = 1000
                 case 'D': value = 500
                 case 'C': value = 100
                 case 'L': value = 50
                 case 'X': value = 10
                 case 'V': value = 5
                 case 'I': value = 1   
            return value         

        while symbols:
            if len(symbols) > 1:
                to_num = [symbols[0], symbols[1]]

                if to_num[0] == pre_M_D and to_num[1] == 'M':
                    value += 900; del symbols[0:2]; continue
                elif to_num[0] == pre_M_D and to_num[1] == 'D':
                    value += 400; del symbols[0:2]; continue

                if to_num[0] == pre_C_L and to_num[1] == 'C':
                    value += 90; del symbols[0:2]; continue
                elif to_num[0] == pre_C_L and to_num[1] == 'L':
                    value += 40; del symbols[0:2]; continue

                if to_num[0] == pre_X_V and to_num[1] == 'X':
                    value += 9; del symbols[0:2]; continue
                elif to_num[0] == pre_X_V and to_num[1] == 'V':
                    value += 4; del symbols[0:2]; continue               

                # if it hasn't been continued, there are no pre_ symbols
                value += match_symbol(to_num[0])
                symbols.pop(0)

            else:
                value += match_symbol(symbols[0])
                symbols.pop(0)
        
        return value
