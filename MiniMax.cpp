// Minimax algorithm (Alpha-Beta Pruning) for a 3D Tic-Tac-Toe
// Author: Pawan Raj
// Repo URl: https://github.com/myselfpawanraj/3D-Tic-Tac-Toe


#include <bits/stdc++.h>
using namespace std;

#define F(i, n) for (int i = 0; i < n; i++)
#define N 3
#define inf 6
#define maxDepth 5

char board[N][N][N];


// function to check if there is space in board 
bool isComplete(){
	F(i, N) F(j, N) F(k, N) {
		if(board[i][j][k] == '0')
			return 0;
	}
	return 1;
}

// function to check if the value won the game
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

// Implementation of algorithm
int minimax(int depth, int turn, int alpha, int beta) {
	
	// Terminating conditions
	
    if (isWin('2'))
        return maxDepth+1-depth;
    if (isWin('1'))
        return depth-maxDepth-1;
    if (isComplete())
        return 0;
    if (depth >= maxDepth)
        return 0;
    
    
    
    int best_val, val;
    if(turn == 1) {
    	best_val = inf;
    	F(i, N) F(j, N) F(k, N){
			if (board[i][j][k] == '0') {
				board[i][j][k] = '1';
				val = minimax(depth+1, 2, alpha, beta);
				board[i][j][k] = '0';				
				
				
				best_val = min(best_val, val);
				beta = min(beta, best_val);
				
				if(beta <= alpha){
					return best_val;
				}
			}
		}
		return best_val;
    }
    else {
    	best_val = -inf;
    	F(i, N) F(j, N) F(k, N){
			if (board[i][j][k] == '0') {
				board[i][j][k] = '2';
				val = minimax(depth+1, 1, alpha, beta);
				board[i][j][k] = '0';
				
				best_val = max(best_val, val);
				alpha = max(alpha, best_val);
				
				if(beta <= alpha){
					return best_val;
				}
			}
		}
		return best_val;
    }
    
}

int32_t main() {
	
	// Taking Inputs
	
	F(i, N) F(j, N) F(k, N){
		cin >> board[i][j][k];
	}
	
	int a[3] = {-1, -1, -1};
	int val = -inf;
	
	F(i, N) F(j, N) F(k, N){
		if (board[i][j][k] == '0') {
			board[i][j][k] = '2';
			int t = minimax(0, 1, -inf, inf);
			if(t > val){
				val = t;
				a[0] = i;
				a[1] = j;
				a[2] = k;
			}
			board[i][j][k] = '0';			
		}
	}
	
	// Printing the cooardinates
	
	cout << a[0] <<"\n";
	cout << a[1] <<"\n";
	cout << a[2] <<"\n";
	
	/*
	To display the board
	
	board[a[0]][a[1]][a[2]] = '2';
	F(i, N) F(j, N) {
		F(k, N){
			cout << board[i][j][k] <<" ";
		}
		cout << '\n';
	}
	*/
    return 0;
}