package main

import (
    "fmt"
    "sync"
)

func main() {
    fmt.Println("Hello, World!")

    x := 10
    y := 20
    sum := add(x, y)
    fmt.Printf("Sum: %d\n", sum)

    numbers := []int{1, 2, 3}
    for _, number := range numbers {
        fmt.Printf("Number: %d\n", number)
    }

    // Concurrency with Goroutines
    var wg sync.WaitGroup
    wg.Add(2)

    go func() {
        defer wg.Done()
        fmt.Println("Goroutine 1")
    }()

    go func() {
        defer wg.Done()
        fmt.Println("Goroutine 2")
    }()

    wg.Wait()
}

func add(a int, b int) int {
    return a + b
}
