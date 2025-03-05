class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []

        temp = []
        word_length = 0
        i = 0
        while i < len(words):
            word = words[i]
            if word_length + len(word) + len(temp) <= maxWidth:
                temp.append(word)
                word_length += len(word)
                i += 1
            else:
                extra_space = maxWidth - word_length
                
                line = ""

                if len(temp) == 1:
                    line += temp[0] + " " * extra_space

                else:
                    space_location = len(temp) - 1
                    min_blank, mod_blank = divmod(extra_space, space_location)
                    
                    line = temp[0]
                    for j in range(1, len(temp)):
                        line += " " * min_blank
                        if j <= mod_blank:
                            line += " "
                        line += temp[j]
                
                output.append(line)
                temp = []
                word_length = 0

        output.append(" ".join(temp) + " " * (maxWidth - word_length - len(temp) + 1))

        return output