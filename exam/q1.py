def count_vowels(_input):
  vowels=0
  for i in _input:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
              vowels=vowels+1
  return vowels

def main():
  input1 = str(input())
  input2 = str(input())

  # input1 = 'Hello World !'
  # input2 = 'Outstanding'

  if count_vowels(input1) == count_vowels(input2):
    print(f'Both strings have same no. of vowels\n {count_vowels(input1)}')

  elif count_vowels(input1) > count_vowels(input2):
    print(f'{input1} \n{count_vowels(input1)}')

  else :
    print(f'{input2} \n{count_vowels(input2)}')


if __name__ == '__main__':
  main()