#include <bits/stdc++.h>

using namespace std;



int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        bool ok = false;
        vector<int> a(n);
        for(int i = 0;i<n;i++){
            cin>>a[i];
        }
        for(int i = 0;i<n;i++){
            if(count(a.begin(),a.end(),a[i])>1){
                cout<<a[i]<<endl;
                ok = true;
                break;
            }
        }
        if(!ok) cout<<"NO"<<endl;
    }
    return 0;
}