package main

import (
    "fmt"
)

func main() {
    var N, E, K int
    fmt.Scanf("%d", &N)
    fmt.Scanf("%d", &E)

    var presentArr [101]int

    var persons [101]map[int]bool
    for i, _ := range persons {
        persons[i] = make(map[int]bool, E)
    }

    for e := 0; e < E; e++ {
        fmt.Scanf("%d", &K)

        present := presentArr[:K]

        isBard := false
        for k := 0; k < K; k++ {
            fmt.Scanf("%d", &present[k])
            if present[k] == 1 {
                isBard = true
            }
        }

        if isBard {
            //  fmt.Println(present)
            for _, p := range present {
                m := persons[p]
                m[e] = true
                persons[p] = m
                // fmt.Printf("%d - %+v\n",p,persons)
            }
        } else {
            m := make(map[int]bool, E)
            for _, p := range present {
                for v, e := range persons[p] {
                    if e {
                        m[v] = e
                    }
                }
            }
            for _, p := range present {
                x := persons[p]
                for i := range x {
                    delete(x, i)
                }
                for v, e := range m {
                    x[v] = e
                }
                persons[p] = x
            }
        }

        // fmt.Printf("%+v\n",persons)
    }

    //  fmt.Printf("............\n")
    //  fmt.Printf("%+v",persons)

    maxSongs := len(persons[1])

    for i, p := range persons {
        if len(p) == maxSongs {
            fmt.Println(i)
        }
    }
}
