## Sorting

> Sort implementation in Python

## Demo

Demo on [Repl.it](https://repl.it/@yoginth/sorting)

## Install

```
$ pip install sorting
```

## Usage

```python
import sorting

data = [1, 8, 3, 5, 6, 9, 2, 4]

res = sorting.bubble(data)
print('Bubble Sort      : ', res)

res = sorting.bucket(data)
print('Bucket Sort      : ', res)

res = sorting.comb(data)
print('Comb Sort        : ', res)

res = sorting.counting(data)
print('Counting Sort    : ', res)

res = sorting.maxheap(data)
print('Max Heap Sort    : ', res)

res = sorting.minheap(data)
print('Min Heap Sort    : ', res)

res = sorting.merge(data)
print('Merge Sort       : ', res)

res = sorting.quick(data)
print('Quick Sort       : ', res)

res = sorting.radix(data)
print('Radix Sort       : ', res)

res = sorting.selection(data)
print('Selection Sort   : ', res)

res = sorting.cycle(data)
print('Cycle Sort       : ', res)
"""
Output:
Bubble Sort      :  [1, 2, 3, 4, 5, 6, 8, 9]
Bucket Sort      :  [1, 2, 3, 4, 5, 6, 8, 9]
Comb Sort        :  [1, 2, 3, 4, 5, 6, 8, 9]
Counting Sort    :  [1, 2, 3, 4, 5, 6, 8, 9]
Max Heap Sort    :  [1, 2, 3, 4, 5, 6, 8, 9]
Min Heap Sort    :  [1, 2, 3, 4, 5, 6, 8, 9]
Merge Sort       :  [1, 2, 3, 4, 5, 6, 8, 9]
Quick Sort       :  [1, 2, 3, 4, 5, 6, 8, 9]
Radix Sort       :  [1, 2, 3, 4, 5, 6, 8, 9]
Selection Sort   :  [1, 2, 3, 4, 5, 6, 8, 9]
Cycle Sort       :  [1, 2, 3, 4, 5, 6, 8, 9]
"""
```

## Get Help

There are few ways to get help:

 1. Please [post questions on Stack Overflow](https://stackoverflow.com/questions/ask). You can open issues with questions, as long you add a link to your Stack Overflow question.

 2. For bug reports and feature requests, open issues.

 3. For direct and quick help, you can [email me](mailto://yoginth@zoho.com).

## How to contribute
Have an idea? Found a bug? See [how to contribute][contributing].

Thanks!

## License

[MIT][license]

[LICENSE]: https://yoginth.mit-license.org/
[contributing]: /CONTRIBUTING.md
