from lib import file_reader, extractor

def main():
    # from DMU to Mori
    temp_file = file_reader.Reader.open_file("BPM.30.006.I")
    extractor.DMU.block_extractor(temp_file)
    
    


if __name__ == '__main__':
    main()