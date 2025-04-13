import java.util.Stack;
import java.util.Map;

public class Solution {
    // Time complexity: O(n)
    // Space complexity: O(n)

    // create a map to store the pairs of parentheses
    private static final Map<Character, Character> parMap = Map.of(
            '(', ')',
            '[', ']',
            '{', '}');

    public boolean isValid(String s) {
        // create a stack for the parentheses
        Stack<Character> stack = new Stack<>();
        char[] sArr = s.toCharArray();

        for (char c : sArr){
            if (parMap.containsKey(c))
                stack.push(c);

            else{
                // if the stack is empty we got closing with no opening
                if (stack.isEmpty())
                    return false;

                // check the top of the stack
                char top = stack.pop();

                // if the open and closing parentheses do not match
                if (parMap.get(top) != c)
                    return false;
            }
        }

        return stack.isEmpty();
    }
}
//
//extends for class
//
//implement for interface
//
//what is the difference ?
//
//interface is a contract, there is no logic, a list of methods needed to do