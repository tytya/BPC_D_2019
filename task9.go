/*
Creator: Krylova Elizaveta
*/

package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"sort"
	"strconv"
	"strings"
)

// Symbol is type
type Symbol struct {
	S string
	N int
}

// ByN is type
type ByN []Symbol

func (a ByN) Len() int           { return len(a) }
func (a ByN) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByN) Less(i, j int) bool { return a[i].N > a[j].N }

func main() {
	var STR string
	var SYM []string
	isAlpha := regexp.MustCompile(`^[a-z]+$`).MatchString

	myscanner := bufio.NewScanner(os.Stdin)
	myscanner.Scan()
	STR = myscanner.Text()
	STR = strings.ToLower(STR)

	for _, s := range strings.Split(STR, "") {
		if isAlpha(s) {
			SYM = append(SYM, s)
		}
	}

	sort.Strings(SYM)

	SYMBOLS := []Symbol{}
	var check bool
	s := Symbol{
		S: SYM[0],
		N: 1,
	}

	SYMBOLS = append(SYMBOLS, s)

	for i := 1; i < len(SYM); i++ {
		check = true
		for j := 0; j < len(SYMBOLS); j++ {

			if SYMBOLS[j].S == SYM[i] {
				SYMBOLS[j].N++
				check = false
				break
			}

		}
		if check {
			s := Symbol{
				S: SYM[i],
				N: 1,
			}
			SYMBOLS = append(SYMBOLS, s)
		}
	}
	sort.Sort(ByN(SYMBOLS))
	for i := 0; i < len(SYMBOLS); i++ {
		fmt.Println(SYMBOLS[i].S + ": " + strconv.Itoa(SYMBOLS[i].N))
	}
}
