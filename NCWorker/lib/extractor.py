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
            block_obj = block.Block(bl[0],"","")
            print(block_obj.tool_name)

