# Read from the file words.txt and output the word frequency list to stdout.
grep -oE '[a-z]+' words.txt | sort | uniq -c | sort -nr | awk '{print $2" "$1}'

#grep表示搜索
# grep -oE '[a-z]+'会输出文本中的单词
#shaoping@ubuntu3:~$ echo this is a test line | grep -o "[a-z]+"  (少了E没有输出，少了o按照整句话输出)
#shaoping@ubuntu3:~$ echo this is a test line | grep -E "[a-z]+"
#this is a test line
# | 的意思是前面的输出作为后面的输入
#sort则按照字母顺序进行排序
# uniq -c则会对其按照次数进行统计
#sort -nr 按照次数进行统计 反向
#awk 输出 print $2" "$1  输出第二列 输出“ ” 输出第一列
