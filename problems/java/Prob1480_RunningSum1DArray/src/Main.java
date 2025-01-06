class Main {
    public static int[] runningSum(int[] nums) {
        
        int acc = 0;
        int[] runningSumList = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            acc += nums[i];
            runningSumList[i] = acc;
        }
        
        return runningSumList;
    }

    public static void main(String [] args) {
        
        int [] list = {1,1,1,1,1};
        int [] ret = runningSum(list);

        for (int runSum : ret) {
            System.out.println(runSum);
        }
    
    }
}