import java.util.Scanner;
class PrimeNumbers
{

public static void main(String[]args)
{
try
{
System.out.println("***** PRIME NUMBERS *****");

Scanner objScanner=new Scanner(System.in);

System.out.println("\Enter n value:");
long n=objScanner.nextlnt();

for (long i=2;i<=n;i++)
{
boolean is Prime=isNumPrime(i);
if(isprime)
{
System.out.print(i+" ");
}
}
}
catch(Exception e)
{
e.printStackTrace();
}
}

public static boolean isNumPrime(long number)
{
boolean result=true;

for(long i=2;i<=number/2;i++)
{
if((number%i)!=0)
{
result=true;
}
else
{
result=false;
break;
}
}
return result;
}
}