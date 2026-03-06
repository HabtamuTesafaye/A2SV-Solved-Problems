class Solution:
    def compress(self, chars: List[str]) -> int:
        write_position = 0  
        read_position = 0  
        
        while read_position < len(chars):
            current_char = chars[read_position]
            char_count = 0
            
            # Count consecutive occurrences of the current character
            while read_position < len(chars) and chars[read_position] == current_char:
                char_count += 1
                read_position += 1
            
            # Write the character to the compressed position
            chars[write_position] = current_char
            write_position += 1
            
            # If count > 1, write the count as individual digits
            if char_count > 1:
                for digit in str(char_count):
                    chars[write_position] = digit
                    write_position += 1
        
        return write_position