# py_file_input.py - 파일 입출력

# a(추가), r(읽기), x(쓰기)
f = open('./day02/textfile.txt', mode='w', encoding="utf-8")

f.write('저는 한국사람입니다.\n')
f.write('저는 남자입니다.\n')


f.close()

print('텍스트 파일이 생성되었습니다.')

#읽기
f = open('./day02/textfile.txt', mode='r', encoding="utf-8")

while True:
  line = f.readline()
  if not line: break
  
  print(line)


f.close()
