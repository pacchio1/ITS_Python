package main
import ("fmt")
//comment
/* multi
line*/
const PI=3.142
func main() {
  //var arr1 = [...]int{1,2,3}
  //arr2 := [...]int{4,5,6,7,8}
  myslice2 := []string{"Go", "Slices", "Are", "Powerful"}
  fmt.Println(len(myslice2))
  fmt.Println(cap(myslice2))
  fmt.Println(myslice2)
  fmt.Println("Hello Mom!")
}
