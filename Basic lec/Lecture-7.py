# file i/o in python

'''
    1. Text files (char)
    2. Binary files
                        '''
## "r" reading
# f = open("demo.txt","r")
# data=f.read()
# print(type(data))
# print(data)
# print(f.readline())




## "w" writing file
f = open("demo.txt","w")
f.write("i want to add something new .")
# "x" creatnew and open it with writing
# "a" open for writing appending from end
# "b" binary mode
# "t" text mode
# "+" add a disc file for updating (reading and writing)


f.close() # we have to close file all the time
# ==========================================
# 1. WRITE METHODS (फाइल में लिखना)
# ==========================================

# 'with' का इस्तेमाल करने से फाइल अपने आप बंद (close) हो जाती है
with open("demo.txt", "w", encoding="utf-8") as file:
    # write(): एक सिंगल स्ट्रिंग (लाइन) लिखने के लिए
    file.write("Hello World!\n")
    file.write("Welcome to Python File Handling.\n")
    
    # writelines(): लिस्ट के रूप में एक साथ कई लाइनें लिखने के लिए
    lines_list = ["Line 3: Learn Python.\n", "Line 4: Code daily.\n"]
    file.writelines(lines_list)

print("--- फाइल सफलतापूर्वक बन गई है ---")


# ==========================================
# 2. READ METHODS (फाइल से डेटा पढ़ना)
# ==========================================

with open("demo.txt", "r", encoding="utf-8") as file:
    # मेथड A: read() - पूरी फाइल को एक साथ एक स्ट्रिंग में पढ़ना
    # content = file.read()
    # print(content)
    
    # मेथड B: readline() - एक बार में केवल एक लाइन पढ़ना
    first_line = file.readline()
    print("पहिली लाइन:", first_line.strip()) # strip() एक्स्ट्रा स्पेस/न्यूलाइन हटाता है
    
    # मेथड C: readlines() - बची हुई सभी लाइनों को एक 'List' में बदलना
    remaining_lines = file.readlines()
    print("बाकी लाइनें (List फॉर्मेट में):", remaining_lines)


# ==========================================
# 3. POSITION METHODS (फाइल में कर्सर की जगह जानना)
# ==========================================

with open("demo.txt", "r", encoding="utf-8") as file:
    print("\n--- कर्सर पोजीशन टेस्ट ---")
    
    file.read(5)  # शुरुआती 5 कैरेक्टर पढ़े
    
    # tell(): कर्सर अभी किस नंबर (बाइट) पर है, यह बताता है
    current_pos = file.tell()
    print(f"कर्सर अभी {current_pos} नंबर पोजीशन पर है।")
    
    # seek(position): कर्सer को वापस किसी भी नंबर पर भेजने के लिए
    file.seek(0)  # कर्सर को वापस शुरुआत (0) पर भेज दिया
    print("seek(0) के बाद पहली लाइन फिर से:", file.readline().strip())


# ==========================================
# 4. APPEND METHOD (पुराना डेटा बिना मिटाए नया लिखना)
# ==========================================

with open("demo.txt", "a", encoding="utf-8") as file:
    # यह फाइल के सबसे नीचे जुड़ जाएगा
    file.write("Line 5: This is appended text.\n")


# ==========================================
# 5. BONUS: फाइल को मैन्युअली बंद करना
# ==========================================
# अगर आप 'with' इस्तेमाल नहीं करते, तो close() करना जरूरी है:
f = open("demo.txt", "r")
# अपना कोड यहाँ लिखें...
f.close() # फाइल को मेमोरी से फ्री करने के लिए





