#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <ctime>
#include <cmath>
#include <cstdlib>
#include <unordered_map>
#include <list>
#include <stack>
using namespace std;

const double log18 = log(18);

struct dict1cube {
	unsigned short co;
	unsigned short eo;
	unsigned short e2;
	unsigned long long oldstep;
	short f1;
};

struct dict2cube {
	unsigned short c;
	unsigned short e1;
	unsigned short e2;
	unsigned short e3;
	unsigned long long oldstep;
	short f1;
};

struct cubepack {
	unsigned short c;
	unsigned short co;
	unsigned short eo;
	unsigned short e1;
	unsigned short e2;
	unsigned short e3;
};

struct solvecube {
	unsigned short c;
	unsigned short co;
	unsigned short eo;
	unsigned short e1;
	unsigned short e2;
	unsigned short e3;
	unsigned long long oldstep;
	short step;
	short f1;
};

struct solvereturn {
	short htm;
	short qtm;
	short stm;
	unsigned long long minmovep1;
	unsigned long long minmovep2;
};

unordered_map<unsigned int, unsigned long long int> getdict1(int dict1step, unordered_map<unsigned short, unsigned short>* cor0, unordered_map<unsigned short, unsigned short>* eor0, unordered_map<unsigned short, unsigned short>* ep4r0) {
	unordered_map<unsigned int, unsigned long long int> dict1;
	dict1.reserve(14000000);
	cout << "dict1" << endl;
	cout << setw(8) << "step" << setw(16) << "cubes left" << setw(16) << "dict length" << setw(16) << "time/s" << endl;
	unsigned short ccon = 0, cen2 = 10200, ceon = 0;
	dict1cube cd1c = { ccon,ceon,cen2,1,-1 };
	list<dict1cube> predictstate = { cd1c };
	list<dict1cube> newpredictstate;
	dict1[cen2 / 24 + 495 * (ceon + (unsigned int)2048 * ccon)] = 1;
	clock_t t0 = clock();
	
	unsigned short oco, oeo, oe2, nco, neo, ne2;
	unsigned long long oldstep, newstep;
	short f, t, f1;
	unsigned int key;
	list<dict1cube>::iterator it;
	clock_t t1;
	for (int step = 1; step < dict1step + 1; step++) {
		t1 = clock();
		for (it = predictstate.begin(); it != predictstate.end(); it++) {
			oco = it->co, oeo = it->eo, oe2 = it->e2, oldstep = it->oldstep, f1 = it->f1;
			oldstep *= 18;
			for (f = 0; f < 6; f++) {
				if (f != f1 && f1 - f != 3) {
					newstep = oldstep + 3 * f + 2;
					nco = oco, neo = oeo, ne2 = oe2;
					for (t = 0; t < 3; t++) {
						nco = cor0[f].at(nco);
						neo = eor0[f].at(neo);
						ne2 = ep4r0[f].at(ne2);
						key = ne2 / 24 + 495 * (neo + (unsigned int)2048 * nco);
						if (!dict1.count(key)) {
							dict1[key] = newstep;
							if (step != dict1step) {
								newpredictstate.push_back({ nco,neo,ne2,newstep,f });
							}
						}
						newstep--;
					}
				}
			}
		}
		cout << setw(8) << step << setw(16) << newpredictstate.size() << setw(16) << dict1.size() << setw(16) << (double)(clock() - t1) / CLOCKS_PER_SEC << "s" << endl;
		predictstate = newpredictstate;
		newpredictstate = {};
	}
	dict1.erase(cen2 / 24 + 495 * (ceon + (unsigned int)2048 * ccon));
	cout << setw(8) << "dict 1" << setw(16) <<"" << setw(16) << dict1.size() << setw(16) << (double)(clock() - t0) / CLOCKS_PER_SEC << "s" << endl;
	return dict1;
}

