#include <iostream>
#include <vector>

// Return the index of `target` in a sorted vector, or -1 if not found
int binarySearch(const std::vector<int>& arr, int target) {
    int low = 0;
    int high = static_cast<int>(arr.size()) - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}

int main() {
    std::vector<int> numbers = {2, 5, 8, 12, 16, 23, 38};
    std::cout << "Index of 12: " << binarySearch(numbers, 12) << std::endl;
    std::cout << "Index of 38: " << binarySearch(numbers, 38) << std::endl;
    std::cout << "Index of 2: "  << binarySearch(numbers, 2)  << std::endl;
    return 0;
}
