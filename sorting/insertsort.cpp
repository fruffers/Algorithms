// for and while loop
// put current value 

void sort(int a[], int n) {
    int i,j,temp;
    for (i = 1; i < n; i++) {
        // loop all possible compare values
        temp = a[i];
        j = a[i-1];
        while (j>=0 && temp < j) {
            // loop compare all sorted values before the end compare val i
            // break out when j reaching 0
            a[j+1] = a[j];
            j = j-1;
        }
        a[j+1]=temp;
    }
}