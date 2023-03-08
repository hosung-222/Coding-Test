def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        x = phone_book[i+1]
        
        if phone_book[i] == x[:len(phone_book[i])]:
            return False
    return True