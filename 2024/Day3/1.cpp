#include <iostream>
#include <regex>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <iterator>

using namespace std;

int main() {
    fstream file;
    file.open("1.txt", ios::in);
    int ans = 0;

    string aline;
    int count = 0;
    while (getline(file, aline)) {
        stringstream ss(aline);
        string line = ss.str();
        std::regex pattern("mul\\((\\d+),(\\d+)\\)");
        auto begin=std::sregex_iterator (line.begin(), line.end(), pattern);
        auto end= std::sregex_iterator();

        std::cout << "All matches:\n";
        vector<int> v1;
        vector<int> v2;
        int sum = 0;

        for( auto it=begin; it!=end; ++it) {
            // it-> captures the first group (\\d+)
            v1.push_back(stoi(it->str(1)));
            // it-> captures the second group (\\d+)
            v2.push_back(stoi(it->str(2)));

        }

        for(int i=0; i<v1.size(); i++) {
            sum += v1[i]*v2[i];
        }
        

        ans += sum;
        
    }

    cout << ans << endl;
}