#if 0
#include <cstdio>
#include <string.h>
#include <algorithm>
using namespace std;

int dp[150][50];
char s[150];

int getnum(int i, int j)
{
	if (j > i&&s[i - 1] == '0' || strlen(s) < j) return -1;
	int ret = 0;
	for (int k = i - 1; k < j; ++k) ret = ret * 10 + s[k] - '0';
	return (ret <= 100 ? ret : -1);
}

int main()
{
	int n;
	while (scanf("%d %s", &n, s) != EOF)
	{
		memset(dp, -1, sizeof(dp));
		dp[0][0] = dp[1][0] = dp[2][0] = 0;
		int len = strlen(s);
		for (int i = 1; i <= len; ++i)
			for (int j = (i - 1) / 3 + ((i - 1) % 3 ? 1 : 0) + 1; j <= min(n, i); ++j)
			{
				if (dp[i - 1][j - 1] == -1) continue;
				for (int k = 0; k < 3; ++k)
					if (getnum(i, i + k) != -1) dp[i + k][j] = max(dp[i + k][j], dp[i - 1][j - 1] + getnum(i, i + k));
			}
		printf("%.2f\n", 1.0*dp[len][n] / n);
	}
	return 0;
}
#endif