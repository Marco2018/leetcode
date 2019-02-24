### Code Jam

### Code Jam

##### 常用

```c++
typedef long long ll;
```

##### overflow 范围

```
int  -2147483648～2147483647   10^10
long long的最大值：9223372036854775807
```

##### stdio

```c++
cin>>t;
cout<<x<<endl;
```

##### 二分查找

```c++
while (ub - lb > 0) {
	int t = (ub + lb) / 2;
    if (t==target)break;
    else if(t>target){
	    ub = t;
	}
	else {
		lb = t;
	}
}
while (ub - lb >= 0) {
	int t = (ub + lb) / 2;
    if(t==target) break;
    else if (t>target) {
	    ub = t-1;
	}
	else {
		lb = t+1;
	}
}
```



##### 大整数计算

一定要注意overflow的问题，要及时取mod

例如对于过大的pow(x,y)溢出，自己构造函数计算

```c++
ll pow1(ll x, ll y, ll z) {
	ll t = 1;
	for (ll k = 0; k < y; k++) {
		t = (t*x) % z;
	}
	return t;
}
```

