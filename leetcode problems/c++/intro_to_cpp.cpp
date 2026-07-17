#include <bits/stdc++.h>

using namespace std;

class solution
{
public:
    int add(int a, int b)
    {
        return a + b;
    }

    int addAllElements(const vector<int> &inputvector)
    {
        int sum = 0;

        for (int i = 0; i < inputvector.size(); i++)
        {
            sum += inputvector[i];
        }

        return sum;
    }

    int addAll(const int arr[])
};

int main()
{
    std::vector<int> vec = {5, 2, 9, 1, 5, 6};

    int numbers[] = {1, 2, 4, 5, 6, 7};

    for (int nums : numbers)
    {
        cout << nums << ",";
    }
    // cout << numbers;

    cout << "\n";
    // now i will rotate the whole array , like the first element goes in the last and the last to the first
    // we will have

    // Sorts in ascending order by default
    std::sort(vec.begin(), vec.end());

    for (int num : vec)
    {
        cout << num << " ";
    }
    solution sol;

    cout << "addition of two numbers";
    cout << sol.add(1, 3) << endl;

    cout << "addition of all the elements in the list";
    cout << sol.addAllElements(vec);

    return 0;
}
