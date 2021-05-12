#include <bits/stdc++.h>
using namespace std;
#define F(i, n) for (int i = 0; i < n; i++)

const int N = 3;
const int inf = 6;
char board[N][N][N];

bool isComplete(){
	F(i, N) F(j, N) F(k, N) {
		if(board[i][j][k] == '0')
			return 0;
	}
	return 1;
}

bool isWin(char val){
	
    // To check 2D Diagonal lines
    
	F(i, N){
		if (board[0][0][i] == val && board[1][1][i] == val && board[2][2][i] == val)
            return 1;

        if (board[2][0][i] == val && board[1][1][i] == val && board[0][2][i] == val)
            return 1;

        if (board[0][i][0] == val && board[1][i][1] == val && board[2][i][2] == val)
            return 1;

        if (board[2][i][0] == val && board[1][i][1] == val && board[0][i][2] == val)
            return 1;

        if (board[i][0][0] == val && board[i][1][1] == val && board[i][2][2] == val)
            return 1;
            
        if (board[i][2][0] == val && board[i][1][1] == val && board[i][0][2] == val)
            return 1;
	}
	
    // To check diagonal lines of the cube

    if (board[0][0][0] == val && board[1][1][1] == val && board[2][2][2] == val)
        return 1;

    if (board[0][0][2] == val && board[1][1][1] == val && board[2][2][0] == val)
        return 1;

    if (board[2][0][0] == val && board[1][1][1] == val && board[0][2][2] == val)
        return 1;

    if (board[2][0][2] == val && board[1][1][1] == val && board[0][2][0] == val)
        return 1;
        
    // To check straight lines

    bool temp = 1;
    F(i, N) F(j, N) {
        temp = 1;
    	F(k, N) if (board[i][j][k] != val) temp = 0;
    	
        if(temp) return 1;

        temp = 1;
    	F(k, N) if (board[i][k][j] != val) temp = 0;

        if(temp) return 1;
        
        temp = 1;
    	F(k, N) if (board[k][i][j] != val) temp = 0;
            
        if(temp) return 1;
    }
            
    return 0;
}

int minimax(int depth, int turn) {
	
    if (isWin('2'))
        return 6-depth;
    if (isWin('1'))
        return depth-6;
    if (isComplete())
        return 0;
    if (depth >= 4)
        return 0;
    
    if(turn == 1) {
    	int val = inf;
    	F(i, N) F(j, N) F(k, N){
			if (board[i][j][k] == '0') {
				board[i][j][k] = '1';
				int t = minimax(depth+1, 2);
				val = min(val, t);
				board[i][j][k] = '0';			
			}
		}
		return val;
    }
    else {
    	int val = -inf;
    	F(i, N) F(j, N) F(k, N){
			if (board[i][j][k] == '0') {
				board[i][j][k] = '2';
				int t = minimax(depth+1, 1);
				val = max(val, t);
				board[i][j][k] = '0';
			}
		}
		return val;
    }
    
}

int32_t main() {
	
	F(i, N) F(j, N) F(k, N){
		cin >> board[i][j][k];
	}
	int a[3] = {-1, -1, -1};
	int val = -10;
	F(i, N) F(j, N) F(k, N){
		if (board[i][j][k] == '0') {
			board[i][j][k] = '2';
			int t = minimax(0, 1);
			if(t > val){
				val = t;
				a[0] = i;
				a[1] = j;
				a[2] = k;
			}
			// cout << i <<" "<< j <<" "<< k <<" = " << t << '\n';
			board[i][j][k] = '0';			
		}
	}
	// cout << a[0] <<"\n";
	// cout << a[1] <<"\n";
	// cout << a[2] <<"\n";
	// cout << "\n\n";
	
	board[a[0]][a[1]][a[2]] = '2';
	F(i, N) F(j, N) {
		F(k, N){
			cout << board[i][j][k] <<" ";
		}
		cout << '\n';
	}
    return 0;
}