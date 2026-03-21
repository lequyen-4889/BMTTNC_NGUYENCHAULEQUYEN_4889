class PlayFairCipher:

    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.upper().replace("J", "I") # Chuyển "J" thành "I" trong khóa
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        seen = set()
        matrix = []
        for char in key:
            if char.isalpha()and char not in seen:
                seen.add(char)
                matrix.append(char)

        for char in alphabet:
            if char not in seen:
                matrix.append(char)
        
        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def preprocess_text(self,text):
        text = text.upper().replace("J", "I")
        text = "".join(filter(str.isalpha,text))
        
        pairs = []
        i = 0
        
        while i < len(text):
            a = text[i]
            
            if i + 1 < len(text):
                b = text[i + 1]
                if a==b:
                    pairs.append(a + "X")
                    i += 1
                else:
                    pairs.append(a + b)
                    i += 2
            else:
                pairs.append(a + "X")
                i += 1
        return pairs

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_encrypt(self, plain_text, matrix):
        # Chuyển "J" thành "I" trong văn bản đầu vào
        plain_text = self.preprocess_text(plain_text)
        encrypted_text = ""

        for pair in plain_text:
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        pairs = [cipher_text[i:i+2]for i in range(0, len(cipher_text), 2)]
        decrypted_text = ""
        for pair in pairs:
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1)% 5] + matrix[row2][(col2 - 1) %5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 -1)%5][col1]+matrix[(row2-1)%5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return decrypted_text