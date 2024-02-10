import java.util.*;
class prime{
public static void main(String[] args){
Scanner sc = new Scanner(System.in);
int i,j,n;
System.out.print("enter a positive number : ");
n = sc.nextInt();
if (n<=0){
System.out.print("not valid");
}else{
for (i=2;i<n+1;i++){
boolean isprime=true;
for (j=2;j<i;j++){
if (i%j == 0){
isprime = false;
break;
}}
if (isprime == true){
System.out.printf("%d ",i);
}
}
}}}


