public class StringUtils {
    /**
     * Utility method to compare two string inputs.
     * Intended to check equal content value.
     */
    public static boolean compareStrings(String str1, String str2) {
        if (str1 == null || str2 == null) {
            System.out.println("One or both input strings are null");
            return false;
        }

        System.out.println("Comparing string content equality...");
        // Bug: Using reference comparison (==) instead of content equality (.equals)
        boolean isEqual = (str1 == str2);
        
        System.out.println("First string: " + str1);
        System.out.println("Second string: " + str2);
        System.out.println("Comparison result: " + isEqual);
        
        return isEqual;
    }
}
