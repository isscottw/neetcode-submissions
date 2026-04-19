class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        SPECIAL_CHAR = "#"
        for string in strs:
            encoded_string += str(len(string)) + SPECIAL_CHAR + string
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_list = []
        SPECIAL_CHAR = "#"
        i = 0
        while i < len(s):
            #find len
            cur_len = ""
            while (s[i] != SPECIAL_CHAR):
                cur_len += s[i]
                i+=1
            #skip delimiter
            i+=1
            #find string
            cur_str = s[i:i + int(cur_len)]
            decoded_list.append(cur_str)
            # update index
            i += int(cur_len)
        
        return decoded_list
