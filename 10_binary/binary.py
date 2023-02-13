# for my reference in converting a decimal to binary
def decimal_to_binary(num):
  if num >= 1:
    decimal_to_binary(num // 2)
  print(num % 2, end = '')

if __name__ == '__main__':
    n = int(input().strip())
    
    count = 0
    maximum = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
            if count > maximum:
                maximum = count
        else:
            count = 0
        n //= 2
    print(maximum)
