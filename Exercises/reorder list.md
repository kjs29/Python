Create a function called `swap` that takes two argument, `lst` and `order`.

`lst` and `order` are both lists, `lst` is a list to be swapped, and `order` represents the order.

The function returns a reordered list with the order defined in the `order`.

For example,

```py
print(swap(['world', 'hello'],[2, 1]))    # ['hello', 'world']
```

<details>

  <summary>answer</summary>
  
```py
def swap(lst, order):
    dic = {k:v for k,v in zip(order, lst)}
    return [dic[key] for _,key in enumerate(sorted(dic.keys()))]
```

</details>


<details>

  <summary>answer2</summary>
  
```py
def swap(lst, order):
    return [item for _, item in sorted(zip(order, lst))]
```

</details>
