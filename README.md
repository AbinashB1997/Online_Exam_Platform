$ **INSTRUCTIONS FOR ADMIN**

> Folder Terminology

### PVC (Data/)
* When user will submit the test, a unique folder with their registration number will be created inside the PVC.

* These folder will be further moved to User/ and will be removed from here.

### User/
* This directory is responsible for copying the unique folders(of individual user) from PVC(data/) to User/

### Admin/
* Admin/ is belong to the adminstration. Completely secure. Can not be exposed to outside(users).

* It contains the input files and the output files by problem setters.

* When user submits test, the input files of admin will be tested on the corresponding codes of user and the output will be made available in a sub-directory(/user_out) inside Admin/

* Finally, the task is now reduced so much. Now the task is to compare the user's output with admin's output file.

$ **INSTRUCTIONS FOR USER**

* User should print their output in newline for each test cases

* No need to return anything

* User should have to declare main function. And if he/she wish to make more functions they need to manage them.
> Example-1(Sample)
```
/* Code to add 2 numbers with function*/

#include<bits/stdc++.h>
using namespace std;

int add2Numbers(int a, int b) {
    return a + b;
}

int main()
{
    int tt; // Read input for testcases
    cin >> tt;
    while(tt--) {
        int a, b; // Read input for numbers
        cin >> a >> b;
        cout << add2Numbers(a, b) << endl;
    }
    return 0;
}

```
> Example-2(Sample)

```
/* Code to add 2 numbers without function*/

#include<bits/stdc++.h>
using namespace std;

int main()
{
    int tt; // Read input for testcases
    cin >> tt;
    while(tt--) {
        int a, b; // Read input for numbers
        cin >> a >> b;
        cout << a + b << endl;
    }
    return 0;
}

```

* Admin is not managing the main function. So user solely responsible of that part too.

* Users are requested to submit either a fully compiled code/Empty code. Meaning, they can either submit a fully functional code or they can leave the question unanswered.

* Users are requested to take care of newLines ('\n').

> **Instructions regarding newline**
* [*What is a newLine?*](https://en.wikipedia.org/wiki/Newline)
```
C++ : cout<<'answer'<<endl or cout<<'answer'<<'\n'

python: print('answer')

Java: System.out.println('answer')

JavaScript: console.log('answer')
```