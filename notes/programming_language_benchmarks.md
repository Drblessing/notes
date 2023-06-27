# Programming language benchmarks

Simple benchmarks for various programming languages. Just counting to gargantuan numbers.

---

## Results

| Language | Time (s) | Number | Speed (#/s) | Multiplier |
| -------- | -------- | ------ | ----------- | ---------- |
| Go       | 31.16s   | 1e11   | 3.2e+09     | 250x       |
| Rust     | 16.69s   | 1e10   | 6.0e+08     | 46x        |
| Python   | 79.73s   | 1e9    | 1.3e+07     | 1x         |

---

## Code

### Go

```go
package main

import "fmt"

func main() {
	var counter int64
	for counter = 0; counter < 100_000_000_000; counter++ {
	}
	fmt.Println(counter)
}
```

### Rust

```rust
fn main() {
    let mut counter: u128 = 0;
    while counter < 10_000_000_000 {
        counter += 1;
    }
    println!("{}", counter);
}

```

### Python

```python
i = 0
while i < 1_000_000_000:
    i += 1
print(i)
```
