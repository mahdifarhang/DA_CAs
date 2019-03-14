#include <iostream>
#include <vector>


using namespace std;

/*int max_area(vector<int>, int);

int max_vec(vector<int> arr)
{
	int m = 0;
	for (int i = 0; i < arr.size(); i++)
	{
		if (arr[i] > m)
			m = arr[i];
	}
	return m;
}

int main()
{
	vector<int> array;
	int temp;
	while(cin >> temp)
		array.push_back(temp);
	int mheight = max_vec(array);
	temp = 0;
	int max_space = 0;
	for (int i = 0; i <= mheight; i++)
	{
		temp = max_area(array, i);
		if (temp > max_space)
			max_space = temp;
	}
	cout << max_space << endl;
}



int max_area(vector<int> array, int h)
{
	int result = 0;
	int j = 0;
	int m = 0;
	for (int i = 0; i < array.size(); i++)
	{
		j = i;
		m = 0;
		while(true)
		{
			if (array[j] >= h && j < array.size())
			{
				m++;
			}
			else
				break;
			j++;
		}
		if (result < m * h)
			result = m* h;
		i = j;
	}
	return result;
}
*/
int power(int a, int b)
{
	int result = 1;
	for (int i = 0; i < b; i++)
		result *= a;
	return result;
}

vector<int> func(int n)
{
	vector<int> result;
	int temp = 0;	
	int i = n * 5 / 2;
	int j = 1;
	while (temp <= n)
	{
		temp = 0;
		j = 1;
		while (i / power(5, j) > 0)
		{
			temp += (i / power(5, j));
			j++;
		}
		if (temp == n)
			result.push_back(i);
		i++;
	}
	return result;
}

int main()
{
	int n;
	cin >> n;
	vector<int> result = func(n);
	for(int i = 0; i < result.size(); i++)
		cout << result[i] << ' ';
	cout << endl;
}