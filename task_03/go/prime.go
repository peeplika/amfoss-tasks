package main

import "fmt"

func main(){
var n int
fmt.Println("enter a positive number")
fmt.Scanln(&n)
if n <= 0{
fmt.Println("not valid")
}else{
for i:=2;i<n+1;i++{
isprime := true
for j:=2;j<i;j++{
if i%j==0{
isprime = false
break
}
}
if isprime == true {
fmt.Print("\n",i)
}}}
}
