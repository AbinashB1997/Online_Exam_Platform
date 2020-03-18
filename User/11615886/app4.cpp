#include<bits/stdc++.h>

using namespace std;

typedef struct Node {
    int data;
    Node * left;
    Node * right;
    Node (int d) {
        data = d;
        left = right = NULL;
    }
} Node;

Node * BuildTree(vector<int> &arr, int start, int end) {
    if(start > end) {
        return NULL;
    }
    Node * root, * tmp;
    tmp = new Node(arr[start]);
    tmp->left = BuildTree(arr, 2 * start + 1, end);
    tmp->right = BuildTree(arr, 2 * start + 2, end);
    return tmp;
}

void inorder(Node * root) {
    if(root) {
        inorder(root->left);
        cout << root->data << ' ';
        inorder(root->right);
    }
}

int main() {
    int tt; cin >> tt;
    while(tt--) {
        int size; cin >> size;
        vector<int> arr(size);
        for(int i = 0; i < size; i++) {
            cin >> arr[i];
        }
        Node * root = BuildTree(arr, 0, arr.size() - 1);
        inorder(root);
        cout << endl;
    }
}