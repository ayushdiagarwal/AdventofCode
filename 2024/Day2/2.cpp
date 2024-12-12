#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <unordered_map>

using namespace std;

template <typename T>
void printVec(vector<T> vec) {
    for(int i=0; i<vec.size(); i++) {
        cout << vec[i] << " ";
    }
    cout << endl;
} 


bool checkValid(vector<int> &v1) {
    printVec(v1);
    bool flag = false;


    vector<int> sorted_v1 = v1; 
    sort(sorted_v1.begin(), sorted_v1.end());

    vector<int> reversed_v1 = sorted_v1; 
    reverse(reversed_v1.begin(), reversed_v1.end());

    if (sorted_v1 == (v1) || reversed_v1 == v1) {
        flag = true;
    }
    int fucked_up = 0;

    if (flag) {
        bool valid = true;
        for(int i=0; i<v1.size()-1; i++) {
            if(abs(v1[i] - v1[i+1]) < 1 || abs(v1[i] - v1[i+1]) > 3) {
                // valid = false;   
                fucked_up++;
                if (fucked_up > 1) {
                    valid = false;
                    break;  
                }
            }
        }
        if (valid) {
            return true;
        }
    }
}

int main() {
    fstream file;
    file.open("Day2-1.txt", ios::in);
    string line;
    int count = 0;
    while (getline(file, line)) {
        stringstream ss(line); 
        int word;
        vector<int> v1;
        while (ss >> word) {
            v1.push_back(word);
        }  

        if (checkValid(v1)) {
            count++;
        };

    cout << count << endl;
    return 0;

    }
}