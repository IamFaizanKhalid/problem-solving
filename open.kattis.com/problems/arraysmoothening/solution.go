package main

import (
    "bytes"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

func main() {
    var n, k int
    fmt.Scanf("%d %d", &n, &k)

    m := getOccurances()

    var repC [200001]int
    for _, apr := range m {
        repC[apr]++
    }

    for i := 200000; i >= 1; i-- {
        if repC[i] != 0 {
            if repC[i] > k {
                fmt.Println(i)
                return
            } else {
                repC[i-1] += repC[i]
                k -= repC[i]
            }
        }
    }
    
    fmt.Println(0)
}

func getOccurances() map[int]int {
    var x int
    m := make(map[int]int)

    var buf bytes.Buffer
    _, _ = io.Copy(&buf, os.Stdin)

    arr := strings.Fields(buf.String())
    for _, v := range arr {
        x, _ = strconv.Atoi(v)
        m[x]++
    }

    return m
}
