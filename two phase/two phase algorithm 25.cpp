#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <ctime>
#include <time.h>
#include <unordered_map>
#include <list>

using namespace std;

int main() {
	time_t rawtime;
	struct tm* info;
	char buffer[64];
	time(&rawtime);
	info = localtime(&rawtime);
	strftime(buffer, 64, "%Y-%m-%d %H:%M:%S", info);
	cout << buffer << endl;


	clock_t t1, t2;
	t1 = clock();
	for (int i = 0; i < 300000000; i++) {
		continue;
	}
	t2 = clock();
	cout << (double)(t2 - t1) / CLOCKS_PER_SEC << endl;

	clock_t tinit = clock();

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
					n1 += 24;
				}
			}
		}
	}
	cout << "ep4dict " << ep4dict.size() << endl;

	/*
	for (const auto& key_value : ep4dict) {
		int key = key_value.first;
		int value = key_value.second;
		cout << key << " - " << value << endl;
	}
	*/

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
														eodict[(((((((((((edgedirection[0][i]) * 6 + edgedirection[1][j]) * 6 + edgedirection[2][k]) * 6 + edgedirection[3][l]) * 6 + edgedirection[4][m]) * 6 + edgedirection[5][n]) * 6 + edgedirection[6][o]) * 6 + edgedirection[7][p]) * 6 + edgedirection[8][q]) * 6 + edgedirection[9][r]) * 6 + edgedirection[10][s]) * 6 + edgedirection[11][t]] = n1;
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


	unordered_map<unsigned short, unsigned short> cr[6][3], cor[6][3], ep4r[6][3], eor[6][3];
	for (short f = 0; f < 6; f++) {
		short c1, c2, c3, c4, e1, e2, e3, e4;
		c1 = facecorner[f][0];
		c2 = facecorner[f][1];
		c3 = facecorner[f][2];
		c4 = facecorner[f][3];
		e1 = faceedge[f][0];
		e2 = faceedge[f][1];
		e3 = faceedge[f][2];
		e4 = faceedge[f][3];
		int* fe = faceedge[f];

		for (short t = 0; t < 3; t++) {
			cout << f << " " << t << endl;
			int nc1 = facetimecorner[f][t][0];
			int nc2 = facetimecorner[f][t][1];
			int nc3 = facetimecorner[f][t][2];
			int nc4 = facetimecorner[f][t][3];
			int ne1 = facetimeedge[f][t][0];
			int ne2 = facetimeedge[f][t][1];
			int ne3 = facetimeedge[f][t][2];
			int ne4 = facetimeedge[f][t][3];
			int* fte = facetimeedge[f][t];
			int* ftd = facetimedirection[f][t];

			unordered_map<unsigned short, unsigned short> cmap;
			for (const auto& key_value : cdict) {
				int key = key_value.first;
				short c[8],dc[8];
				for (int i = 7; i >= 0; i--) {
					int re = key % 8;
					c[i] = re;
					dc[i] = re;
					key /= 8;
				}
				c[c1] = dc[nc1];
				c[c2] = dc[nc2];
				c[c3] = dc[nc3];
				c[c4] = dc[nc4];

				cmap[cdict.at(((((((c[0] * 8 + c[1]) * 8 + c[2]) * 8 + c[3]) * 8 + c[4]) * 8 + c[5]) * 8 + c[6]) * 8 + c[7])] = key_value.second;
			}
			cr[f][t] = cmap;

			unordered_map<unsigned short, unsigned short> comap;
			for (const auto& key_value : codict) {
				int key = key_value.first;
				short co[8], dco[8];
				for (int i = 7; i >= 0; i--) {
					int re = key % 6;
					co[i] = re;
					dco[i] = re;
					key /= 6;
				}
				co[c1] = ftd[dco[nc1]];
				co[c2] = ftd[dco[nc2]];
				co[c3] = ftd[dco[nc3]];
				co[c4] = ftd[dco[nc4]];

				comap[codict.at(((((((co[0] * 6 + co[1]) * 6 + co[2]) * 6 + co[3]) * 6 + co[4]) * 6 + co[5]) * 6 + co[6]) * 6 + co[7])] = key_value.second;
			}
			cor[f][t] = comap;

			unordered_map<unsigned short, unsigned short> eomap;
			for (const auto& key_value : eodict) {
				int key = key_value.first;
				short eo[12], deo[12];
				for (int i = 11; i >= 0; i--) {
					int re = key % 6;
					eo[i] = re;
					deo[i] = re;
					key /= 6;
				}
				eo[e1] = ftd[deo[ne1]];
				eo[e2] = ftd[deo[ne2]];
				eo[e3] = ftd[deo[ne3]];
				eo[e4] = ftd[deo[ne4]];

				eomap[eodict.at(((((((((((eo[0] * 6 + eo[1]) * 6 + eo[2]) * 6 + eo[3]) * 6 + eo[4]) * 6 + eo[5]) * 6 + eo[6]) * 6 + eo[7]) * 6 + eo[8]) * 6 + eo[9]) * 6 + eo[10]) * 6 + eo[11])] = key_value.second;
			}
			eor[f][t] = eomap;

			unordered_map<unsigned short, unsigned short> ep4map;
			for (const auto& key_value : ep4dict) {
				int key = key_value.first;
				short ep4[4];
				for (int i = 3; i >= 0; i--) {
					int re = key % 12;
					for (int j = 0; j < 4; j++) {
						if (re == fte[j]) {
							re = fe[j];
							break;
						}
					}
					ep4[i] = re;
					key /= 12;
				}
				//cout << key_value.second << endl;
				ep4map[ep4dict.at(((ep4[0]*12+ep4[1])*12+ep4[2])*12+ep4[3])] = key_value.second;
			}
			ep4r[f][t] = ep4map;
		}

	}
	tinit = clock() - tinit;
	cout <<"initial time " << (double)tinit / CLOCKS_PER_SEC << "s" << endl;

	time(&rawtime);
	info = localtime(&rawtime);
	strftime(buffer, 64, "%Y-%m-%d %H:%M:%S", info);
	cout << buffer << endl;


	unordered_map<unsigned short, unsigned short> cr0[3] = { cr[0][0],cr[1][0],cr[2][0] };
	unordered_map<unsigned short, unsigned short> cor0[3] = { cor[0][0],cor[1][0],cor[2][0] };
	unordered_map<unsigned short, unsigned short> eor0[3] = { eor[0][0],eor[1][0],eor[2][0] };
	unordered_map<unsigned short, unsigned short> ep4r0[3] = { ep4r[0][0],ep4r[1][0],ep4r[2][0] };
	unordered_map<unsigned short, unsigned short> cr1[3] = { cr[0][1],cr[1][1],cr[2][1] };
	unordered_map<unsigned short, unsigned short> ep4r1[3] = { ep4r[0][1],ep4r[1][1],ep4r[2][1] };
	int ccn=0, ccon=0, cen1=0, cen2=10200, cen3=11856, ceon=0;

	int dict1step = 1;
	int dict2step = 1;

	//dict1 unsigned int->unsigned long long int
	//dict2 unsigned long long int->unsigned long long int
	unordered_map<unsigned int, unsigned long long int> dict1;
	cout << "dict1" << endl;
	list<int> predictstate;


}

