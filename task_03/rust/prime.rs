use std::io;

fn main() {
    let mut input = String::new();

    println!("Enter a positive number :");
    io::stdin().read_line(&mut input).expect("");

    let num: i32 = input.trim().parse().expect("");
    if num <= 0 {
    println!("not valid");
    }else {
    for i in 2 .. num {
    let mut isprime = true;
    for j in 2 .. i {
    if i%j == 0 {
    isprime = false;
    break;
    }}
    if isprime == true {
    println!("{}",i);
    }}}

}


