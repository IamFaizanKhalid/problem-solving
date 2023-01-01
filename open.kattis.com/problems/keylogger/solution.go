package main

import (
	"bufio"
	"fmt"
	"os"
)

var mapping = map[string]byte{
	"clank":  'A',
	"bong":   'B',
	"click":  'C',
	"tap":    'D',
	"poing":  'E',
	"clonk":  'F',
	"clack":  'G',
	"ping":   'H',
	"tip":    'I',
	"cloing": 'J',
	"tic":    'K',
	"cling":  'L',
	"bing":   'M',
	"pong":   'N',
	"clang":  'O',
	"pang":   'P',
	"clong":  'Q',
	"tac":    'R',
	"boing":  'S',
	"boink":  'T',
	"cloink": 'U',
	"rattle": 'V',
	"clock":  'W',
	"toc":    'X',
	"clink":  'Y',
	"tuc":    'Z',
}

func main() {
	var n int
	fmt.Scanf("%d", &n)

	var str [100000]byte
	var i int

	var sound string
	var caps, shift bool

	cin := bufio.NewScanner(os.Stdin)

	for ; n > 0; n-- {
		cin.Scan()
		sound = cin.Text()

		v, ok := mapping[sound]
		if ok {
			if caps != shift {
				str[i] = v
			} else {
				str[i] = v + 32
			}
			i++
		} else {
			switch sound {
			case "whack":
				str[i] = ' '
				i++
			case "bump":
				caps = !caps
			case "dink":
				shift = true
			case "thumb":
				shift = false
			case "pop":
				if i > 0 {
					i--
				}
			}
		}
	}

	fmt.Println(string(str[:i]))
}
