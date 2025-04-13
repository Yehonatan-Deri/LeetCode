public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");

        Solution solution = new Solution();

        // make some test
        String test1 = "({[]})";
        String test2 = "({[})";
        String test3 = "({[})]";
        String test4 = "({[})";

        System.out.println("Test 1: " + solution.isValid(test1)); // true
        System.out.println("Test 2: " + solution.isValid(test2)); // false
        System.out.println("Test 3: " + solution.isValid(test3)); // false
        System.out.println("Test 4: " + solution.isValid(test4)); // false
        // test with empty string
        String test5 = "";
        System.out.println("Test 5: " + solution.isValid(test5)); // true
        // test with only opening parentheses
        String test6 = "({[";
        System.out.println("Test 6: " + solution.isValid(test6)); // false
        // test with only closing parentheses
        String test7 = ")}]";
        System.out.println("Test 7: " + solution.isValid(test7)); // false
        // test with only one parentheses
        String test8 = "(";
        System.out.println("Test 8: " + solution.isValid(test8)); // false
        // test with only one closing parentheses
        String test9 = ")";
        System.out.println("Test 9: " + solution.isValid(test9)); // false
    }
}