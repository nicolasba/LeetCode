import java.util.HashMap;
import java.util.Map;

/*
 * 	Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

	You may assume that each input would have exactly one solution, and you may not use the same element twice.

	You can return the answer in any order.
 */
public class Main {

	public static void main(String[] args) {
		/*
		 * Input: nums = [2,7,11,15], target = 9 
		 * Output: [0,1] Output: Because nums[0] + nums[1] == 9, we return [0, 1].
		 */
		
		int nums[] = {2,7,11,15};
		int sol1[] = twoSumBrute(nums, 9);
		int sol2[] = twoSumHashTable(nums, 9);
		
		System.out.println(sol1[0] + " " + sol1[1]);
		System.out.println(sol2[0] + " " + sol2[1]);
		

	}

	// Brute force approach
	public static int[] twoSumBrute(int[] nums, int target) {

		for (int i = 0; i < nums.length; i++)
			for (int j = i + 1; j < nums.length; j++) {
				if (nums[i] + nums[j] == target)
					return new int[] { i, j };
			}

		return null;
	}

	// One-pass hash table
	public static int[] twoSumHashTable(int[] nums, int target) {
		Map<Integer, Integer> map = new HashMap<>();
		for (int i = 0; i < nums.length; i++) {
			int complement = target - nums[i];
			if (map.containsKey(complement)) {
				return new int[] { map.get(complement), i };
			}
			map.put(nums[i], i);
		}
		throw new IllegalArgumentException("No two sum solution");
	}

}