unordered_map<unsigned long long int, unsigned long long int> getdict2(int dict2step,unsigned long long* eighteen, unordered_map<unsigned short, unsigned short>* cr0, unordered_map<unsigned short, unsigned short>* ep4r0, unordered_map<unsigned short, unsigned short>* cr1, unordered_map<unsigned short, unsigned short>* ep4r1) {
	unordered_map<unsigned long long int, unsigned long long int> dict2;
	dict2.reserve(6000000);
	cout << "dict2" << endl;
	cout << setw(8) << "step" << setw(16) << "cubes left" << setw(16) << "dict length" << setw(16) << "time/s" << endl;
	unsigned short ccn = 0, cen1 = 0, cen2 = 10200, cen3 = 11856;
	dict2cube cd2c = { ccn,cen1,cen2,cen3,0,-1 };
	list<dict2cube> predictstate = { cd2c };
	list<dict2cube> newpredictstate;
	dict2[cen3 + 11880 * (cen2 + 11880 * (cen1 + (unsigned long long)11880 * ccn))] = 1;
	clock_t t0 = clock();

	unsigned short oc, oe1, oe2, oe3, nc, ne1, ne2, ne3;
	unsigned long long oldstep, newstep;
	short t, f1;
	unsigned long long key;
	list<dict2cube>::iterator it;
	clock_t t1;
	for (int step = 1; step < dict2step + 1; step++) {
		t1 = clock();
		unsigned long long eighteen0 = eighteen[step - 1], eighteen1 = eighteen[step];
		for (it = predictstate.begin(); it != predictstate.end(); it++) {
			oc = it->c, oe1 = it->e1, oe2 = it->e2, oe3 = it->e3, oldstep = it->oldstep, f1 = it->f1;
			for (short f : {0, 3}) {
				if (f != f1 && (f1 != 3 || f != 3)) {
					nc = oc;
					ne1 = oe1;
					ne2 = oe2;
					ne3 = oe3;
					for (t = 2; t > -1; t--) {
						nc = cr0[f].at(nc);
						ne1 = ep4r0[f].at(ne1);
						ne2 = ep4r0[f].at(ne2);
						ne3 = ep4r0[f].at(ne3);
						key = ne3 + 11880 * (ne2 + 11880 * (ne1 + (unsigned long long)11880 * nc));
						if (!dict2.count(key)) {
							newstep = oldstep + (3 * f + t) * eighteen0;
							dict2[key] = newstep + eighteen1;
							if (step != dict2step) {
								newpredictstate.push_back({ nc,ne1,ne2,ne3,newstep,f });
							}
						}
					}
				}
			}
			for (short f : {1, 2, 4, 5}) {
				if (f != f1 && f1 - f != 3) {
					nc = cr1[f].at(oc);
					ne1 = ep4r1[f].at(oe1);
					ne2 = ep4r1[f].at(oe2);
					ne3 = ep4r1[f].at(oe3);
					key = ne3 + 11880 * (ne2 + 11880 * (ne1 + (unsigned long long)11880 * nc));
					if (!dict2.count(key)) {
						newstep = oldstep + (3 * f + 1) * eighteen0;
						dict2[key] = newstep + eighteen1;
						if (step != dict2step) {
							newpredictstate.push_back({ nc,ne1,ne2,ne3,newstep,f });
						}
					}
				}
			}
		}
		cout << setw(8) << step << setw(16) << newpredictstate.size() << setw(16) << dict2.size() << setw(16) << (double)(clock() - t1) / CLOCKS_PER_SEC << "s" << endl;
		predictstate = newpredictstate;
		newpredictstate = {};
	}
	cout << setw(8) << "dict 2" << setw(16) << "" << setw(16) << dict2.size() << setw(16) << (double)(clock() - t0) / CLOCKS_PER_SEC << "s" << endl;
	return dict2;
}


void randomcube(short randomstrings[2][5000],int a) {
	srand((unsigned)time(NULL));
	short f, t;
	for (int i = 0; i < a; i++) {
		f = rand() % 6;
		t = rand() % 3;
		randomstrings[0][2 * i] = f;
		randomstrings[0][2 * i + 1] = t;
		randomstrings[1][2 * a - 2 * i - 2] = f;
		randomstrings[1][2 * a - 2 * i - 1] = 2 - t;
	}
}

