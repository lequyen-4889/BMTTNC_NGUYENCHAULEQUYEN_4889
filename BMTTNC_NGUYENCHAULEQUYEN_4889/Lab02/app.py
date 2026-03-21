from flask import Flask, render_template, request
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher
from cipher.caesar import CaesarCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


# trang caesar
@app.route("/caesar")
def caesar():
    return render_template("caesar.html")


# encrypt caesar
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():

    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    caesar = CaesarCipher()

    encrypted_text = caesar.encrypt_text(text, key)

    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"


# decrypt caesar
@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():

    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])

    caesar = CaesarCipher()

    decrypted_text = caesar.decrypt_text(text, key)

    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

# Vigenere
# Vigenere Routes
@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

@app.route("/vigenere_encrypt", methods=['POST'])
def vigenere_encrypt():
    # Lấy dữ liệu từ form HTML
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    
    cipher = VigenereCipher()
    # Gọi đúng tên hàm trong class của bạn
    result = cipher.vigenere_encrypt(text, key)
    
    # Trả về kết quả (nên render lại template để hiện kết quả trên giao diện)
    return f"Encrypted: {result}"

@app.route("/vigenere_decrypt", methods=['POST'])
def vigenere_decrypt():
    # Lấy dữ liệu từ form HTML
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    
    cipher = VigenereCipher()
    # Gọi đúng tên hàm trong class của bạn
    result = cipher.vigenere_decrypt(text, key)
    
    # Trả về kết quả
    return f"Decrypted: {result}"

# Rail Fence
@app.route("/railfence")
def railfence():
    return render_template("railfence.html")

@app.route("/rail_encrypt", methods=['POST'])
def rail_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    cipher = RailFenceCipher()
    result = cipher.rail_fence_encrypt(text, key)
    return f"Encrypted: {result}"

@app.route("/rail_decrypt", methods=['POST'])
def rail_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    cipher = RailFenceCipher()
    result = cipher.rail_fence_decrypt(text, key)
    return f"Decrypted: {result}"


# Playfair
@app.route("/playfair_matrix", methods=['POST'])
def playfair_matrix():
    key = request.form['inputKeyMatrix']
    cipher = PlayFairCipher(key)
    matrix = cipher.create_playfair_matrix()
    return str(matrix)


@app.route("/playfair_encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    cipher = PlayFairCipher(key)
    result = cipher.playfair_encrypt(text)
    return result


@app.route("/playfair_decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    cipher = PlayFairCipher(key)
    result = cipher.playfair_decrypt(text)
    return result

# Transposition
@app.route("/transposition")
def transposition():
    return render_template("transposition.html")

@app.route("/trans_encrypt", methods=['POST'])
def trans_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    cipher = TranspositionCipher()
    result = cipher.encrypt(text, key)
    return f"Encrypted: {result}"

@app.route("/trans_decrypt", methods=['POST'])
def trans_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    cipher = TranspositionCipher()
    result = cipher.decrypt(text, key)
    return f"Decrypted: {result}"


#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)