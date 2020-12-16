package main

import "fmt"

func main() {
	arr := []int{7, 4, 2, 6, 3, 1, 8, 9, 5}

	print(arr)
	fmt.Println("start bubble sort")
	bubblesort(arr)
	fmt.Println("end bubble sort")
	print(arr)
}

func print(arr []int) {
	for _, v := range arr {
		fmt.Printf("%d ", v)
	}
	fmt.Println()
}

func bubblesort(arr []int) {
	for i := 0; i < len(arr)-1; i++ {
		for j := 0; j < len(arr)-1; j++ {
			if arr[j] > arr[j+1] {
				temp := arr[j+1]
				arr[j+1] = arr[j]
				arr[j] = temp

				fmt.Println("bubble sort replacing indices")
				print(arr)

			}
		}
	}
}

/*
void selectionSort() {
   int indexMin,i,j;
	const int SIZE = 10;

	int table[ SIZE ];
	//srand( time( NULL ) );
	for( i = 0; i < SIZE; i++ ) table[ i ] = rand( ) % 10;
	for( i = 0; i < SIZE; i++ ) cout << table[ i ] << " ";
    cout << endl;

    for(i = 0; i < SIZE-1; i++)
    {
      indexMin = i;
      for(j = i+1; j < SIZE;j++)
      {
         if(table[j] < table[indexMin])
         {
            indexMin = j;
         }
      }
      if(indexMin != i)
      {
         int temp = table[indexMin];
         table[indexMin] = table[i];
         table[i] = temp;
      }
    }

   for( i = 0; i < SIZE; i++ ) cout << table[ i ] << " ";
}


void insertSort()
{
    int i, j, value;
    const int SIZE = 10;

	int table[ SIZE ];
	//srand( time( NULL ) );
	for( i = 0; i < SIZE; i++ ) table[ i ] = rand( ) % 10;
	for( i = 0; i < SIZE; i++ ) cout << table[ i ] << " ";
    cout << endl;

    for (i = 1; i < SIZE; ++i)
    {
        value = table[i];
        for (j = i - 1; j >= 0 && table[j] > value; --j)
        {
            table[j + 1] = table[j];
        }
        table[j + 1] = value;
    }
    for( i = 0; i < SIZE; i++ ) cout << table[ i ] << " ";
}
*/