void getcubewithbase(cubepack unsolvedcubes[6], short randomstrings[2][5000], int a, unordered_map<unsigned short, unsigned short> cr[6][3], unordered_map<unsigned short, unsigned short> cor[6][3], unordered_map<unsigned short, unsigned short> eor[6][3], unordered_map<unsigned short, unsigned short> ep4r[6][3]) {
	int directions[3][6] = { {0, 1, 2, 3, 4, 5},{1, 2, 0, 4, 5, 3},{2, 0, 1, 5, 3, 4 } };
	for (int i = 0; i < 6; i++) {
		int* direction = directions[i % 3];
		unsigned short c = 0, co = 0, eo = 0, e1 = 0, e2 = 10200, e3 = 11856;
		for (int j = 0; j < a; j++) {
			short f = direction[randomstrings[i / 3][2 * j]];
			short t = randomstrings[i / 3][2 * j + 1];
			c = cr[f][t].at(c);
			co = cor[f][t].at(co);
			eo = eor[f][t].at(eo);
			e1 = ep4r[f][t].at(e1);
			e2 = ep4r[f][t].at(e2);
			e3 = ep4r[f][t].at(e3);
		}
		unsolvedcubes[i] = { c,co,eo,e1,e2,e3 };
	}
}

solvereturn solve(cubepack cubepack, short threadid, short htm, short qtm, short stm, short phase1step, unordered_map<unsigned short, unsigned short> cr0[6], unordered_map<unsigned short, unsigned short> cor0[6], unordered_map<unsigned short, unsigned short> eor0[6], unordered_map<unsigned short, unsigned short> ep4r0[6], unordered_map<unsigned short, unsigned short> cr1[6], unordered_map<unsigned short, unsigned short> ep4r1[6], unordered_map<unsigned short, unsigned short> cr[6][3], unordered_map<unsigned short, unsigned short> ep4r[6][3], unordered_map<unsigned short, unsigned short> eor[6][3], unordered_map<unsigned int, unsigned long long int>* dict1, unordered_map<unsigned long long int, unsigned long long int>* dict2) {
	clock_t tstart = clock();
	unsigned short c = cubepack.c, co = cubepack.co, eo = cubepack.eo, e1 = cubepack.e1, e2 = cubepack.e2, e3 = cubepack.e3;
	cout << "thread " << threadid << endl << "c = " << c << "  co = " << co << "  eo = " << eo << "  e1 = " << e1 << "  e2 = " << e2 << "  e3 = " << e3 << endl;
	solvecube initialcube = { c,co,eo,e1,e2,e3,1,0,-1 };
	stack<solvecube> cubes;
	cubes.push(initialcube);
	solvecube tempcube,pushcube;
	unsigned short oc, oco, oeo, oe1, oe2, oe3, nc, nco, neo, ne1, ne2, ne3, nc1, ne11, ne21, ne31;
	unsigned long long oldstep, m1_1, m1_2, m1, m2;
	unsigned int key1;
	unsigned long long int key2;
	short step, f1, f0, t0, l, qtmvalue, stmvalue;
	unsigned long long minmovep1=1, minmovep2=1;
	unordered_map<unsigned short, unsigned short> *crf0, *corf0, *eorf0, *ep4rf0, *ep4rf0t0, *ep4rf01;
	while (!cubes.empty()) {
		tempcube=cubes.top();
		cubes.pop();
		oc = tempcube.c, oco = tempcube.co, oeo = tempcube.eo, oe1 = tempcube.e1, oe2 = tempcube.e2, oe3 = tempcube.e3, oldstep = tempcube.oldstep * 18, step = tempcube.step + 1, f1 = tempcube.f1;
		for (short f = 0; f < 6; f++) {
			if (f != f1 && f1 - f != 3) {
				m1_1 = oldstep + 3 * f;
				crf0 = &cr0[f];
				corf0 = &cor0[f];
				eorf0 = &eor0[f];
				ep4rf0 = &ep4r0[f];
				nc = oc, nco = oco, neo = oeo, ne1 = oe1, ne2 = oe2, ne3 = oe3;
				for (short t = 0; t < 3; t++) {
					m1 = m1_1 + t;
					nc = crf0->at(nc);
					nco = corf0->at(nco);
					neo = eorf0->at(neo);
					ne1 = ep4rf0->at(ne1);
					ne2 = ep4rf0->at(ne2);
					ne3 = ep4rf0->at(ne3);

					if (step != phase1step) {
						pushcube = { nc,nco,neo,ne1,ne2,ne3,m1,step,f };
						cubes.push(pushcube);
					}
					key1 = ne2 / 24 + 495 * (neo + (unsigned int)2048 * nco);
					if (dict1->count(key1)) {
						m1_2=dict1->at(key1);
						f0 = f, nc1 = nc, ne11 = ne1, ne21 = ne2, ne31 = ne3;
						while (m1_2 > 18) {
							f0 = m1_2 / 3 % 6;
							t0 = m1_2 % 3;
							m1 = 18 * m1 + 3 * f0 + t0;
							m1_2 /= 18;
							nc1 = cr[f0][t0].at(nc1);
							ep4rf0t0 = &ep4r[f0][t0];
							ne11 = ep4rf0t0->at(ne11);
							ne21 = ep4rf0t0->at(ne21);
							ne31 = ep4rf0t0->at(ne31);
						}
						key2 = ne31 + 11880 * (ne21 + 11880 * (ne11 + (unsigned long long)11880 * nc1));
						if (dict2->count(key2)) {
							m2=dict2->at(key2);
							l = (short)(log(m1) / log18) + (short)(log(m2) / log18);
							if (l <= htm) {
								htm = l;
								minmovep1 = m1;
								minmovep2 = m2;
								qtmvalue = htm;
								stmvalue = htm;
								cout << threadid << "   " << htm <<" = "<<step << " + " << (short)(log(m1) / log18) - (short)(log(m1_1) / log18) << " + " << (short)(log(m2) / log18) << "    type 1  phase1 " << m1 << "  phase2 " << m2 << "    ";
								unsigned long long printm1 = m1;
								unsigned long long printm2 = m2;
								while (printm1 >= 18) {
									cout << printm1 / 3 % 6 << printm1 % 3;
									if (printm1 % 3 == 1) {
										qtmvalue++;
									}
									printm1 /= 18;
								}
								while (printm2 >= 18) {
									cout << printm2 / 3 % 6 << printm2 % 3;
									if (printm2 % 3 == 1) {
										qtmvalue++;
									}
									printm2 /= 18;
								}
								cout << endl;
								if (qtmvalue < qtm) {
									qtm = qtmvalue;
								}
								if (stmvalue < stm) {
									stm = stmvalue;
								}

								ep4rf01 = &ep4r1[f0];
								nc1 = cr1[f0].at(nc1);
								ne1 = ep4rf01->at(ne1);
								ne2 = ep4rf01->at(ne2);
								ne3 = ep4rf01->at(ne3);
								key2 = ne31 + 11880 * (ne21 + 11880 * (ne11 + (unsigned long long)11880 * nc1));
								if (dict2->count(key2)) {
									m1 += 2;
									m2 = dict2->at(key2);
									l = (short)(log(m1) / log18) + (short)(log(m2) / log18);
									if (l <= htm) {
										htm = l;
										minmovep1 = m1;
										minmovep2 = m2;
										qtmvalue = htm;
										stmvalue = htm;
										cout << threadid << "   " << htm << " = " << step << " + " << (short)(log(m1) / log18) - (short)(log(m1_1) / log18) << " + " << (short)(log(m2) / log18) << "    type 2  phase1 " << m1 << "  phase2 " << m2 << "    ";
										unsigned long long printm1 = m1;
										unsigned long long printm2 = m2;
										while (printm1 >= 18) {
											cout << printm1 / 3 % 6 << printm1 % 3;
											if (printm1 % 3 == 1) {
												qtmvalue++;
											}
											printm1 /= 18;
										}
										while (printm2 >= 18) {
											cout << printm2 / 3 % 6 << printm2 % 3;
											if (printm2 % 3 == 1) {
												qtmvalue++;
											}
											printm2 /= 18;
										}
										cout << endl;
										if (qtmvalue < qtm) {
											qtm = qtmvalue;
										}
										if (stmvalue < stm) {
											stm = stmvalue;
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

	solvereturn sr = { htm,qtm,stm,minmovep1,minmovep2 };
	cout << "finish thread " << threadid <<"    htm "<<htm << "  qtm " << qtm << "  stm " << stm <<"    time " << (double)(clock()-tstart) / CLOCKS_PER_SEC << "s" << endl << endl;
	return sr;
}

int main(int argc,char** argv) {
	time_t rawtime;
	struct tm* info;
	char buffer[64];
	time(&rawtime);
	info = localtime(&rawtime);
	strftime(buffer, 64, "%Y-%m-%d %H:%M:%S", info);
	cout << buffer << endl;

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
	unsigned short n = 0, n1 = 0;

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
									cdict[((((((i * 8 + j) * 8 + k) * 8 + l) * 8 + m) * 8 + n) * 8 + o) * 8 + p] = n1;
									n1++;
								}
							}
						}
					}
				}
			}
		}
	}
	cout << "cdict " << cdict.size() << endl;
	
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
			for (auto& key_value : cdict) {
				int key = key_value.first;
				short c[8]{}, dc[8]{};
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
				cmap[key_value.second] = cdict.at(((((((c[0] * 8 + c[1]) * 8 + c[2]) * 8 + c[3]) * 8 + c[4]) * 8 + c[5]) * 8 + c[6]) * 8 + c[7]);
			}
			cr[f][t] = cmap;

			unordered_map<unsigned short, unsigned short> comap;
			for (auto& key_value : codict) {
				int key = key_value.first;
				short co[8]{}, dco[8]{};
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
				comap[key_value.second] = codict.at(((((((co[0] * 6 + co[1]) * 6 + co[2]) * 6 + co[3]) * 6 + co[4]) * 6 + co[5]) * 6 + co[6]) * 6 + co[7]);
			}
			cor[f][t] = comap;

			unordered_map<unsigned short, unsigned short> eomap;
			for (auto& key_value : eodict) {
				int key = key_value.first;
				short eo[12]{}, deo[12]{};
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
				eomap[key_value.second] = eodict.at(((((((((((eo[0] * 6 + eo[1]) * 6 + eo[2]) * 6 + eo[3]) * 6 + eo[4]) * 6 + eo[5]) * 6 + eo[6]) * 6 + eo[7]) * 6 + eo[8]) * 6 + eo[9]) * 6 + eo[10]) * 6 + eo[11]);
			}
			eor[f][t] = eomap;

			unordered_map<unsigned short, unsigned short> ep4map;
			for (auto& key_value : ep4dict) {
				int key = key_value.first;
				short ep4[4]{};
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
				ep4map[key_value.second] = ep4dict.at(((ep4[0] * 12 + ep4[1]) * 12 + ep4[2]) * 12 + ep4[3]);
			}
			ep4r[f][t] = ep4map;
		}

	}
	tinit = clock() - tinit;
	cout << "initialize time " << (double)tinit / CLOCKS_PER_SEC << "s" << endl;

	unordered_map<unsigned short, unsigned short> cr0[6] = { cr[0][0],cr[1][0],cr[2][0],cr[3][0],cr[4][0],cr[5][0] };
	unordered_map<unsigned short, unsigned short> cor0[6] = { cor[0][0],cor[1][0],cor[2][0],cor[3][0],cor[4][0],cor[5][0] };
	unordered_map<unsigned short, unsigned short> eor0[6] = { eor[0][0],eor[1][0],eor[2][0],eor[3][0],eor[4][0],eor[5][0] };
	unordered_map<unsigned short, unsigned short> ep4r0[6] = { ep4r[0][0],ep4r[1][0],ep4r[2][0],ep4r[3][0],ep4r[4][0],ep4r[5][0] };
	unordered_map<unsigned short, unsigned short> cr1[6] = { cr[0][1],cr[1][1],cr[2][1],cr[3][1],cr[4][1],cr[5][1] };
	unordered_map<unsigned short, unsigned short> ep4r1[6] = { ep4r[0][1],ep4r[1][1],ep4r[2][1],ep4r[3][1],ep4r[4][1],ep4r[5][1] };
	unsigned short ccn = 0, ccon = 0, cen1 = 0, cen2 = 10200, cen3 = 11856, ceon = 0;

	unsigned long long eighteen[16] = { 1 };
	for (int i = 1; i <= 15; i++) {
		eighteen[i] = 18 * eighteen[i - 1];
	}

	short phase1step = 5;
	short dict1step = 7;
	short dict2step = 8;
	short stepshouldbelow = phase1step + dict1step + dict2step + 1;
	int cubenumber = 10;
	short threadn = 6;

	if (argc >= 4) {
		phase1step = atoi(argv[1]);
		dict1step = atoi(argv[2]);
		dict2step = atoi(argv[3]);
	}
	if (argc >= 5) {
		cubenumber = atoi(argv[4]);
	}
	if (argc >= 6) {
		threadn = atoi(argv[5]);
	}
	cout << phase1step << " + " << dict1step << " + " << dict2step << endl;
	clock_t tdict0, tdict1, tdict2, starttime;
	tdict0 = clock();
	unordered_map<unsigned int, unsigned long long int> dict1 = getdict1(dict1step, cor0, eor0, ep4r0);
	tdict1 = clock();
	unordered_map<unsigned long long int, unsigned long long int> dict2 = getdict2(dict2step,eighteen,cr0,ep4r0,cr1,ep4r1);
	tdict2 = clock();
	cout << "dicts time " << (double)(tdict2 - tdict0) / CLOCKS_PER_SEC << "s = " << (double)(tdict1 - tdict0) / CLOCKS_PER_SEC << "s + " << (double)(tdict2 - tdict1) / CLOCKS_PER_SEC << "s" << endl;
	cout << cubenumber << " cubes " << threadn << " threads" << endl;
	list<short> htms,qtms,stms;
	
	starttime = clock();
	for (int i = 0; i < cubenumber; i++) {
		cout << endl << endl << "cube " << i + 1 << endl;
		time(&rawtime);
		info = localtime(&rawtime);
		strftime(buffer, 64, "%Y-%m-%d %H:%M:%S", info);
		cout << buffer << endl;
		cout << "search depth " << phase1step << " + " << dict1step << " + " << dict2step << " = " << stepshouldbelow - 1 << endl;

		short randomstrings[2][5000];
		srand((unsigned)time(NULL));
		int a = 1024 + rand() % 1024;
		cout << "random with " << a << " moves" << endl;
		randomcube(randomstrings,a);
		cubepack unsolvedcubes[6];
		getcubewithbase(unsolvedcubes,randomstrings, a, cr, cor, eor, ep4r);

		short htm = stepshouldbelow;
		short qtm = 2 * stepshouldbelow;
		short stm = stepshouldbelow;
		unsigned long long minmovep1=0, minmovep2=0;
		solvereturn sr[6]{};
		for (int j = 0; j < threadn; j++) {
			sr[j]=solve(unsolvedcubes[j], j, htm, qtm, stm, phase1step, cr0, cor0, eor0, ep4r0, cr1, ep4r1, cr, ep4r, eor, &dict1, &dict2);
			if (htm > sr[j].htm) {
				minmovep1 = sr[j].minmovep1;
				minmovep2 = sr[j].minmovep2;
			}
			htm = sr[j].htm;
			qtm = sr[j].qtm;
			stm = sr[j].stm;
		}
		cout << "finish solve cube " << i+1 << endl;
		if (htm >= stepshouldbelow) {
			cout << "no solution" << endl;
		}
		else {
			htms.push_back(htm);
			qtms.push_back(qtm);
			stms.push_back(stm);
			cout << "min htm " << htm <<" qtm "<<qtm<<" stm "<<stm << endl<<"solution "<<minmovep1<<"  "<<minmovep2<<"    "<<endl;//decode value
			while (minmovep1 >= 18) {
				cout << minmovep1 / 3 % 6 << minmovep1 % 3;
				minmovep1 /= 18;
			}
			while (minmovep2 >= 18) {
				cout << minmovep2 / 3 % 6 << minmovep2 % 3;
				minmovep2 /= 18;
			}
			cout << endl;
			double ahtm = 0;
			for (short s : htms) {
				ahtm += s;
			}
			ahtm = ahtm / htms.size();
			cout << "average htm " << ahtm<<endl;
		}
	}

	cout << "two phase algorithm version 25" << endl << endl;

	time(&rawtime);
	info = localtime(&rawtime);
	strftime(buffer, 64, "%Y-%m-%d %H:%M:%S", info);
	cout << buffer << endl;
	
	cout << "average time " << (double)(clock() - starttime) / cubenumber / CLOCKS_PER_SEC << "s" << endl;

	cout << "htm" << endl;
	double ahtm = 0;
	for (short s : htms) {
		ahtm += s;
		cout << s << " ";
	}
	cout << endl;
	ahtm = ahtm / htms.size();
	cout << "average htm " << ahtm << endl;

	//cout << "Press enter";
	//cin.get();
}
