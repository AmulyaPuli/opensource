import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt(); 
        int z = sc.nextInt(); 
        int a = x * y;
        int b = z * 1440;
        if(a<=b) {
            System.out.println("YES");
        }
        else {
            System.out.println("NO");
        }
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    }
}
