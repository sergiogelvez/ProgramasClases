#include <stdio.h>
#include <stdlib.h>

int** generate_pascal(int num_rows, int** return_column_sizes) {
    if (num_rows <= 0) return NULL;

    int** triangle = (int**)malloc((size_t)num_rows * sizeof(int*));
    *return_column_sizes = (int*)malloc((size_t)num_rows * sizeof(int));

    for (int i = 0; i < num_rows; ++i) {
        int row_size = i + 1;
        (*return_column_sizes)[i] = row_size;
        triangle[i] = (int*)malloc((size_t)row_size * sizeof(int));

        triangle[i][0] = 1;
        triangle[i][row_size - 1] = 1;

        for (int j = 1; j < i; ++j) {
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
        }
    }
    return triangle;
}

void free_pascal(int** triangle, int num_rows, int* column_sizes) {
    for (int i = 0; i < num_rows; ++i) {
        free(triangle[i]);
    }
    free(triangle);
    free(column_sizes);
}

int main(void) {
    int num_rows = 5;
    int* column_sizes = NULL;
    int** triangle = generate_pascal(num_rows, &column_sizes);

    for (int i = 0; i < num_rows; ++i) {
        for (int j = 0; j < column_sizes[i]; ++j) {
            printf("%d ", triangle[i][j]);
        }
        printf("\n");
    }

    free_pascal(triangle, num_rows, column_sizes);
    return 0;
}
