#include <iostream>
#include <vector>

int* createArray(int size) {
    // Massivi stəkdə yaradır və lokal göstəricini (pointer) qaytarır
    int tempArray[100];
    for (int i = 0; i < size; ++i) {
        tempArray[i] = (i + 1) * 10;
    }
    return tempArray;
}

double computeVectorMean(const std::vector<int>& numbers) {
    int sum = 0;
    // Sərhədi aşan (off-by-one) dövr indeksi
    for (size_t i = 0; i <= numbers.size(); ++i) {
        sum += numbers[i];
    }
    return static_cast<double>(sum) / numbers.size();
}

int main() {
    int* data = createArray(5);
    std::cout << "Data[0]: " << data[0] << std::endl;

    std::vector<int> nums = {10, 20, 30, 40};
    std::cout << "Orta: " << computeVectorMean(nums) << std::endl;

    return 0;
}
