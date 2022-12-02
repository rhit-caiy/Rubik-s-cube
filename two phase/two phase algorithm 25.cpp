#include <stdio.h>
#include <iostream>
#include <time.h>
#include <unordered_map>

using namespace std;

int main() {
	/*
	clock_t t1, t2;
	double dt;
	t1 = clock();
	for (int i = 0; i < 100000000; i++) {
		continue;
	}
	t2 = clock();
	dt = (double)(t2 - t1) / CLOCKS_PER_SEC;
	printf("%d    %f\n", 0, dt);

	unordered_map<unsigned long long int, unsigned long long int> umap1, umap2;
	unsigned long long int a, b;
	a = 1;
	b = 2;

	t1 = clock();
	for (int i = 0; i < 1000000; i++) {
		umap1[i] = i;
	}
	t2 = clock();
	dt = (double)(t2 - t1) / CLOCKS_PER_SEC;
	printf("%d    %f\n", 0, dt);

	t1 = clock();
	for (int i = 0; i < 1000000; i++) {
		umap2.insert(make_pair(i, i));
	}
    
	t2 = clock();
	dt = (double)(t2 - t1) / CLOCKS_PER_SEC;
	printf("%d    %f\n", 0, dt);
	*/ ;
    int cc[8] = { 0,1,2,3,4,5,6,7 };
    int cco[8] = { 0,0,0,0,3,3,3,3 };
    int ce[12] = { 0,1,2,3,4,5,6,7,8,9,10,11 };
    int ceo[12] = { 0,0,0,0,1,1,4,4,3,3,3,3 };

    int facetimecorner[6][3][4] = { {{2,3,1,0},{3,1,0,2},{1,0,2,3}},{{6,4,2,0},{4,2,0,6},{2,0,6,4}},{{4,5,3,2},{5,3,2,4},{3,2,4,5}},{{6,7,5,4},{7,5,4,6},{5,4,6,7}},{{5,7,1,3},{7,1,3,5},{1,3,5,7}},{{7,6,0,1},{6,0,1,7},{0,1,7,6}} };  
    int facetimeedge[6][3][4] = { {{1,2,3,0},{2,3,0,1},{3,0,1,2}},{{4,9,5,1},{9,5,1,4},{5,1,4,9}},{{5,10,6,2},{10,6,2,5},{6,2,5,10}},{{9,8,11,10},{8,11,10,9},{11,10,9,8}},{{6,11,7,3},{11,7,3,6},{7,3,6,11}},{{7,8,4,0},{8,4,0,7},{4,0,7,8}} };
    int facecorner[6][4] = { {0,2,3,1},{0,6,4,2},{2,4,5,3},{4,6,7,5},{3,5,7,1},{1,7,6,0} };
    int faceedge[6][4] = { {0,1,2,3},{1,4,9,5},{2,5,10,6},{10,9,8,11},{3,6,11,7},{0,7,8,4} };
    int facetimedirection[6][3][6] = { {{0,5,1,3,2,4},{0,4,5,3,1,2},{0,2,4,3,5,1}},{{2,1,3,5,4,0},{3,1,5,0,4,2},{5,1,0,2,4,3}},{{4,0,2,1,3,5},{3,4,2,0,1,5},{1,3,2,4,0,5}},{{0,2,4,3,5,1},{0,4,5,3,1,2},{0,5,1,3,2,4}},{{5,1,0,2,4,3},{3,1,5,0,4,2},{2,1,3,5,4,0}},{{1,3,2,4,0,5},{3,4,2,0,1,5},{4,0,2,1,3,5}} };
    int cornerdirection[8][3] = { {0,5,1},{0,4,5},{0,1,2},{0,2,4},{3,2,1},{3,4,2},{3,1,5},{3,5,4} };
    int edgedirection[12][2] = { {0,5},{0,1},{0,2},{0,4},{1,5},{1,2},{4,2},{4,5},{3,5},{3,1},{3,2},{3,4} };

    unordered_map<int, unsigned short> cdict, codict, ep4dict, eodict;

    cout << sizeof(short) << " " << sizeof(int) << " " << sizeof(long int) << " " << sizeof(long long int) << " " << sizeof(unsigned long long int)<<endl;

    unsigned short n = 0;
	unsigned short n1 = 0;

    //cdict
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			if (i == j) {
				continue;
			}
			for (int k = 0; k < 8; k++) {
				if (i == k || j == k) {
					continue;
				}
				for (int l = 0; l < 8; l++) {
					if (i == l || j == l || k == l) {
						continue;
					}
					for (int m = 0; m < 8; m++) {
						if (i == m || j == m || k == m || l == m) {
							continue;
						}
						for (int n = 0; n < 8; n++) {
							if (i == n || j == n || k == n || l == n || m == n) {
								continue;
							}
							for (int o = 0; o < 8; o++) {
								if (i == o || j == o || k == o || l == o || m == o || n == o) {
									continue;
								}
								for (int p = 0; p < 8; p++) {
									if (i == p || j == p || k == p || l == p || m == p || n == p || o == p) {
										continue;
									}
									cdict[((((((i * 8 + j) * 8 + k) * 8 + l) * 8 + m) * 8 + n) * 8 + o) * 8 + p]=n1;
									n1++;
								}
							}
						}
					}
				}
			}
		}
	}
	cout<<"cdict " << cdict.size() << endl;
	/*
	cout << cdict.at(key) << endl;
	for (const auto& key_value : cdict) {
		int key = key_value.first;
		int value = key_value.second;
		//cout << key << " - " << value << endl;
	}
	*/
	//codict
	n1 = 0;
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			for (int k = 0; k < 3; k++) {
				for (int l = 0; l < 3; l++) {
					for (int m = 0; m < 3; m++) {
						for (int n = 0; n < 3; n++) {
							for (int o = 0; o < 3; o++) {
								for (int p = 0; p < 3; p++) {
									if ((i + j + k + l + m + n + o + p) % 3 == 0) {
										codict[((((((cornerdirection[0][i] * 6 + cornerdirection[1][j]) * 6 + cornerdirection[2][k]) * 6 + cornerdirection[3][l]) * 6 + cornerdirection[4][m]) * 6 + cornerdirection[5][n]) * 6 + cornerdirection[6][o]) * 6 + cornerdirection[7][p]] = n1;
										n1++;
									}
								}
							}
						}
					}
				}
			}
		}
	}
	cout << "codict " << codict.size() << endl;
	/*
	for (const auto& key_value : codict) {
		int key = key_value.first;
		int value = key_value.second;
		//cout << key << " - " << value << endl;
	}
	*/

	//ep4dict
	n1 = 0;
	for (int i = 0; i < 12; i++) {
		for (int j = i + 1; j < 12; j++) {
			for (int k = j + 1; k < 12; k++) {
				for (int l = k + 1; l < 12; l++) {
					ep4dict[((i * 12 + j) * 12 + k) * 12 + l] = n1 + 0;
					ep4dict[((i * 12 + j) * 12 + l) * 12 + k] = n1 + 1;
					ep4dict[((i * 12 + k) * 12 + j) * 12 + l] = n1 + 2;
					ep4dict[((i * 12 + k) * 12 + l) * 12 + j] = n1 + 3;
					ep4dict[((i * 12 + l) * 12 + j) * 12 + k] = n1 + 4;
					ep4dict[((i * 12 + l) * 12 + k) * 12 + j] = n1 + 5;
					ep4dict[((j * 12 + i) * 12 + k) * 12 + l] = n1 + 6;
					ep4dict[((j * 12 + i) * 12 + l) * 12 + k] = n1 + 7;
					ep4dict[((j * 12 + k) * 12 + i) * 12 + l] = n1 + 8;
					ep4dict[((j * 12 + k) * 12 + l) * 12 + i] = n1 + 9;
					ep4dict[((j * 12 + l) * 12 + i) * 12 + k] = n1 + 10;
					ep4dict[((j * 12 + l) * 12 + k) * 12 + i] = n1 + 11;
					ep4dict[((k * 12 + i) * 12 + j) * 12 + l] = n1 + 12;
					ep4dict[((k * 12 + i) * 12 + l) * 12 + j] = n1 + 13;
					ep4dict[((k * 12 + j) * 12 + i) * 12 + l] = n1 + 14;
					ep4dict[((k * 12 + j) * 12 + l) * 12 + i] = n1 + 15;
					ep4dict[((k * 12 + l) * 12 + i) * 12 + j] = n1 + 16;
					ep4dict[((k * 12 + l) * 12 + j) * 12 + i] = n1 + 17;
					ep4dict[((l * 12 + i) * 12 + j) * 12 + k] = n1 + 18;
					ep4dict[((l * 12 + i) * 12 + k) * 12 + j] = n1 + 19;
					ep4dict[((l * 12 + j) * 12 + i) * 12 + k] = n1 + 20;
					ep4dict[((l * 12 + j) * 12 + k) * 12 + i] = n1 + 21;
					ep4dict[((l * 12 + k) * 12 + i) * 12 + j] = n1 + 22;
					ep4dict[((l * 12 + k) * 12 + j) * 12 + i] = n1 + 23;
				}
			}
		}
	}
	cout << "ep4dict " << ep4dict.size() << endl;

	//eodict
	n1 = 0;
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			for (int k = 0; k < 2; k++) {
				for (int l = 0; l < 2; l++) {
					for (int m = 0; m < 2; m++) {
						for (int n = 0; n < 2; n++) {
							for (int o = 0; o < 2; o++) {
								for (int p = 0; p < 2; p++) {
									for (int q = 0; q < 2; q++) {
										for (int r = 0; r < 2; r++) {
											for (int s = 0; s < 2; s++) {
												for (int t = 0; t < 2; t++) {
													if ((i + j + k + l + m + n + o + p + q + r + s + t) % 2 == 0) {
														eodict[((((((((((i * 12 + j) * 12 + k) * 12 + l) * 12 + m) * 12 + n) * 12 + o) * 12 + p) * 12 + q) * 12 + r) * 12 + s) * 12 + t]=n1;
														n1++;
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
	cout << "eodict " << eodict.size() << endl;





}