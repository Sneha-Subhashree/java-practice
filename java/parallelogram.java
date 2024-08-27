import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int b = sc.nextInt(); 
        int h = sc.nextInt(); 
        if (b < 1 || h < 1) {
            System.out.println("java.lang.Exception: Breadth and height must be positive");
            return;
        }
        int res = b * h;
        System.out.println(res);
    }
}
