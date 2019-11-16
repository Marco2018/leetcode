<https://codingcompetitions.withgoogle.com/kickstart/faq>

推荐使用C++

Then, we will run your code against Test Set 1. If it passes every test in that test set (within time and memory limits, etc.), we will run it on Test Set 2 (if there is one)

关于输出：

500 与500.0不同，

2.3 与2.3000001 视为相同

##### Input & Out

```c++
 #include <iostream> // includes cin to read from stdin and cout to write to stdout
    using namespace std; 
    int main() {
      int t, n, m;
      cin >> t; // read t. cin knows that t is an int, so it reads it as such.
      for (int i = 1; i <= t; ++i) {
        cin >> n >> m; // read n and then m.
        cout << "Case #" << i << ": " << (n + m) << " " << (n * m) << endl;
      }
      return 0;
    }
```

```python
# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    # This is all you need for most Code Jam problems.
    t = int(input()) # read a line with a single integer
    for i in range(1, t + 1):
      n, m = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
      print("Case #{}: {} {}".format(i, n + m, n * m))
      # check out .format's specification for more formatting options
```



Interactive problem

部分通过test 不会得到分数，只有完整通过一个test set才有分

For each problem, we choose one of the following as your scoring attempt:

- Your latest attempt. In that case, we use the sum of the values of all passed test sets as your point total.
- Your earliest attempt that passed the most Visible Test Sets. In that case, we add up the scores for those passed Visible Test Sets.

We choose the option that gives you the most points.



4 minutes times the total number of penalty attempts