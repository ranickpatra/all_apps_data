import java.util.Scanner;

public class prob_1 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int x = combination(N-1, N-2);

        System.out.println(x * x);


    }

    public static int fact(int x) {
        if (x <= 0)
            return 1;

        int fact = 1;
        for (int i = 1; i <=x ; i++) {
            fact *= i;
        }

        return fact;
    }

    public static int permutation(int x, int r) {
        return fact(x) / fact(x - r);
    }

    public static int combination(int x, int r) {
        return permutation(x, r) / fact(r);
    }




}