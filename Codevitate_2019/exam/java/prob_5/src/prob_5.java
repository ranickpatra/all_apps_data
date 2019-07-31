import java.util.ArrayList;
import java.util.Scanner;

public class prob_5 {

    static  int[] N;
    static int[][] monkey = new int[10][];
    static int[] timing;


    public static void main(String[] atgs) {

        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        N = new int[t];
        for (int i=0; i<t; i++) {
            N[i] = scanner.nextInt();
            monkey[i] = new int[N[i]];
            for (int j = 0; j < N[i]; j++) {
                monkey[i][j] = scanner.nextInt();
            }
        }

        for (int i=0; i<t; i++){
            System.out.println(calculate_pos(monkey[i]));
        }

    }


    public static int lcm(int x, int y) {
        int greater;
        if (x > y)
            greater = x;
        else
            greater = y;

        int lcm;
        while(true) {
            if((greater % x == 0) && (greater % y == 0)){
                lcm = greater;
                break;
            }
            greater += 1;
        }

        return lcm;

    }


    public static int calculate_pos(int[] mon) {
        timing = new int[mon.length];
        aa[] ss = new aa[mon.length];

        for (int i=0; i< mon.length; i++) {
//            int desired = i;
//            int current = i;
//            int count = 0;
//            while(true) {
//                count += 1;
//                current = mon[current] - 1;
//                if (current == desired) {
//                    timing[i] = count;
//                    break;
//                }
//            }
            ss[i] = new aa();
            ss[i].start(i, mon);





        }
        class aa extends Thread {

            int desired;
            int current;
            int count = 0;
            int[] mon;


            public void start(int i, int[] mon) {
                desired = current = i;
                this.mon = mon;
                this.run();

            }
            @Override
            public void run() {
                while(true) {
                    count += 1;
                    current = mon[current] - 1;
                    if (current == desired) {
                        timing[desired] = count;
                        break;
                    }
                }
            }
        }


        for (int i = 0; i < mon.length; i++) {
            try {
                ss[i].join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        ArrayList<Integer> alist = new ArrayList<>();
        for (int i = 0; i < timing.length; i++) {
            if (!alist.contains(timing[i])) {
                alist.add(timing[i]);
            }
        }

        int ll = 1;
        for ( int x: alist) {
            ll = lcm(ll, x);
        }

        return  ll;
    }





}
