#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    fstream file;
    file.open("Day1.txt", ios::in);
    int word;
    vector<int> v1, v2;
    int count = 0;
    while (file >> word) {
        if (count % 2 == 0) {
            v1.push_back(word);
        }
        else {
            v2.push_back(word);
        }
        count++;
    }

    unordered_map<int, int> freq;
    for(int i=0; i<v1.size(); i++) {
        freq[v2[i]]++;
    }

    int ans = 0;
    for(int i=0; i<v1.size(); i++) {
        cout << freq[v1[i]] << endl;
        ans += freq[v1[i]]*v1[i];
    }

    cout << ans << endl;


    return 0;
}