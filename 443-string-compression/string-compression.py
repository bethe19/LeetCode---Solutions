class Solution:
    def compress(self, chars: List[str]) -> int:
        counter = 1
        index = 0
        for i in range(1,len(chars)+1):
            if i == len(chars):
                s = str(counter)
                if counter > 1:
                    for j in s:
                        index += 1
                        chars[index] = j
                index += 1
                break
            if chars[i] == chars[i-1]:
                counter += 1
                continue
            else:
                s = str(counter)
                if counter > 1:
                    for j in s:
                        index += 1
                        chars[index] = j
                index += 1
                chars[index] = chars[i]
                counter = 1
        
        return index


