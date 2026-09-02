    // The following program works only if your compiler is C99 compatible.
    #include <stdio.h>
     
    // m and n must be passed before the 2D array
    template <size_t rows, size_t cols>
    void print(int (&arr)[rows][cols])
    {
        int i, j;
        int m = rows;
        int n = cols;
        for (i = 0; i < m; i++)
          for (j = 0; j < n; j++)
            printf("%d ", arr[i][j]);
    }
     
    int main()
    {
        int arr[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int m = 3, n = 3;
        print(arr);
        return 0;
    }