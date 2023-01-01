package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var N, K int
	fmt.Scanf("%d %d", &N, &K)

	cin := bufio.NewScanner(os.Stdin)
	cin.Split(bufio.ScanWords)

	m := make(map[int][]int, K+1)

	var x int
	for n := 0; n < N; n++ {
		cin.Scan()
		x, _ = strconv.Atoi(cin.Text())

		m[x] = append(m[x], n)
	}

	minSum := getMinDist(m, N, K, m[1][0])
	for _, i := range m[1] {
		sum := getMinDist(m, N, K, i)
		if sum < minSum {
			minSum = sum
		}
	}

	fmt.Println(1 + minSum)
}

func getMinDist(m map[int][]int, N, K, prevI int) int {
	totalDist := 0

	for k := 2; k <= K; k++ {
		minDist := (N + m[k][0] - prevI) % N
		minI := m[k][0]
		for _, i := range m[k] {
			dist := (N + i - prevI) % N
			if dist < minDist {
				minDist = dist
				minI = i
			}
		}
		totalDist += minDist
		prevI = minI
	}

	return totalDist
}
