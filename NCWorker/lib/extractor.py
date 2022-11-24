from lib import block
class DMU:

    def block_extractor(temp_file: list):
        indices = []
        block_indices = []
        blocks = []
        #temp_file = [x.replace('N','') for x in temp_file]
        for str in temp_file:
            if("T" in str and "M13" in str):  
                indices.append(temp_file.index(str))
                print(f"---------{str}  {temp_file.index(str)}")
        count: int = 0
        for ind in indices:
            if(indices.index(ind)==len(indices)-1):
                block_indices.append((ind, len(temp_file)-4))
            else:
                block_indices.append((ind, indices[count+1]))
            count += 1
        print(len(block_indices))
        for block in block_indices:
            blocks.append(temp_file[block[0]-1:block[1]])
        print(blocks[1])
        DMU.block_constructor(blocks)
       
    def block_constructor(blocks):
        
        for bl in blocks:
            tool_num, pre_loader = StringParser.tool_num_finder(bl[1], bl[2])
            diam_cor = StringParser.diam_finder(bl)
            height_cor = (f"H{tool_num}") 
            block_obj = block.Block(bl[0], tool_num,pre_loader, height_cor,diam_cor, bl)
            print(f"{block_obj.tool_name} #{block_obj.tool_num} corrector: {height_cor} {block_obj.diam_cor} {block_obj.pre_loader}")


class StringParser:

    def tool_num_finder(s :str, s2: str) ->int:
        s = s.split(" ")
        s2 = s2.split(" ")
        result = 0
        result2 = 0
        for substr in s:
            if ("T" in substr):
                substr = substr.replace("T", "")
                result = int(substr)
        for substr in s2:
            if ("T" in substr):
                substr = substr.replace("T", "")
                result2 = int(substr)

        return result, result2

    def diam_finder(bl : list) ->bool:
        cor = False
        for b in bl:
            if (("G41" in b) or ("G42" in b)):
                cor = True
        return cor